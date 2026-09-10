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

---

## 3. Travail Demandé (Exercice Guidé à Trous)

Les fichiers de départ sont déjà pré-remplis à 80% ! Vous avez uniquement quelques lignes ciblées à compléter.

### Étape 1 : Compléter le diagramme de classes [`passerelle.puml`](passerelle.puml)
Ouvrez [`passerelle.puml`](passerelle.puml) *(prévisualisation avec **`Alt + D`**)* et complétez les balises `TODO` :
- **TODO 1 :** Renseigner l'attribut de `CapteurTemperature` (`- m_unite : string`) et de `CapteurHumidite` (`- m_pourcentageRelatif : bool`).
- **TODO 2 :** Déclarer les 2 relations d'héritage `<|--` vers la classe mère `Capteur`.
- **TODO 3 :** Déclarer l'agrégation faible `o--` entre `Passerelle` et `Capteur` (cardinalité `"0..*"`).
- **TODO 4 :** Déclarer la composition forte `*--` entre `Passerelle` et `AfficheurLCD` (cardinalité `"1"`).

### Étape 2 : Compléter le code (C++ ou Python au choix)
- **En C++ :** Ouvrez [`cpp/Passerelle.cpp`](cpp/Passerelle.cpp) et complétez `TODO 1` (`m_capteurs.push_back`) et `TODO 2` (boucle d'acquisition). Compilez avec `make` et testez avec `./passerelle_iot`.
- **En Python :** Ouvrez [`python/passerelle.py`](python/passerelle.py) et complétez `TODO 1` (`self._capteurs.append`) et `TODO 2` (boucle d'acquisition). Testez avec `python main.py`.


---

<div align="center">

| ⬅️ Précédent | 🏠 Accueil | ➡️ Suite Logique |
| :--- | :---: | ---: |
| [**Cours 03 : Diagramme de Classes**](../../cours/03-diagramme-classes/) | [**Sommaire des TP**](../README.md) | [**Chapitre 04 : Diagramme de Séquence ➔**](../../cours/04-diagramme-sequence/) |

<br>

[<kbd> &nbsp; ➡️ Passer à l'étape suivante : Chapitre 04 — Diagramme de Séquence &nbsp; </kbd>](../../cours/04-diagramme-sequence/)

</div>

