# 🔌 TP 1 — Diagramme des Cas d'Utilisation : Borne de Recharge IRVE

---

## 1. Contexte du Système

La société *VoltCharge* développe une **borne de recharge pour véhicules électriques (IRVE)** connectée, destinée aux parkings d'entreprises et aux copropriétés.

La borne est équipée :
- D'un écran tactile de dialogue.
- D'un lecteur de badge RFID (NFC).
- D'un compteur d'énergie certifié MID (sur bus Modbus RS485).
- D'un contrôleur de charge gérant le verrouillage de la prise de type 2 et le relais de puissance.
- D'un modem 4G/Ethernet communicant avec le serveur de supervision central via le protocole standardisé **OCPP** (*Open Charge Point Protocol*).

---

## 2. Cahier des Charges Fonctionnel

1. **Conducteur de véhicule électrique :**
   - Peut badger pour s'authentifier et déverrouiller la trappe de prise.
   - Peut démarrer une session de recharge.
   - Peut consulter en temps réel sur l'écran la puissance instantanée et l'énergie délivrée.
   - Peut interrompre sa recharge à tout moment en re-badgant.
   - Peut demander l'envoi d'un reçu de recharge par email (optionnel).

2. **Technicien de maintenance :**
   - Doit pouvoir s'authentifier avec un badge « Master ».
   - Peut lancer un autodiagnostic des composants matériels (relais, compteur, capteurs de température).
   - Peut mettre à jour le firmware de la borne via une clé USB ou à distance.
   - Bénéficie de l'accès à toutes les fonctions de consultation de base.

3. **Superviseur distant (Serveur Cloud OCPP) :**
   - Reçoit automatiquement les relevés de consommation de fin de session.
   - Peut ordonner le verrouillage d'urgence de la borne à distance en cas d'anomalie réseau électrique.
   - Synchronise l'horloge de la borne toutes les nuits.

---

## 3. Travail Demandé

1. **Identification des acteurs :**
   - Listez les acteurs humains et les acteurs systèmes / matériels externes.
   - Identifiez d'éventuelles relations de généralisation (héritage) entre acteurs.
2. **Élaboration du Diagramme Use Case :**
   - Complétez le fichier PlantUML fourni [`borne_irve.puml`](borne_irve.puml).
   - Intégrez correctement les relations `<<include>>` (ex: authentification) et `<<extend>>` (ex: envoi de reçu).
3. **Fiche descriptive textuelle :**
   - Rédigez dans un fichier `compte_rendu.md` la fiche détaillée du cas d'utilisation **« Démarrer une session de recharge »** (préconditions, scénario nominal en 6 à 8 étapes, scénarios d'exceptions, postconditions).
