# 🛠️ Tutoriel Rapide : Syntaxe du Code PlantUML

PlantUML utilise l'approche **« Diagram as Code »** : vous décrivez vos diagrammes sous forme de texte simple, et l'outil génère le schéma graphique automatiquement.

---

## 1. La Règle d'Or

Tout bloc ou fichier PlantUML commence impérativement par `@startuml` et se termine par `@enduml`.  
Les commentaires débutent par une simple apostrophe `'`.

```plantuml
@startuml
' Ceci est un commentaire
@enduml
```

---

## 2. Cas d'Utilisation (Use Case)

```plantuml
@startuml
left to right direction

actor "Conducteur" as User
actor "Serveur Cloud" as Cloud <<Système externe>>

rectangle "Système : Borne de Recharge" {
    usecase "Recharger véhicule" as UC_Charge
    usecase "S'authentifier" as UC_Auth
    usecase "Recevoir un reçu" as UC_Recu
}

User --> UC_Charge
UC_Charge ..> UC_Auth : <<include>>
UC_Charge <.. UC_Recu : <<extend>>
UC_Charge --> Cloud
@enduml
```

### Règles clés :
- `actor "Nom" as Alias` : déclare un acteur.
- `usecase "Nom" as Alias` : déclare une bulle de cas d'utilisation.
- `rectangle "Nom" { ... }` : délimite le périmètre du système.
- `A ..> B : <<include>>` : inclusion (B est obligatoire).
- `B <.. A : <<extend>>` : extension (A est optionnel).

### Héritage (Généralisation) en Use Case :
PlantUML utilise la flèche `--|>` (triangle vide) pour matérialiser l'héritage :

```plantuml
' 1. Héritage entre Acteurs (Admin hérite de Utilisateur)
Technicien --|> Utilisateur

' 2. Héritage entre Cas (Spécialisation d'un besoin générique)
(Payer par CB) --|> (Régler la commande)
(Payer par RFID) --|> (Régler la commande)
```


---

## 3. Diagramme de Classes

```plantuml
@startuml
skinparam classAttributeIconSize 0

abstract class Capteur {
    # id : int
    # label : string
    + {abstract} acquerir() : float
    + getLabel() : string
}

class CapteurTemperature {
    - coefficient : float
    + acquerir() : float
}

class Passerelle {
    - nom : string
    + ajouterCapteur(c: Capteur*) : void
}

class EcranOLED {
    + afficher(texte: string) : void
}

Capteur <|-- CapteurTemperature : Héritage
Passerelle o-- "0..*" Capteur    : Agrégation (Faible)
Passerelle *-- "1" EcranOLED    : Composition (Forte)
@enduml
```

### Symboles de Visibilité :
- `-` : **Privé** (`private`)
- `+` : **Public** (`public`)
- `#` : **Protégé** (`protected`)

### Flèches de Relations :
- `<|--` : **Héritage** (triangle vide)
- `o--` : **Agrégation** (losange vide)
- `*--` : **Composition** (losange plein noir)
- `-->` : **Association navigable**

---

## 4. Diagramme de Séquence

```plantuml
@startuml
autonumber

actor "Client" as user
participant "IHM Web" as ihm
participant "Serveur" as srv
database "BaseDeDonnées" as db

user -> ihm : Cliquer sur "Connexion"
activate ihm

ihm -> srv : POST /login
activate srv

srv -> db : SELECT * FROM users
activate db
db --> srv : Données utilisateur
deactivate db

alt Identifiants valides
    srv --> ihm : 200 OK
    ihm --> user : Accès accordé
else Identifiants invalides
    srv --> ihm : 401 Unauthorized
    ihm --> user : Erreur de connexion
end

deactivate srv
deactivate ihm
@enduml
```

### Règles clés :
- `autonumber` : numérote automatiquement chaque échange.
- `->` : appel de méthode synchrone (flèche pleine).
- `-->` : valeur de retour (flèche pointillée).
- `activate / deactivate` : barres d'exécution.
- `alt ... else ... end` : branchement conditionnel `if ... else`.

---

## 5. Diagramme d'États-Transitions

```plantuml
@startuml
[*] --> Veille : Mise sous tension

state Veille {
    entry / eteindreLEDs()
}

state Connecte {
    do / emettreTrames()
}

Veille --> Connecte : BoutonAppuye / allumerLED()
Connecte --> Veille : after(10s) / timeout()
Connecte --> [*] : CommandeArret
@enduml
```

### Syntaxe d'une transition :
$$\text{EtatSource} \rightarrow \text{EtatCible} : \text{Événement } [\text{Garde}] \; / \; \text{Action}$$

- `entry /` : action d'entrée.
- `exit /` : action de sortie.
- `do /` : traitement en continu.
- `[*]` : état initial ou final.
