# 📝 Corrigé TP 3 — Machine d'États & Protocole Série Fiabilisé

---

## 1. Explications de la Machine d'États

L'automate garantit la **résilience** de la communication sur un bus industriel bruité (parasites moteurs, CEM) :
- Les réémissions évitent de perdre des données sur des micro-coupures.
- Le seuil `retryCount >= 3` protège le système d'une boucle infinie en cas de capteur débranché.

Les diagrammes complets sont consultables dans :
- [`protocole_uart_corrige.puml`](protocole_uart_corrige.puml)
- [`sequence_protocole_corrige.puml`](sequence_protocole_corrige.puml)

---

## 2. Simulateur Exécutable

Un script Python simulant fidèlement la machine d'états est fourni dans [`simulateur_fsm.py`](simulateur_fsm.py).  
Pour le tester :
```bash
python simulateur_fsm.py
```
