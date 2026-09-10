# 📡 TP 3 — Diagramme de Séquence : Dialogue Réseau & MQTT

---

## 1. Contexte du Système

Une station de surveillance environnementale pour salle serveurs (BTS CIEL IR/ER) mesure la température et l'humidité ambiantes. Dès qu'un seuil critique est franchi, elle doit émettre une alerte instantanée vers un superviseur central à l'aide du protocole standardisé **MQTT** (*Message Queuing Telemetry Transport*).

---

## 2. Spécification des Échanges Chronologiques

Le système met en scène 4 participants :
1. `Horloge` (Timer d'échantillonnage de 10 secondes)
2. `ControleurPrincipal` (Application centrale)
3. `CapteurTemp` (Sonde matérielle sur bus I2C)
4. `ClientMQTT` (Module réseau embarqué)
5. `BrokerMQTT` (Serveur distant / Cloud)

### Scénario à modéliser :
1. L'horloge déclenche l'événement `tick10s()`.
2. Le `ControleurPrincipal` demande l'acquisition à `CapteurTemp` via `lireTemperature()`.
3. Le capteur retourne la température mesurée (ex : 28.5 °C).
4. Le contrôleur évalue la valeur par rapport au seuil critique (25.0 °C).
5. **Alternative (`alt`) :**
   - **Si `temperature >= seuil` :**
     - Le contrôleur ordonne au client MQTT de publier une alerte prioritaire (`publierAlerte()`).
     - Le client transmet un paquet `MQTT PUBLISH` (QoS 1, Topic: `"alerte/critique"`).
     - Le broker distant accuse réception avec un paquet `PUBACK`.
     - Le client confirme la réussite de l'envoi au contrôleur.
   - **Sinon (Cas nominal) :**
     - Le contrôleur demande une publication périodique standard sans accusé de réception (`publierTélémétrie()`, QoS 0).
6. Le contrôleur met le microcontrôleur en veille légère (`miseEnSommeil()`).

---

## 3. Travail Demandé (Exercice Guidé à Trous)

Le fichier [`sequence_mqtt.puml`](sequence_mqtt.puml) contient déjà l'architecture générale et la branche critique d'alerte. Vous n'avez que **3 balises `TODO` (environ 4 lignes)** à ajouter :

1. **TODO 1 : Retour de mesure en pointillés (`-->`)**
   - Écrivez la réponse de la sonde renvoyant sa température au contrôleur (`Sonde --> Ctrl : float (ex: 28.5)`).
2. **TODO 2 : Message réseau asynchrone QoS 0 (`->>`)**
   - Dans la branche `else`, complétez l'envoi de la trame vers le broker avec une flèche ouverte sans attente d'accusé (`MQTT ->> Broker : PUBLISH (QoS=0, Topic="telemetrie/temp")`).
3. **TODO 3 : Mise en veille finale**
   - Appelez la méthode interne `Ctrl -> Ctrl : miseEnSommeil()` puis désactivez la ligne de vie avec `deactivate Ctrl`.

*(💡 Visualisez instantanément votre schéma dans VS Code avec **`Alt + D`**)*.


---

<div align="center">

| ⬅️ Précédent | 🏠 Accueil | ➡️ Suite Logique |
| :--- | :---: | ---: |
| [**Cours 04 : Diagramme de Séquence**](../../cours/04-diagramme-sequence/) | [**Sommaire des TP**](../README.md) | [**Chapitre 05 : Passage UML vers Code ➔**](../../cours/05-passage-uml-vers-code/) |

<br>

[<kbd> &nbsp; ➡️ Passer à l'étape suivante : Chapitre 05 — Passage UML vers Code &nbsp; </kbd>](../../cours/05-passage-uml-vers-code/)

</div>

