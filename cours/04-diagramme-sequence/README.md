# 📚 Module 04 — Le Diagramme de Séquence

---

## 1. Utilité & Définition

Le diagramme de séquence représente la **dimension temporelle et dynamique** du système.
Il met en scène l'échange chronologique de messages entre **instances d'objets** et **acteurs externes** pour réaliser un scénario précis issu d'un cas d'utilisation.

En BTS CIEL, il est indispensable pour modéliser :
- Les **protocoles réseaux** (MQTT, HTTP REST, CoAP, Modbus TCP, WebSockets).
- Les **dialogues inter-processus** et bus matériels (SPI, I2C, UART).
- Les séquences d'initialisation et de traitement d'erreurs.

---

## 2. Éléments Clés d'un Diagramme de Séquence

```mermaid
sequenceDiagram
    autonumber
    actor Tech as Technicien
    participant IHM as IHM Web
    participant Srv as Serveur Backend
    participant BDD as Base SQLite

    Tech->>IHM: Cliquer sur "Générer Rapport"
    activate IHM
    IHM->>Srv: GET /api/rapport?format=json
    activate Srv
    Srv->>BDD: SELECT * FROM mesures WHERE date > J-7
    activate BDD
    BDD-->>Srv: Liste des enregistrements
    deactivate BDD
    
    alt Mesures disponibles
        Srv-->>IHM: 200 OK (données JSON)
        IHM-->>Tech: Affichage du graphique interactif
    else Aucune mesure trouvée
        Srv-->>IHM: 404 Not Found
        IHM-->>Tech: Message "Aucune donnée disponible"
    end

    deactivate Srv
    deactivate IHM
```

### Fragments Combinés Majeurs :
- `alt` : **Alternative :** Exécute un bloc parmi plusieurs selon une condition (`if ... else`).
- `opt` : **Optionnel :** Exécute un bloc si la condition est vraie, rien sinon (`if` sans `else`).
- `loop` : **Boucle :** Répète le bloc tant qu'une condition est vérifiée (`for`, `while`).
- `par` : **Parallélisme :** Exécute plusieurs branches simultanément (threads, multitâche).
