# 🛠️ Guide d'Installation de l'Outillage (VS Code & PlantUML)

Ce guide détaille la configuration de votre poste de travail pour éditer, prévisualiser et exporter vos diagrammes UML.

---

## 1. Installation de Visual Studio Code

Téléchargez et installez VS Code depuis le site officiel :  
👉 [https://code.visualstudio.com/](https://code.visualstudio.com/)

---

## 2. Extensions Indispensables

Installez les extensions suivantes depuis le menu des extensions de VS Code (`Ctrl+Shift+X`) :

1. **PlantUML** (par *jebbs*)  
   - ID : `jebbs.plantuml`  
   - Permet de visualiser les diagrammes `.puml` via le raccourci `Alt+D`.
2. **Markdown Preview Mermaid Support** (par *Matt Bierner*)  
   - ID : `bierner.markdown-mermaid`  
   - Permet à VS Code d'afficher directement les diagrammes Mermaid inclus dans les fichiers `.md`.
3. **C/C++** (par *Microsoft*)  
   - ID : `ms-vscode.cpptools`  
   - Indispensable pour la complétion et la vérification syntaxique du code C++.
4. **Python** (par *Microsoft*)  
   - ID : `ms-python.python`

---

## 3. Prérequis Système pour PlantUML (Local)

PlantUML génère les schémas vectoriels à l'aide de **Java** et du moteur de graphes **Graphviz**.

### Option A : Sous Windows
1. Installez Java JRE ou JDK (ex: OpenJDK ou Java de Oracle).
2. Installez Graphviz :
   - Via **winget** dans PowerShell :
     ```powershell
     winget install Graphviz.Graphviz
     ```
   - Ou téléchargez l'installateur sur : [https://graphviz.org/download/](https://graphviz.org/download/)
3. Dans VS Code, vérifiez que le chemin vers `dot.exe` est détecté (automatique si ajouté au PATH).

### Option B : Sous Linux (Ubuntu / Debian)
```bash
sudo apt update
sudo apt install -y default-jre graphviz
```

### Option C : Utiliser le serveur PlantUML distant (sans installer Java/Graphviz)
Si vous ne souhaitez rien installer en local, vous pouvez configurer VS Code pour utiliser le serveur public :
1. Ouvrez les paramètres VS Code (`Ctrl+,`).
2. Cherchez `plantuml.server`.
3. Indiquez : `https://www.plantuml.com/plantuml`
4. Changez `plantuml.render` à `PlantUMLServer`.

---

## 4. Raccourcis Claviers Utiles

| Action | Raccourci Windows / Linux |
| :--- | :---: |
| **Aperçu du diagramme PlantUML actif** | `Alt + D` |
| **Exporter le diagramme en PNG / SVG** | `Ctrl + Shift + P` $\rightarrow$ *PlantUML: Export Current Diagram* |
| **Aperçu d'un fichier Markdown à côté** | `Ctrl + K` puis `V` |
| **Ouvrir le terminal intégré** | `Ctrl + \`` |
