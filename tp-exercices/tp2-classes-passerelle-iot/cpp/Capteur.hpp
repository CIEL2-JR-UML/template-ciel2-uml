#pragma once
#include <string>
#include <iostream>

class Capteur {
protected:
    int m_id;
    std::string m_label;
    float m_valeur;

public:
    Capteur(int id, const std::string& label);
    virtual ~Capteur();

    virtual bool acquerir() = 0; // Méthode virtuelle pure (classe abstraite)

    int getId() const;
    std::string getLabel() const;
    float getValeur() const;
};
