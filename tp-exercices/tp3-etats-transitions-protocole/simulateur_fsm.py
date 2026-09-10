# -*- coding: utf-8 -*-
"""
Simulateur de l'automate à états finis (FSM) du protocole UART - TP 3 BTS CIEL.
Démontre le fonctionnement concret des transitions, gardes et timeouts.
"""
import enum
import time
import random

class Etat(enum.Enum):
    REPOS = 1
    ENVOI_REQUETE = 2
    ATTENTE_REPONSE = 3
    TRAITEMENT_DONNEES = 4
    DEFAUT_COMMUNICATION = 5

class AutomateProtocole:
    def __init__(self):
        self.etat = Etat.REPOS
        self.retry_count = 0
        self.max_retries = 3

    def declencher_releve(self):
        print(f"\n--- NOUVELLE TRANSACTION ---")
        self.etat = Etat.REPOS
        self.retry_count = 0

        # Événement : demande de relève
        self.etat = Etat.ENVOI_REQUETE
        self._executer_envoi()

    def _executer_envoi(self):
        while self.etat != Etat.REPOS and self.etat != Etat.DEFAUT_COMMUNICATION:
            if self.etat == Etat.ENVOI_REQUETE:
                print(f"[ETAT] ENVOI_REQUETE (Tentative {self.retry_count + 1}/{self.max_retries})")
                print("       -> Émission de la trame REQ sur bus RS485")
                self.etat = Etat.ATTENTE_REPONSE

            elif self.etat == Etat.ATTENTE_REPONSE:
                print("[ETAT] ATTENTE_REPONSE (Timer 3s armé)")
                # Simulation de la réponse (succès, corruption ou timeout)
                evenement = random.choice(["OK", "CRC_ERROR", "TIMEOUT"])
                time.sleep(0.5)

                if evenement == "OK":
                    print("       [OK] Trame réponse valide reçue avec CRC conforme !")
                    self.etat = Etat.TRAITEMENT_DONNEES
                else:
                    self.retry_count += 1
                    print(f"       [ERREUR] Incident détecté : {evenement}")
                    if self.retry_count < self.max_retries:
                        print(f"       -> Garde [retry < 3] vérifiée : Réémission.")
                        self.etat = Etat.ENVOI_REQUETE
                    else:
                        print(f"       -> Garde [retry >= 3] atteinte : Passage en DÉFAUT.")
                        self.etat = Etat.DEFAUT_COMMUNICATION

            elif self.etat == Etat.TRAITEMENT_DONNEES:
                print("[ETAT] TRAITEMENT_DONNEES : Émission ACK & Enregistrement BDD")
                self.etat = Etat.REPOS
                print("[ETAT] REPOS : Transaction achevée avec succès.")

        if self.etat == Etat.DEFAUT_COMMUNICATION:
            print("[ETAT] DEFAUT_COMMUNICATION : Alarme sonore active, attente opérateur.")

if __name__ == "__main__":
    automate = AutomateProtocole()
    # Test 1 : Scénario
    automate.declencher_releve()
    automate.declencher_releve()
