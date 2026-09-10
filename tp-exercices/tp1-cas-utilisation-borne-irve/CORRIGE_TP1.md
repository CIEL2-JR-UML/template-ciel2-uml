# 📝 Corrigé TP 1 — Diagramme des Cas d'Utilisation (Borne IRVE)

---

## 1. Analyse des Acteurs

| Acteur | Type | Rôle et justification |
| :--- | :---: | :--- |
| **Conducteur** | Principal (Humain) | Initie les sessions de charge et consulte sa consommation instantanée. |
| **Technicien** | Principal (Humain) | Effectue les opérations de maintenance et diagnostic. **Hérite de Conducteur**. |
| **Serveur Cloud OCPP** | Secondaire (Système tiers) | Supervise le parc, autorise les transactions et peut stopper la borne en urgence. |
| **Compteur MID** | Secondaire (Matériel) | Fournit les index d'énergie certifiés via le bus Modbus RS485. |

> [!NOTE]
> **Règle d'héritage :** `Technicien --|> Conducteur`. Le technicien étant capable de recharger un véhicule de service sans badge additionnel, il hérite des droits d'un conducteur lambda.

---

## 2. Diagramme PlantUML Corrigé

Le schéma complet est disponible dans [`borne_irve_corrige.puml`](borne_irve_corrige.puml).

---

## 3. Fiche Descriptive Détaillée : « Démarrer une session de charge »

| Rubrique | Description |
| :--- | :--- |
| **Identifiant / Nom** | UC-01 : Démarrer une session de charge |
| **Acteur principal** | Conducteur |
| **Acteurs secondaires** | Serveur Cloud OCPP, Contrôleur de verrouillage de prise |
| **Préconditions** | 1. La borne est alimentée et opérationnelle (LED bleue d'attente).<br>2. Le véhicule est raccordé avec le câble Type 2. |
| **Scénario Nominal** | 1. Le conducteur présente son badge RFID devant le lecteur.<br>2. Le système exécute le cas d'utilisation `S'authentifier` (`<<include>>`).<br>3. Le badge est validé localement ou auprès du serveur OCPP.<br>4. Le système verrouille le câble côté borne et côté véhicule.<br>5. Le système active le contacteur de puissance et démarre l'injection.<br>6. Le système affiche la puissance instantanée et le chrono de charge.<br>7. Le système propose au conducteur l'envoi d'un reçu (`<<extend>>`). |
| **Scénarios Alternatifs** | **7a. Envoi de reçu demandé :** Le conducteur saisit son email ou valide son adresse par défaut. Le système planifie l'envoi du récapitulatif (`<<extend>>`). |
| **Scénarios d'Exception** | **2a. Badge refusé :** La borne affiche « Badge non reconnu », émet 3 bips et déverrouille le câble.<br>**4a. Échec verrouillage prise :** Le système coupe le relais par sécurité et affiche le code défaut ERR-12. |
| **Postconditions** | La session de charge est active et l'énergie est comptabilisée en base de données. |

---

## 4. Grille d'Évaluation Type BTS CIEL (Barème /10)

- **Acteurs (/2) :** Identification des acteurs humains et systèmes (+1 pt pour l'héritage Technicien $ightarrow$ Conducteur).
- **Frontière & Cas (/2) :** Frontière délimitée et libellés à l'infinitif.
- **Inclusions (/2) :** `<<include>>` correct vers `S'authentifier` avec le bon sens de flèche.
- **Extensions (/1) :** `<<extend>>` correct depuis `Recevoir un reçu`.
- **Fiche textuelle (/3) :** Scénario nominal clair, exceptions identifiées, pré/postconditions.
