# 🎓 Guide de Correction Officiel — BTS CIEL 2ème Année

Ce document est réservé à l'équipe pédagogique. Il centralise les corrigés et grilles d'évaluation pour les **3 diagrammes fondamentaux** de l'UML (Cas d'utilisation, Classes, Séquence).

---

## 📁 Répertoire des Corrigés Détaillés

| Travail Pratique | Diagramme | Livrables Corrigés Clés |
| :--- | :---: | :--- |
| **TP 1 : Borne IRVE** | **Cas d'Utilisation (UC)** | [`borne_irve_corrige.puml`](tp-exercices/tp1-cas-utilisation-borne-irve/borne_irve_corrige.puml), [`CORRIGE_TP1.md`](tp-exercices/tp1-cas-utilisation-borne-irve/CORRIGE_TP1.md) |
| **TP 2 : Passerelle IoT** | **Classes $\rightarrow$ C++ / Python** | [`passerelle_corrige.puml`](tp-exercices/tp2-classes-passerelle-iot/passerelle_corrige.puml), Codes C++/Python testés |
| **TP 3 : Supervision MQTT** | **Diagramme de Séquence** | [`sequence_mqtt_corrige.puml`](tp-exercices/tp3-sequence-supervision-mqtt/sequence_mqtt_corrige.puml), [`CORRIGE_TP3.md`](tp-exercices/tp3-sequence-supervision-mqtt/CORRIGE_TP3.md) |
| **TP 4 : Contrôle d'Accès** | **Synthèse (Trio Complet)** | [`controle_acces_uc.puml`](tp-exercices/tp4-projet-synthese-controle-acces/controle_acces_uc.puml), [`controle_acces_classes.puml`](tp-exercices/tp4-projet-synthese-controle-acces/controle_acces_classes.puml), [`controleur_acces.py`](tp-exercices/tp4-projet-synthese-controle-acces/controleur_acces.py) |

---

## 📊 Grille d'Évaluation Globale des Compétences UML (BTS CIEL)

| Compétence Référentiel | Critères d'Excellence | Barème |
| :--- | :--- | :---: |
| **C1 : Analyse fonctionnelle (Use Case)** | Acteurs corrects, frontière délimitée, distinction stricte `<<include>>` vs `<<extend>>`. | /5 |
| **C2 : Modélisation structurelle (Classes)** | Encapsulation stricte (`-`/`#`), multiplicités, distinction nette entre agrégation (`o--`) et composition (`*--`). | /5 |
| **C3 : Modélisation dynamique (Séquence)** | Cohérence chronologique, précision des flèches (sync, async, retours), fragments `alt`/`loop`. | /5 |
| **C4 : Implémentation & Code** | Traduction rigoureuse des classes en C++ et Python, héritage et collections (`std::vector`). | /5 |
| **TOTAL** | | **/20** |

---

<div align="center">

| ⬅️ Accueil | 📄 Corrigés Rapides | ➡️ Suite |
| :---: | :---: | :---: |
| [**Sommaire Général**](README.md) | [**TP 1**](tp-exercices/tp1-cas-utilisation-borne-irve/CORRIGE_TP1.md) &nbsp;•&nbsp; [**TP 2**](tp-exercices/tp2-classes-passerelle-iot/CORRIGE_TP2.md) &nbsp;•&nbsp; [**TP 3**](tp-exercices/tp3-sequence-supervision-mqtt/CORRIGE_TP3.md) &nbsp;•&nbsp; [**TP 4**](tp-exercices/tp4-projet-synthese-controle-acces/CORRIGE_TP4.md) | [**Mémento UML CIEL**](ressources/cheatsheet-uml-ciel.md) |

<br>

[<kbd> &nbsp; 📝 Consulter le corrigé du TP 1 — Borne IRVE ➔ &nbsp; </kbd>](tp-exercices/tp1-cas-utilisation-borne-irve/CORRIGE_TP1.md)

</div>

