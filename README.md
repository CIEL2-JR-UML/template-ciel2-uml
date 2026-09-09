# 📐 Cours & Travaux Pratiques UML — BTS CIEL 2ème Année

[![GitHub Template](https://img.shields.io/badge/Template-Repository-blue?logo=github)](https://github.com/CIEL2-JR-UML)
[![BTS CIEL](https://img.shields.io/badge/BTS-CIEL%20(IR%20%2F%20ER)-orange.svg)](https://eduscol.education.fr)
[![UML 2.5](https://img.shields.io/badge/Standard-UML%202.5-brightgreen.svg)](https://www.omg.org/spec/UML/)
[![C++ / Python](https://img.shields.io/badge/Langages-C%2B%2B20%20%7C%20Python%203-blueviolet.svg)](cours/07-passage-uml-vers-code/)
[![PlantUML & Mermaid](https://img.shields.io/badge/Outils-PlantUML%20%26%20Mermaid-success.svg)](ressources/)

Ce dépôt constitue le **modèle (template repository) officiel de cours, travaux pratiques et ressources** pour l'apprentissage et la mise en application de la modélisation **UML (Unified Modeling Language)** en **BTS CIEL 2ème année** (Cybersécurité, Informatique et Réseaux, Électronique), options **Informatique & Réseaux (IR)** et **Électronique & Réseaux (ER)**.

---

## 🎯 Objectifs Pédagogiques

Au terme de ce module, l'étudiant est capable de :
1. **Analyser un cahier des charges** et formaliser le besoin client avec le **Diagramme des Cas d'Utilisation (UC)**.
2. **Concevoir l'architecture statique** d'une application ou d'un firmware avec le **Diagramme de Classes** (encapsulation, relations, héritage, cardinalités).
3. **Modéliser les interactions dynamiques** entre objets et services réseau (MQTT, HTTP, Sockets) avec le **Diagramme de Séquence**.
4. **Décrire les comportements réactifs et les protocoles** de communication à l'aide du **Diagramme d'États-Transitions** (indispensable pour l'embarqué et les objets connectés).
5. **Formaliser des algorithmes et processus** avec le **Diagramme d'Activité**.
6. **Traduire fidèlement la modélisation UML en code** propre en **C++** (Qt / STL) et en **Python**.
7. **Pratiquer l'outillage moderne** : GitHub, rendu Markdown / Mermaid natif, PlantUML sous VS Code, gestion de versions Git.

---

## 🗺️ Sommaire & Progression Pédagogique

| Module | Titre | Thèmes Clés | Diagrammes |
| :---: | :--- | :--- | :---: |
| **01** | [**Démarche & Cycle de vie**](cours/01-demarche-conception-uml/) | Cycle en V, Agilité, Rôle de l'UML dans les épreuves E5/E6 | — |
| **02** | [**Cas d'Utilisation (UC)**](cours/02-diagramme-cas-utilisation-uc/) | Acteurs, frontière, `<<include>>`, `<<extend>>`, généralisation, fiches textuelles | Use Case |
| **03** | [**Diagramme de Classes**](cours/03-diagramme-classes/) | Attributs, méthodes, visibilité, association, agrégation, composition, multiplicités | Classes |
| **04** | [**Diagramme de Séquence**](cours/04-diagramme-sequence/) | Lignes de vie, messages synchrones/asynchrones, fragments `alt`, `loop`, `opt`, `par` | Séquence |
| **05** | [**États-Transitions**](cours/05-diagramme-etats-transitions/) | Automates finis, événements `[garde] / action`, timeouts, focus embarqué/réseau | Machine d'États |
| **06** | [**Diagramme d'Activité**](cours/06-diagramme-activites/) | Flux de contrôle, aiguillages, parallélisme `fork`/`join`, couloirs de responsabilité | Activité |
| **07** | [**Passage UML $\rightarrow$ Code**](cours/07-passage-uml-vers-code/) | Traduction concrète vers **C++** et **Python**, gestion des relations 1-1, 1-N, agrégation | Classes $\rightarrow$ Code |

---

## 🛠️ Travaux Pratiques & Évaluations

Chaque TP contient un énoncé guidé, un cahier des charges réaliste, des fichiers de départ et des grilles d'évaluation :

| TP | Sujet | Contexte Métier BTS CIEL | Livrables Attendus |
| :---: | :--- | :--- | :--- |
| **TP 1** | [**Borne de Recharge IRVE**](tp-exercices/tp1-cas-utilisation-borne-irve/) | Borne communicante pour véhicules électriques | Diagramme Use Case, fiches de cas d'utilisation |
| **TP 2** | [**Passerelle IoT Multi-Capteurs**](tp-exercices/tp2-classes-passerelle-iot/) | Passerelle réseau collectant des capteurs (I2C/SPI) | Diagramme de classes $\rightarrow$ Code C++ et Python |
| **TP 3** | [**Protocole & Machine d'États**](tp-exercices/tp3-etats-transitions-protocole/) | Protocole communicant capteur/passerelle sur bus série | Diagramme d'états-transitions, diagramme de séquence |
| **TP 4** | [**Projet de Synthèse : Contrôle d'Accès**](tp-exercices/tp4-projet-synthese-controle-acces/) | Lecteur RFID, gâche électrique, serveur d'autorisation | Modélisation complète de bout en bout + squelette |

---

## 🚀 Utilisation de ce Dépôt (Modèle / Template)

### Pour l'enseignant :
1. Ce dépôt est configuré comme **Template Repository** dans l'organisation `CIEL2-JR-UML`.
2. Il sert de modèle unique pour générer les dépôts de travail des étudiants ou binômes.

### Pour l'étudiant :
1. Cliquez sur le bouton vert **« Use this template »** (en haut à droite sur GitHub) $\rightarrow$ **« Create a new repository »**.
2. Sélectionnez l'organisation `CIEL2-JR-UML` comme propriétaire.
3. Nommez votre dépôt selon la consigne (ex : `tp-uml-NOM-PRENOM`).
4. Choisissez la visibilité **Privé**.
5. Clonez votre dépôt localement :
   ```bash
   git clone https://github.com/CIEL2-JR-UML/tp-uml-NOM-PRENOM.git
   cd tp-uml-NOM-PRENOM
   ```

---

## 💻 Environnement Recommandé (VS Code)

1. **Éditeur :** [Visual Studio Code](https://code.visualstudio.com/)
2. **Extensions recommandées :**
   - **PlantUML** (`jebbs.plantuml`) : rendu et export instantané (`Alt+D`).
   - **Markdown Preview Mermaid Support** (`bierner.markdown-mermaid`) : aperçu natif des diagrammes dans le Markdown (`Ctrl+K V`).
3. Consultez le [**Guide d'installation de l'outillage**](ressources/guide-outillage-vscode.md) pour configurer Java et Graphviz sous Windows et Linux.

---

## 📚 Ressources & Aides-Mémoires

- 📖 [**Mémento UML CIEL (Cheatsheet)**](ressources/cheatsheet-uml-ciel.md) : Synthèse rapide des symboles, flèches, cardinalités et règles d'or.
- 📐 [**Modèles PlantUML prêts à l'emploi**](ressources/modeles-plantuml/) : Fichiers `.puml` modèles commentés.

---

## 👥 Licence

Ce projet pédagogique est sous licence [MIT](LICENSE). Conçu pour les formations de la filière **BTS CIEL**.
