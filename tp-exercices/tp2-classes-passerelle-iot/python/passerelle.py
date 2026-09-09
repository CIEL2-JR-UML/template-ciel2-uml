from typing import List
from capteur import Capteur

class AfficheurLCD:
    def afficher(self, l1: str, l2: str) -> None:
        print("================ LCD ================")
        print(f"[L1] {l1}")
        print(f"[L2] {l2}")
        print("=====================================")

class Passerelle:
    def __init__(self, nom: str, ip: str):
        self._nom = nom
        self._ip = ip
        self._capteurs: List[Capteur] = []  # Agrégation
        self._afficheur = AfficheurLCD()    # Composition

    def connecter_capteur(self, capteur: Capteur) -> None:
        if capteur is not None:
            self._capteurs.append(capteur)

    def executer_cycle_mesure(self) -> None:
        print(f">> Lancement du cycle sur {self._nom} ({self._ip})")
        for c in self._capteurs:
            if c.acquerir():
                print(f"   -> [{c.label}] Valeur = {c.valeur}")
        self._afficheur.afficher(self._nom, f"Capteurs: {len(self._capteurs)} OK")
