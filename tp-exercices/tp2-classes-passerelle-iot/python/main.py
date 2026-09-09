from capteur import Capteur
from passerelle import Passerelle

class CapteurTemperature(Capteur):
    def acquerir(self) -> bool:
        self._valeur = 23.8
        return True

class CapteurHumidite(Capteur):
    def acquerir(self) -> bool:
        self._valeur = 58.2
        return True

if __name__ == "__main__":
    print("=== DEMO TP 2 : PASSERELLE IOT (PYTHON - BTS CIEL 2) ===")
    passerelle = Passerelle("Gateway-SalleServeur", "192.168.10.254")

    s1 = CapteurTemperature(101, "Sonde Salle Baie 1")
    s2 = CapteurHumidite(102, "Humidite Ambiante")

    passerelle.connecter_capteur(s1)
    passerelle.connecter_capteur(s2)

    passerelle.executer_cycle_mesure()
