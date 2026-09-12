from ingredient import Ingredient
from stap import Stap

class Recept:
    def __init__(self, naam: str, omschrijving: str):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredienten_lijst: list[Ingredient] = []
        self.__stappen_lijst: list[Stap] = []

    def voeg_ingredient_toe(self, ingredient: Ingredient) -> None:
        self.__ingredienten_lijst.append(ingredient)

    def get_ingredienten(self) -> list[Ingredient]:
        return self.__ingredienten_lijst

    def get_naam(self) -> str:
        return self.__naam

    def voeg_stap_toe(self, stap: Stap) -> None:
        self.__stappen_lijst.append(stap)

    def __str__(self) -> str:
        regels = [
            f"Naam: {self.__naam}",
            f"Omschrijving: {self.__omschrijving}",
            "Ingrediënten:",
        ]
        for ingredient in self.__ingredienten_lijst:
            regels.append(f" - {ingredient}")

        regels.append("")
        regels.append("Stappen:")
        for nummer, stap in enumerate(self.__stappen_lijst, start=1):
            regels.append(f" {nummer}. {stap}")
            
        return "\n".join(regels)
