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

## 3. Travail Demandé (Exercice Guidé à Trous)

Le fichier [`borne_irve.puml`](borne_irve.puml) est déjà pré-rempli à 80%. Vous n'avez pas besoin de tout redessiner !

### Étape 1 : Compléter le diagramme PlantUML (3 lignes à écrire)
Ouvrez [`borne_irve.puml`](borne_irve.puml) et complétez les 3 balises `TODO` indiquées :
1. **TODO 1 :** Ajouter la relation d'héritage entre `Tech` et `User`.
2. **TODO 2 :** Ajouter l'inclusion obligatoire `<<include>>` entre `UC_Charge` et `UC_Auth`.
3. **TODO 3 :** Ajouter l'extension optionnelle `<<extend>>` entre `UC_Charge` et `UC_Recu`.

*(💡 Appuyez sur **`Alt + D`** dans VS Code pour voir immédiatement le schéma se mettre à jour !)*

### Étape 2 : Compléter la fiche textuelle à trous
Dans un fichier `compte_rendu.md`, recopiez et complétez les **3 mentions `[À COMPLÉTER]`** du tableau suivant :

| Rubrique | Contenu |
| :--- | :--- |
| **Titre du cas :** | Démarrer une session de recharge |
| **Acteur principal :** | Conducteur |
| **Acteurs secondaires :** | Serveur Cloud OCPP, Verrou de prise |
| **Cas inclus obligatoire :** | **`[À COMPLÉTER 1]`** *(Indice : que doit faire l'usager avec son badge avant de charger ?)* |
| **Scénario nominal :** | 1. Le conducteur branche le câble Type 2 sur la borne.<br>2. Le système demande l'authentification.<br>3. Le conducteur passe son badge RFID.<br>4. Le système valide les droits et verrouille le connecteur.<br>5. Le relais de puissance s'enclenche et le courant est injecté.<br>6. Le système affiche la puissance instantanée. |
| **Scénario d'exception :** | **`[À COMPLÉTER 2]`** *(Indice : que se passe-t-il si le badge est refusé ou non reconnu ?)* |
| **Extension facultative :** | **`[À COMPLÉTER 3]`** *(Indice : quel reçu facultatif peut être demandé ?)* |


---

<div align="center">

| ⬅️ Précédent | 🏠 Accueil | ➡️ Suite Logique |
| :--- | :---: | ---: |
| [**Cours 02 : Cas d'Utilisation**](../../cours/02-diagramme-cas-utilisation-uc/) | [**Sommaire des TP**](../README.md) | [**Chapitre 03 : Diagramme de Classes ➔**](../../cours/03-diagramme-classes/) |

<br>

[<kbd> &nbsp; ➡️ Passer à l'étape suivante : Chapitre 03 — Diagramme de Classes &nbsp; </kbd>](../../cours/03-diagramme-classes/)

</div>

