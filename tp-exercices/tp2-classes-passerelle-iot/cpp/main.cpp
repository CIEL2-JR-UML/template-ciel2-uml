#include "Passerelle.hpp"
#include <iostream>

class CapteurTemperature : public Capteur {
public:
    CapteurTemperature(int id, const std::string& label) : Capteur(id, label) {}
    bool acquerir() override {
        m_valeur = 23.8f;
        return true;
    }
};

class CapteurHumidite : public Capteur {
public:
    CapteurHumidite(int id, const std::string& label) : Capteur(id, label) {}
    bool acquerir() override {
        m_valeur = 58.2f;
        return true;
    }
};

int main() {
    std::cout << "=== DEMO TP 2 : PASSERELLE IOT (BTS CIEL 2) ===" << std::endl;

    Passerelle passerelle("Gateway-SalleServeur", "192.168.10.254");

    CapteurTemperature capteurTemp(101, "Sonde Salle Baie 1");
    CapteurHumidite capteurHum(102, "Humidite Ambiante");

    passerelle.connecterCapteur(&capteurTemp);
    passerelle.connecterCapteur(&capteurHum);

    passerelle.executerCycleMesure();

    return 0;
}
