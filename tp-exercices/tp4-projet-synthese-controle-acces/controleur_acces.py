# -*- coding: utf-8 -*-
"""
Prototype Python complet du système de Contrôle d'Accès Sécurisé (TP 4 BTS CIEL).
"""
import time

class GacheElectrique:
    def __init__(self):
        self._verrouillee = True

    def deverrouiller(self):
        self._verrouillee = False
        print("  [GÂCHE] >> Pêne déverrouillé (Passage autorisé pendant 5s)")

    def verrouiller(self):
        self._verrouillee = True
        print("  [GÂCHE] >> Pêne ré-enclenché (Porte verrouillée)")

class Signalisation:
    def acces_autorise(self):
        print("  [SIGNAL] LED Verte ALLUMÉE + 1 Bip Court (Bip!)")

    def acces_refuse(self):
        print("  [SIGNAL] LED Rouge CLIGNOTANTE + 1 Bip Long (Biiiiip!)")

class ServiceAuthentification:
    def __init__(self):
        # Base de données d'utilisateurs simulée
        self.utilisateurs = {
            "A1-B2-C3-D4": {"nom": "Professeur CIEL", "pin": "1234", "salle_serveur": True},
            "99-88-77-66": {"nom": "Étudiant 1", "pin": "", "salle_serveur": False}
        }

    def verifier_acces(self, uid: str, pin: str = "") -> bool:
        user = self.utilisateurs.get(uid)
        if not user:
            return False
        if user["salle_serveur"]:
            return user["pin"] == pin
        return True

class ControleurAcces:
    def __init__(self, id_porte: str, requiert_pin: bool = False):
        self.id_porte = id_porte
        self.requiert_pin = requiert_pin
        self.gache = GacheElectrique()
        self.signal = Signalisation()
        self.auth_srv = ServiceAuthentification()

    def badge_presente(self, uid: str, pin_saisi: str = ""):
        print(f"\n[PORTAL {self.id_porte}] Badge détecté : UID = {uid}")
        if self.auth_srv.verifier_acces(uid, pin_saisi):
            print("  [AUTH] Accès ACCORDÉ")
            self.signal.acces_autorise()
            self.gache.deverrouiller()
            time.sleep(1) # Simulation temporisation
            self.gache.verrouiller()
        else:
            print("  [AUTH] Accès REFUSÉ (Badge invalide ou mauvais PIN)")
            self.signal.acces_refuse()

if __name__ == "__main__":
    controleur_labo = ControleurAcces("SALLE-INFORMATIQUE-CIEL", requiert_pin=True)
    # Test 1 : Badge autorisé avec bon PIN
    controleur_labo.badge_presente("A1-B2-C3-D4", "1234")
    # Test 2 : Badge inconnu
    controleur_labo.badge_presente("00-11-22-33")
