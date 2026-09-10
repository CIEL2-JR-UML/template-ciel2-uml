# 📝 Corrigé TP 4 — Projet de Synthèse (Contrôle d'Accès Sécurisé)

---

## 1. Dossier de Modélisation du Trio Fondamental

Ce dossier rassemble les 3 modèles clés de conception logicielle :
1. **Cas d'Utilisation :** [`controle_acces_uc.puml`](controle_acces_uc.puml)
   - Acteurs `Usager`, `Agent de sécurité` (hérite de l'usager) et `Serveur d'Authentification`.
   - Relation `<<extend>>` conditionnelle vers la saisie du code PIN (uniquement pour les salles sensibles).
2. **Diagramme de Classes :** [`controle_acces_classes.puml`](controle_acces_classes.puml)
   - Composition forte (`*--`) de la gâche, du lecteur RFID et de la signalisation au sein du contrôleur.
   - Agrégation (`o--`) de l'API cliente réseau.
3. **Diagramme de Séquence :**
   - Scénario d'accès autorisé avec double facteur et déverrouillage pendant 5 secondes.

---

## 2. Prototype Logiciel Fonctionnel

Le script Python [`controleur_acces.py`](controleur_acces.py) implémente l'ensemble de la logique métier objet et valide le comportement.
