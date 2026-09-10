# 📝 Corrigé TP 2 — Diagramme de Classes & Implémentation C++ / Python

---

## 1. Justification des Choix de Conception

1. **Classe Abstraite `Capteur` :**
   - On ne peut pas instancier un « capteur générique » sans savoir comment mesurer physiquement.
   - En C++ : `virtual bool acquerir() = 0;` (méthode virtuelle pure).
   - En Python : décorateur `@abstractmethod` via la classe mère `abc.ABC`.
2. **Agrégation (`Passerelle o-- Capteur`) :**
   - La passerelle ne « possède » pas les capteurs physiquement au sens du cycle de vie : les capteurs peuvent être débranchés, remplacés ou exister avant la passerelle.
   - En destructeur C++ : la passerelle **ne doit pas faire `delete`** sur les capteurs, car ils ont été alloués en dehors.
3. **Composition (`Passerelle *-- AfficheurLCD`) :**
   - L'écran LCD est soudé sur le boîtier de la passerelle. Si la passerelle est détruite, l'écran est détruit avec elle.
   - En C++ : instanciation par valeur directe (`AfficheurLCD m_afficheur;`) ou `std::unique_ptr`.

---

## 2. Validation de l'Exécution

Les codes sources complets sont disponibles et testés dans :
- **C++ :** [`cpp/`](cpp/) $ightarrow$ Compilez avec `make` puis lancez `./passerelle_iot`.
- **Python :** [`python/`](python/) $ightarrow$ Exécutez avec `python main.py`.

---

## 3. Grille d'Évaluation (Barème /10)
- **Diagramme de classes (/3) :** Notations, visibilités `+`/`-` et flèches exactes (`<|--`, `o--`, `*--`).
- **Implémentation C++ (/4) :** Respect des en-têtes `.hpp` / sources `.cpp`, virtualité et propreté du `Makefile`.
- **Implémentation Python (/3) :** Décorateurs `@property`, typage optionnel, gestion propre des listes.

---

<div align="center">

| ⬅️ Corrigé Précédent | 🏠 Énoncé TP 2 | ➡️ Corrigé Suivant |
| :---: | :---: | :---: |
| [**Corrigé TP 1 (Borne IRVE)**](../tp1-cas-utilisation-borne-irve/CORRIGE_TP1.md) | [**Énoncé Étudiant**](README.md) | [**Corrigé TP 3 (MQTT) ➔**](../tp3-sequence-supervision-mqtt/CORRIGE_TP3.md) |

<br>

[<kbd> &nbsp; ➡️ Passer au Corrigé du TP 3 : Supervision MQTT &nbsp; </kbd>](../tp3-sequence-supervision-mqtt/CORRIGE_TP3.md)

</div>

