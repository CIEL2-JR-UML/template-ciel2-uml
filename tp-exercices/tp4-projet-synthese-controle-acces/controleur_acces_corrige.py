# CORRECTION TP 4 : Implémentation Logicielle Orientée Objet (Python 3)
# Contrôle d'Accès Sécurisé par Badge RFID

class LecteurRFID:
    def __init__(self, port: str = "/dev/ttyUSB0"):
        self.port = port

    def lire_uid(self) -> str:
        return "UID_A1B2"

class GacheElectrique:
    def __init__(self, pin_gpio: int = 18):
        self.pin_gpio = pin_gpio
        self.est_ouverte = False

    def deverrouiller(self, secondes: int = 5) -> None:
        self.est_ouverte = True
        print(f"[ACTION MATÉRIELLE] Gâche déverrouillée pendant {secondes} secondes (Porte ouverte)")

class Signalisation:
    def __init__(self, led_verte: int = 23, led_rouge: int = 24):
        self.led_verte = led_verte
        self.led_rouge = led_rouge

    def acces_autorise(self) -> None:
        print("[SIGNALISATION] LED VERTE allumée (Bip court : Accès Accordé)")

    def acces_refuse(self) -> None:
        print("[SIGNALISATION] LED ROUGE clignotante (Bips répétés : Accès Refusé)")

class ClientAuthAPI:
    def __init__(self, url_serveur: str = "https://auth.ciel.lan/api"):
        self.url_serveur = url_serveur
        # Base d'utilisateurs simulée
        self._utilisateurs = {
            "UID_A1B2": "1234", # Usager autorisé
            "UID_C3D4": "9999", # Usager autorisé
        }

    def valider_droits(self, uid: str, pin: str) -> bool:
        return self._utilisateurs.get(uid) == pin

class ControleurAcces:
    def __init__(self, nom_zone: str, api: ClientAuthAPI):
        self.nom_zone = nom_zone
        
        # Composition : composants matériels internes
        self._lecteur = LecteurRFID()
        self._gache = GacheElectrique()
        self._signal = Signalisation()
        
        # Agrégation : service externe
        self._api = api

    def traiter_identification(self, uid: str, pin: str) -> bool:
        print(f"\n--- Traitement badge {uid} sur zone '{self.nom_zone}' ---")
        
        # TODO RÉSOLU :
        est_valide = self._api.valider_droits(uid, pin)
        if est_valide:
            self._gache.deverrouiller(5)
            self._signal.acces_autorise()
            return True
        else:
            self._signal.acces_refuse()
            return False

# ==============================================================================
# Programme de test
# ==============================================================================
if __name__ == "__main__":
    print("=== TEST CORRECTION CONTRÔLE D'ACCÈS RFID (BTS CIEL) ===")
    
    api_centrale = ClientAuthAPI()
    controleur = ControleurAcces("Salle Serveurs Baie 1", api_centrale)

    # Test 1 : Badge valide
    print("\n[TEST 1] Tentative avec badge valide ('UID_A1B2') et code PIN '1234' :")
    controleur.traiter_identification("UID_A1B2", "1234")

    # Test 2 : Badge refusé
    print("\n[TEST 2] Tentative avec badge inconnu ('UID_INCONNU') :")
    controleur.traiter_identification("UID_INCONNU", "0000")
