#include "Capteur.hpp"

Capteur::Capteur(int id, const std::string& label)
    : m_id(id), m_label(label), m_valeur(0.0f) {}

Capteur::~Capteur() {}

int Capteur::getId() const { return m_id; }
std::string Capteur::getLabel() const { return m_label; }
float Capteur::getValeur() const { return m_valeur; }
