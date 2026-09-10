# 🛡️ TP 4 — Projet de Synthèse : Contrôle d'Accès Sécurisé

---

## 1. Présentation du Mini-Projet

Ce projet de synthèse simule une situation réelle d'épreuve professionnelle de BTS CIEL (E5/E6).  
Il vous demande de concevoir l'ensemble des modèles UML nécessaires au développement d'un **système de contrôle d'accès sécurisé par badge RFID et code PIN** pour un laboratoire informatique.

---

## 2. Cahier des Charges

Le système est constitué de :
1. Un **lecteur RFID** (détecte l'UID du badge).
2. Un **clavier codé** (saisie optionnelle d'un code PIN à 4 chiffres pour les zones sensibles).
3. Une **gâche électrique** (déverrouille la porte pendant 5 secondes).
4. Un **module de signalisation** (LED verte / rouge et buzzer).
5. Un **serveur d'authentification central** (interrogé par API réseau pour valider les droits).

---

## 3. Livrables Attendus (Le Trio Fondamental)

1. **Diagramme des Cas d'Utilisation :**
   - Acteurs (`Usager`, `Agent de sécurité`, `Serveur Authentification`).
   - Cas d'utilisation et dépendances (`<<include>>` pour la validation d'accès, `<<extend>>` pour la saisie du code PIN).
2. **Diagramme de Classes :**
   - Architecture orientée objet du firmware (`LecteurRFID`, `ClavierCode`, `GacheElectrique`, `Signalisation`, `ClientAuthAPI`, `ControleurAcces`).
   - Multiplicités, composition et agrégation.
3. **Diagramme de Séquence :**
   - Scénario chronologique complet : présentation du badge, saisie du PIN, requête au serveur, déverrouillage et temporisation de 5s.
4. **Implémentation logicielle :**
   - Squelette de code orienté objet en C++ ou Python pour la classe `ControleurAcces`.
