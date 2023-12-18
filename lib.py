import logging
import json
import os

from constant import DATA_DIR

LOGGER = logging.getLogger()

class Liste(list): #list pour que la class hérite de list et de ces méthode
    def __init__(self, name):
        self.name = name

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Ce n'est pas une string")

        if element in self:
            LOGGER.info(f"l'element {element} est deja dasn la liste")
            return False

        self.append(element)
        return True

    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False

    def afficher(self):
        print(f"Ma liste de {self}")
        for element in self:
            print(f" - {element}")

    def sauvegarder(self):
        chemin = os.path.join(DATA_DIR, f"{self.name}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        with open(chemin, "w") as f:
            json.dump(self, f, indent=4)

        return True

if __name__ == "__main__":
    liste_1 = Liste("courses")
    liste_1.ajouter("pommes")
    liste_1.ajouter("poire")
    liste_1.sauvegarder()

    liste_2 = Liste("films")
    liste_2.ajouter("thor")
    liste_2.ajouter("inception")
    liste_2.sauvegarder()
