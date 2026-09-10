# 💻 TP 2 — Diagramme de Classes & Implémentation C++ / Python

---

## 1. Objectif du TP

Dans ce TP, vous allez modéliser puis implémenter l'architecture logicielle d'une **Passerelle IoT multi-capteurs** destinée à surveiller un local technique informatique (salle serveurs BTS CIEL).

---

## 2. Spécification de l'Architecture

1. **Classe abstraite `Capteur` :**
   - Attributs protégés : `m_id` (int), `m_label` (string), `m_valeur` (float).
   - Méthodes publiques : constructeur, destructeur virtuel, getters, et méthode virtuelle pure `virtual bool acquerir() = 0`.
2. **Classes concrètes dérivées :**
   - `CapteurTemperature` : possède un attribut privé `m_unite` (string, ex: `"°C"`).
   - `CapteurHumidite` : possède un attribut privé `m_pourcentageRelatif` (bool).
3. **Classe `AfficheurLCD` :**
   - Gère l'affichage local (2 lignes de 16 caractères).
   - Méthode `afficherMessage(string ligne1, string ligne2)`.
4. **Classe `Passerelle` :**
   - Possède un nom et une adresse IP.
   - **Agrège** une collection de pointeurs vers des `Capteur` (relation 0..*).
   - **Est composée** d'un objet `AfficheurLCD` (relation de composition 1).
   - Méthodes pour ajouter un capteur, déclencher l'acquisition de tous les capteurs, et afficher la synthèse.

---

## 3. Travail Demandé

1. **Diagramme de classes UML :**
   - Réalisez le diagramme de classes complet sous forme de fichier PlantUML `passerelle.puml` *(Visualisez avec **`Alt + D`**)*.
2. **Implémentation :**
   - Le code squelette est fourni en **C++** (dossier `cpp/`) et en **Python** (dossier `python/`).
   - Complétez les méthodes d'acquisition et de gestion de la collection.
3. **Validation :**
   - En C++ : compilez avec `make` et exécutez le binaire `./passerelle_iot`.
   - En Python : lancez `python main.py`.

---

<div align="center">

| ⬅️ Précédent | 🏠 Accueil | ➡️ Suite Logique |
| :--- | :---: | ---: |
| [**Cours 03 : Diagramme de Classes**](../../cours/03-diagramme-classes/) | [**Sommaire des TP**](../README.md) | [**Chapitre 04 : Diagramme de Séquence ➔**](../../cours/04-diagramme-sequence/) |

<br>

[<kbd> &nbsp; ➡️ Passer à l'étape suivante : Chapitre 04 — Diagramme de Séquence &nbsp; </kbd>](../../cours/04-diagramme-sequence/)

</div>

