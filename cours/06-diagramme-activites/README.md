# 📚 Module 06 — Le Diagramme d'Activité

---

## 1. Objectif

Le diagramme d'activité modélise le **déroulement séquentiel et parallèle** d'un algorithme, d'un processus métier ou d'un flux de traitement de données. Il est le successeur moderne et normalisé de l'organigramme technique (*flowchart*).

---

## 2. Nœuds et Notations Clés

![Diagramme d'Activité](../../ressources/images/activite-acquisition.svg)

---

## 3. Exemple avec Couloirs de Responsabilité (Partitions / Swimlanes)

Dans un système communicant complexe, les couloirs permettent d'attribuer chaque action à une entité matérielle ou logicielle distincte :

```plantuml
@startuml
skinparam ActivityBackgroundColor #F0F8FF
skinparam ActivityBorderColor #000080

|#LightYellow|Capteur I2C|
start
:Effectuer conversion CAN;
:Générer impulsion sur broche INTERRUPT;

|#LightCyan|Microcontrôleur (Firmware)|
:Lire registres de données sur bus I2C;
:Calculer la moyenne glissante sur 10 échantillons;

if (Moyenne > Seuil d'Alerte ?) then (oui)
    :Activer sortie relais ventilateur;
    :Générer trame d'alerte JSON;
else (non)
    :Désactiver sortie relais ventilateur;
    :Générer trame de télémétrie standard;
endif

|#LightGreen|Passerelle LoRaWAN / Cloud|
:Transmettre paquet chiffré vers Gateway;
:Stocker mesure en base de données TimeSeries;
stop
@enduml
```

---

## 4. Règles d'Or pour le Diagramme d'Activité
- **Fourche (`fork`) vs Décision :** La fourche lance des actions **simultanées** (parallèles), alors que le losange de décision choisit **une seule branche** selon une condition.
- **Toujours synchroniser :** Tout `fork` doit se refermer par un `join` avant la fin du flux.
