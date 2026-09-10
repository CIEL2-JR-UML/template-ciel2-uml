# 📝 Corrigé TP 3 — Diagramme de Séquence (Télémétrie MQTT)

---

## 1. Analyse des Échanges Réseau

Le protocole MQTT propose différents niveaux de qualité de service (QoS) :
- **QoS 0 (At most once) :** Utilisé pour la télémétrie courante, l'émetteur envoie sans attendre d'accusé de réception (message asynchrone `->>`).
- **QoS 1 (At least once) :** Indispensable pour les alertes critiques, le broker doit obligatoirement renvoyer un paquet `PUBACK` confirmant la réception.

Le schéma PlantUML complet est disponible dans [`sequence_mqtt_corrige.puml`](sequence_mqtt_corrige.puml).

---

## 2. Grille d'Évaluation (Barème /10)

- **Lignes de vie et activations (/2) :** Nommage correct (`instance : Classe`), barres d'activation ouvertes et fermées aux bons moments.
- **Types de flèches (/2) :** Flèches pleines `->` pour les appels de méthodes locaux, flèches pointillées `-->` pour les retours, et flèches ouvertes `->>` pour les trames réseau.
- **Fragment `alt` conditionnel (/3) :** Condition claire entre crochets `[temp >= seuil]`, distinction correcte entre la branche alerte (QoS 1 avec `PUBACK`) et la branche nominale (QoS 0).
- **Complétude du scénario (/3) :** Présence du déclencheur d'horloge, calcul du seuil et phase finale de mise en sommeil.

---

<div align="center">

| ⬅️ Corrigé Précédent | 🏠 Énoncé TP 3 | ➡️ Corrigé Suivant |
| :---: | :---: | :---: |
| [**Corrigé TP 2 (Passerelle IoT)**](../tp2-classes-passerelle-iot/CORRIGE_TP2.md) | [**Énoncé Étudiant**](README.md) | [**Corrigé TP 4 (Contrôle d'Accès) ➔**](../tp4-projet-synthese-controle-acces/CORRIGE_TP4.md) |

<br>

[<kbd> &nbsp; ➡️ Passer au Corrigé du TP 4 : Projet de Synthèse (RFID) &nbsp; </kbd>](../tp4-projet-synthese-controle-acces/CORRIGE_TP4.md)

</div>

