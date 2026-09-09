# 📚 Module 06 — Le Diagramme d'Activité

---

## 1. Objectif

Le diagramme d'activité modélise le **déroulement séquentiel et parallèle** d'un algorithme, d'un processus métier ou d'un flux de traitement de données. Il est le successeur moderne et normalisé de l'organigramme technique (*flowchart*).

---

## 2. Nœuds et Notations Clés

```mermaid
flowchart TD
    Start((●)) --> Init[Initialiser liaison UART & capteurs]
    Init --> Mesure[Acquérir les tensions analogiques]
    Mesure --> Test{Tension > Seuil ?}
    
    Test -- Oui --> Alerte[Déclencher alarme sonore & envoyer SMS]
    Test -- Non --> Log[Enregistrer mesure sur carte SD]
    
    Alerte --> Fork[Barre de synchronisation : Fork]
    Log --> Fork
    
    Fork --> T1[Mettre à jour affichage OLED]
    Fork --> T2[Émettre trame radio LoRa]
    
    T1 --> Join[Barre de synchronisation : Join]
    T2 --> Join
    
    Join --> End(((◉)))
```
