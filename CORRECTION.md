# 🎓 Guide de Correction Officiel — BTS CIEL 2ème Année

Ce document est réservé à l'équipe pédagogique. Il centralise les corrigés, diagrammes finaux et barèmes types pour l'évaluation des travaux pratiques d'UML (Épreuve **E5** et Projet **E6**).

---

## 📁 Répertoire des Corrigés Détaillés

| Travail Pratique | Dossier | Livrables Corrigés Clés |
| :--- | :--- | :--- |
| **TP 1 : Borne IRVE** | [`tp-exercices/tp1-cas-utilisation-borne-irve/`](tp-exercices/tp1-cas-utilisation-borne-irve/) | [`borne_irve_corrige.puml`](tp-exercices/tp1-cas-utilisation-borne-irve/borne_irve_corrige.puml), [`CORRIGE_TP1.md`](tp-exercices/tp1-cas-utilisation-borne-irve/CORRIGE_TP1.md) |
| **TP 2 : Passerelle IoT** | [`tp-exercices/tp2-classes-passerelle-iot/`](tp-exercices/tp2-classes-passerelle-iot/) | [`passerelle_corrige.puml`](tp-exercices/tp2-classes-passerelle-iot/passerelle_corrige.puml), Codes C++/Python testés |
| **TP 3 : Machine d'États** | [`tp-exercices/tp3-etats-transitions-protocole/`](tp-exercices/tp3-etats-transitions-protocole/) | [`protocole_uart_corrige.puml`](tp-exercices/tp3-etats-transitions-protocole/protocole_uart_corrige.puml), [`simulateur_fsm.py`](tp-exercices/tp3-etats-transitions-protocole/simulateur_fsm.py) |
| **TP 4 : Contrôle d'Accès** | [`tp-exercices/tp4-projet-synthese-controle-acces/`](tp-exercices/tp4-projet-synthese-controle-acces/) | Conception complète (UC, Classes, FSM) + [`controleur_acces.py`](tp-exercices/tp4-projet-synthese-controle-acces/controleur_acces.py) |

---

## 📊 Grille d'Évaluation Globale des Compétences UML (BTS CIEL)

| Compétence Référentiel | Critères d'Excellence | Barème |
| :--- | :--- | :---: |
| **C1 : Analyse du besoin** | Identification correcte des acteurs (primaires/secondaires), frontière du système, inclusions obligatoires vs extensions conditionnelles. | /4 |
| **C2 : Modélisation structurelle** | Encapsulation stricte (`-`/`#`), multiplicités précises, distinction nette entre agrégation (faible) et composition (forte). | /5 |
| **C3 : Modélisation dynamique** | Cohérence chronologique en séquence, complétude des machines d'états (gestion d'erreurs, gardes, timeouts). | /5 |
| **C4 : Implémentation & Test** | Traduction fidèle du diagramme de classes en C++ et Python, propreté du code, séparation header/source. | /6 |
| **TOTAL** | | **/20** |
