# 📐 Cours & Travaux Pratiques UML — BTS CIEL 2ème Année

[![GitHub Template](https://img.shields.io/badge/Template-Repository-blue?logo=github)](https://github.com/CIEL2-JR-UML)
[![BTS CIEL](https://img.shields.io/badge/BTS-CIEL%20(IR%20%2F%20ER)-orange.svg)](https://eduscol.education.fr)
[![UML 2.5](https://img.shields.io/badge/Focus-UC%20%7C%20Classes%20%7C%20Séquence-brightgreen.svg)](https://www.omg.org/spec/UML/)
[![C++ / Python](https://img.shields.io/badge/Langages-C%2B%2B20%20%7C%20Python%203-blueviolet.svg)](cours/05-passage-uml-vers-code/)
[![PlantUML & SVG](https://img.shields.io/badge/Rendu-SVG%20%26%20PlantUML-success.svg)](ressources/)

Ce dépôt constitue le **modèle officiel de cours, travaux pratiques et ressources** pour l'apprentissage et la mise en application des **3 diagrammes fondamentaux de l'UML** en **BTS CIEL 2ème année** (Cybersécurité, Informatique et Réseaux, Électronique) :
1. **Diagramme des Cas d'Utilisation (Use Case)** : Expression du besoin fonctionnel et acteurs.
2. **Diagramme de Classes** : Conception de l'architecture statique orientée objet.
3. **Diagramme de Séquence** : Modélisation des interactions dynamiques et protocoles réseaux.

---

## 🗺️ Sommaire & Progression Pédagogique

| Module | Titre | Thèmes Clés | Diagramme |
| :---: | :--- | :--- | :---: |
| **01** | [**Démarche & Rôle de l'UML**](cours/01-demarche-conception-uml/) | Cycle en V, Agilité, Le trio fondamental dans les épreuves E5/E6 | — |
| **02** | [**Cas d'Utilisation (UC)**](cours/02-diagramme-cas-utilisation-uc/) | Acteurs, frontière, `<<include>>`, `<<extend>>`, héritage, fiches textuelles | Use Case |
| **03** | [**Diagramme de Classes**](cours/03-diagramme-classes/) | Attributs, méthodes, visibilité, association, agrégation, composition, multiplicités | Classes |
| **04** | [**Diagramme de Séquence**](cours/04-diagramme-sequence/) | Lignes de vie, messages synchrones/asynchrones, fragments `alt`, `loop`, `opt` | Séquence |
| **05** | [**Passage UML $\rightarrow$ Code**](cours/05-passage-uml-vers-code/) | Traduction concrète des classes et relations vers **C++20** et **Python 3** | Classes $\rightarrow$ Code |

---

## 🛠️ Travaux Pratiques & Évaluations

| TP | Sujet | Contexte Métier BTS CIEL | Compétences Clés |
| :---: | :--- | :--- | :--- |
| **TP 1** | [**Borne de Recharge IRVE**](tp-exercices/tp1-cas-utilisation-borne-irve/) | Borne communicante pour véhicules électriques | Diagramme Use Case, inclusions/extensions, fiche de cas |
| **TP 2** | [**Passerelle IoT Multi-Capteurs**](tp-exercices/tp2-classes-passerelle-iot/) | Passerelle réseau collectant des capteurs (I2C/SPI) | Diagramme de classes $\rightarrow$ Implémentation C++ et Python |
| **TP 3** | [**Supervision & Protocoles MQTT**](tp-exercices/tp3-sequence-supervision-mqtt/) | Télémétrie capteurs, broker MQTT, accusés et alertes | Diagramme de séquence, fragments `alt`, `loop`, timeouts |
| **TP 4** | [**Projet de Synthèse : Contrôle d'Accès**](tp-exercices/tp4-projet-synthese-controle-acces/) | Lecteur RFID, gâche électrique, serveur central | Conception complète (UC + Classes + Séquence + Code) |

---

## 🚀 Utilisation de ce Dépôt (Template)

### Pour l'étudiant :
1. Cliquez sur le bouton vert **« Use this template »** $\rightarrow$ **« Create a new repository »**.
2. Sélectionnez l'organisation `CIEL2-JR-UML` et nommez votre dépôt (ex : `tp-uml-NOM`).
3. Choisissez la visibilité **Privé**.
4. Clonez votre dépôt pour travailler sous **VS Code** (avec l'extension PlantUML et le raccourci `Alt + D`) ou directement sur votre navigateur via la touche **`.`** de GitHub.

---

## 📚 Ressources & Aides-Mémoires

- 📖 [**Mémento UML CIEL (Cheatsheet)**](ressources/cheatsheet-uml-ciel.md) : Synthèse rapide des 3 diagrammes, flèches, cardinalités et règles d'or.
- 🛠️ [**Tutoriel Rapide PlantUML**](ressources/tuto-plantuml.md) : Guide pas à pas de la syntaxe du code `.puml`.
- 📐 [**Modèles PlantUML prêts à l'emploi**](ressources/modeles-plantuml/) : Templates commentés pour Use Case, Classes et Séquence.
