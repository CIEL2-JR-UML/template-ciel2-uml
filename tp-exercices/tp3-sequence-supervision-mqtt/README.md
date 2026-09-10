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

## 3. Travail Demandé

1. Complétez le fichier PlantUML [`sequence_mqtt.puml`](sequence_mqtt.puml).
2. Utilisez les éléments normalisés :
   - Numérotation automatique (`autonumber`).
   - Messages synchrones (`->`) et asynchrones (`->>`).
   - Réponses en pointillés (`-->`).
   - Barre d'activation (`activate` / `deactivate`).
   - Fragment conditionnel `alt ... else ... end`.
3. Visualisez le schéma avec le raccourci **`Alt + D`**.
