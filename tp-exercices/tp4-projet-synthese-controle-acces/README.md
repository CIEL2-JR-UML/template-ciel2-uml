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

## 3. Travail Demandé (Exercice Guidé à Trous)

Tous les fichiers de base sont fournis et pré-remplis à 80%. Suivez les balises `TODO` dans chaque fichier :

### Étape 1 : Cas d'Utilisation — [`controle_acces_uc.puml`](controle_acces_uc.puml)
*(Visualisez avec **`Alt + D`**)*
- **TODO 1 :** Ajouter l'héritage entre acteurs : `Secu --|> User`.
- **TODO 2 :** Ajouter l'inclusion obligatoire : `UC_Badge ..> UC_Valider : <<include>>`.
- **TODO 3 :** Ajouter l'extension optionnelle : `UC_Badge <.. UC_PIN : <<extend>>`.

### Étape 2 : Diagramme de Classes — [`controle_acces_classes.puml`](controle_acces_classes.puml)
*(Visualisez avec **`Alt + D`**)*
- **TODO 1 :** Déclarer la composition forte de la signalisation : `ControleurAcces *-- "1" Signalisation`.
- **TODO 2 :** Déclarer l'agrégation faible du service réseau : `ControleurAcces o-- "1" ClientAuthAPI`.

### Étape 3 : Diagramme de Séquence — [`controle_acces_sequence.puml`](controle_acces_sequence.puml)
*(Visualisez avec **`Alt + D`**)*
- **TODO 1.1 :** Dans la branche `alt` d'accès autorisé, appeler `Ctrl -> Gache : deverrouiller(5)`.
- **TODO 1.2 :** Déclencher le signal vert `Ctrl -> LED : accesAutorise()`.

### Étape 4 : Implémentation Python — [`controleur_acces.py`](controleur_acces.py)
- Ouvrez le script [`controleur_acces.py`](controleur_acces.py) et complétez la méthode `traiter_identification` (6 lignes simples indiquées dans le commentaire `TODO`).
- Lancez le script dans votre terminal : `python controleur_acces.py` pour valider les tests !


---

<div align="center">

| ⬅️ Précédent | 🏠 Accueil | ➡️ Suite Logique |
| :--- | :---: | ---: |
| [**Cours 05 : Passage UML vers Code**](../../cours/05-passage-uml-vers-code/) | [**Sommaire Général**](../../README.md) | [**Mémento UML CIEL ➔**](../../ressources/cheatsheet-uml-ciel.md) |

<br>

[<kbd> &nbsp; 📖 Consulter le Mémento de Révision UML CIEL ➔ &nbsp; </kbd>](../../ressources/cheatsheet-uml-ciel.md)

</div>

