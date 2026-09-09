#pragma once
#include <vector>
#include <string>
#include "Capteur.hpp"

class AfficheurLCD {
public:
    void afficher(const std::string& l1, const std::string& l2);
};

class Passerelle {
private:
    std::string m_nom;
    std::string m_ip;
    std::vector<Capteur*> m_capteurs; // Agrégation
    AfficheurLCD m_afficheur;         // Composition (objet membre)

public:
    Passerelle(const std::string& nom, const std::string& ip);
    ~Passerelle();

    void connecterCapteur(Capteur* capteur);
    void executerCycleMesure();
};
