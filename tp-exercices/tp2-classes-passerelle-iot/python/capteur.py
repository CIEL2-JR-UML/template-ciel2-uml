from abc import ABC, abstractmethod

class Capteur(ABC):
    """Classe de base abstraite représentant un capteur générique."""
    def __init__(self, id_capteur: int, label: str):
        self._id = id_capteur
        self._label = label
        self._valeur: float = 0.0

    @property
    def id(self) -> int:
        return self._id

    @property
    def label(self) -> str:
        return self._label

    @property
    def valeur(self) -> float:
        return self._valeur

    @abstractmethod
    def acquerir(self) -> bool:
        """Méthode abstraite à surcharger."""
        pass
