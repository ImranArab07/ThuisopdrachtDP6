from ingredient import Ingredient
from stap import Stap

class Recept:
    def __init__(self, naam: str, omschrijving: str) -> None:
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredienten_lijst: list[Ingredient] = []
        self.__stappen_lijst: list[Stap] = []
        self.__aantal_personen = 1

    def voeg_ingredient_toe(self, ingredient: Ingredient) -> None:
        self.__ingredienten_lijst.append(ingredient)

    def get_ingredienten(self) -> list[Ingredient]:
        return self.__ingredienten_lijst

    def get_naam(self) -> str:
        return self.__naam

    def voeg_stap_toe(self, stap: Stap) -> None:
        self.__stappen_lijst.append(stap)
    
    def set_aantal_personen(self, personen: int) -> None:
        if personen < 1:
            raise ValueError("Aantal personen moet minimaal 1 zijn.")
        
        factor = personen / self.__aantal_personen

        for ingredient in self.__ingredienten_lijst:
            nieuwe_hoeveelheid = ingredient.get_hoeveelheid() * factor
            ingredient.set_hoeveelheid(nieuwe_hoeveelheid)

            alternatief = ingredient.get_ingredient(plantaardig=True)

            if alternatief is not ingredient:
                nieuwe_hoeveelheid = alternatief.get_hoeveelheid() * factor
                alternatief.set_hoeveelheid(nieuwe_hoeveelheid)

        self.__aantal_personen = personen

    def get_aantal_personen(self) -> int:
        return self.__aantal_personen
    
    def get_totaal_kcal(self, plantaardig: bool) -> int:
        totaal_per_persoon = 0
        for ingredient in self.__ingredienten_lijst:
            gekozen_ingredient = ingredient.get_ingredient(plantaardig)
            totaal_per_persoon += gekozen_ingredient.get_kcal()

        return totaal_per_persoon * self.__aantal_personen

    def get_plantaardig_recept(self, plantaardig: bool) -> str:
        regels = [
            f"Naam: {self.__naam}",
            f"Omschrijving: {self.__omschrijving}",
            f"Aantal personen: {self.__aantal_personen}",
            "Ingrediënten:",
        ]

        for ingredient in self.__ingredienten_lijst:
            gekozen_ingredient = ingredient.get_ingredient(plantaardig)
            regels.append(f" - {gekozen_ingredient}")

        regels.append("")
        regels.append(f"Totaal aantal kcal: {self.get_totaal_kcal(plantaardig)}")

        return "\n".join(regels)

    def __str__(self) -> str:
        return self.get_plantaardig_recept(False)
