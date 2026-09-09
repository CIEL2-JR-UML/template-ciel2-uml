# 📡 TP 3 — Machine d'États & Diagramme de Séquence : Protocole Série Fiabilisé

---

## 1. Contexte Industriel

Dans un système de télérelève de compteurs d'eau communicants (BTS CIEL ER/IR), une passerelle interroge périodiquement des modules capteurs distants via un bus série RS485 à l'aide d'un protocole demi-duplex (Half-Duplex) fiabilisé par acquittement.

---

## 2. Spécification du Protocole

1. **État Initial : `REPOS`**
   - La passerelle attend l'ordre de relève (`demande_releve`).
2. **État : `ENVOI_REQUETE`**
   - La passerelle transmet une trame de requête d'interrogation (`REQ`).
   - Elle arme un timer de garde de 3 secondes (`timeout3s`).
   - Elle passe à l'état `ATTENTE_REPONSE`.
3. **État : `ATTENTE_REPONSE`**
   - Si une trame réponse valide arrive avant l'échéance : elle envoie un acquittement positif (`ACK`), passe à l'état `TRAITEMENT_DONNEES`, puis revient à `REPOS`.
   - Si la trame reçue est corrompue (erreur CRC) ou si le timer expire : elle incrémente son compteur de réémissions `retryCount`.
     - Si `retryCount < 3` : elle renvoie la requête (transition vers `ENVOI_REQUETE`).
     - Si `retryCount >= 3` : elle passe à l'état `DEFAUT_COMMUNICATION` et déclenche une alarme.

---

## 3. Travail Demandé

1. **Diagramme de Séquence :**
   - Modélisez le scénario nominal (succès au premier essai) et le scénario d'erreur avec répétition sous forme de diagramme de séquence PlantUML.
2. **Diagramme d'États-Transitions :**
   - Complétez le fichier [`protocole_uart.puml`](protocole_uart.puml) pour formaliser l'automate complet avec tous les événements, gardes et actions.
