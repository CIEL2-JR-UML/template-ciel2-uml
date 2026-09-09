# 🛡️ TP 4 — Projet de Synthèse : Système de Contrôle d'Accès Sécurisé

---

## 1. Présentation du Mini-Projet

Ce mini-projet de synthèse simule une situation réelle d'épreuve professionnelle de BTS CIEL. Il vous demande de concevoir l'ensemble des modèles UML nécessaires au développement d'un **système de contrôle d'accès pour un laboratoire électronique / cybersécurité**.

---

## 2. Cahier des Charges

Le système est composé de :
1. Un **lecteur de badge RFID** (13.56 MHz).
2. Un **clavier numérique 12 touches** (code secret complémentaire pour les salles sensibles).
3. Une **gâche électromagnétique** de verrouillage de porte.
4. Une **LED bicolore** (Verte / Rouge) et un **buzzer**.
5. Une **carte contrôleur IP** reliée au réseau du lycée et dialoguant avec un serveur d'authentification central (API REST / HTTPS).

### Règles de Fonctionnement :
- Dès qu'un badge est présenté, le système lit son UID.
- Si le badge requiert une double authentification (salle serveur), le système sollicite la saisie d'un code PIN à 4 chiffres.
- La requête est transmise au serveur central :
  - **Autorisé :** La gâche est déverrouillée pendant 5 secondes, la LED verte s'allume, un bip court retentit.
  - **Refusé :** La porte reste verrouillée, la LED rouge clignote, un bip long retentit, une alerte intrusion est envoyée au serveur.
- Si la porte n'est pas refermée au bout de 30 secondes (capteur magnétique de porte), une alarme locale sonne en continu.

---

## 3. Livrables Attendus

1. **Dossier de Modélisation UML :**
   - **Diagramme Use Case :** Acteurs (Usager, Vigile, Serveur Central) et fonctionnalités.
   - **Diagramme de Classes :** Modélisation orientée objet du firmware (`LecteurRFID`, `Gache`, `Clavier`, `ControleurAcces`, `ClientAuthAPI`).
   - **Diagrammes de Séquence :** Scénario d'accès autorisé avec double authentification, et scénario de refus.
   - **Diagramme d'États-Transitions :** Cycle de vie de la porte et de sa gâche (`Verrouillee`, `DeverrouilleeTemporaire`, `AlarmePorteResteeOuverte`).
2. **Squelette de code orienté objet :**
   - Implémentation en C++ ou en Python de la classe principale `ControleurAcces`.
