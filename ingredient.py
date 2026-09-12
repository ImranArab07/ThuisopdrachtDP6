class Ingredient:
    def __init__(self, naam: str, hoeveelheid: float, eenheid: str):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__plantaardig_alternatief = None  # Optioneel plantaardig alternatief

    def __str__(self):
        return f"{self.__hoeveelheid} {self.__eenheid} {self.__naam}"

    def set_plantaardig_alternatief(
            self, 
            alternatief: "Ingredient"
            ) -> None:
        self.__plantaardig_alternatief = alternatief

    def get_ingredient(self, plantaardig: bool) -> "Ingredient":
        if plantaardig and self.__plantaardig_alternatief is not None:
            return self.__plantaardig_alternatief
        
        return self

    def __str__(self):
        return f"{self.__hoeveelheid} {self.__eenheid} {self.__naam}"