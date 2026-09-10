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
        # ==============================================================================
        # TODO 1 : Gestion de l'agrégation
        # Ajoutez l'objet 'capteur' à la liste 'self._capteurs' si le capteur existe.
        # Indice : if capteur is not None: self._capteurs.append(capteur)
        # ==============================================================================
        pass

    def executer_cycle_mesure(self) -> None:
        print(f">> Lancement du cycle sur {self._nom} ({self._ip})")
        # ==============================================================================
        # TODO 2 : Parcours polymorphique de la collection
        # Parcourez 'self._capteurs'. Pour chaque capteur 'c', appelez c.acquerir()
        # et affichez 'c.label' et 'c.valeur'.
        # Indice :
        # for c in self._capteurs:
        #     if c.acquerir():
        #         print(f"   -> [{c.label}] Valeur = {c.valeur}")
        # ==============================================================================

        self._afficheur.afficher(self._nom, f"Capteurs: {len(self._capteurs)} OK")

