class Ingredient:
    def __init__(
            self,
            naam: str,
            hoeveelheid: float,
            eenheid: str,
            kcal: int
            ) -> None:
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__kcal = kcal
        self.__plantaardig_alternatief = None  # Optioneel plantaardig alternatief

    def set_hoeveelheid(self, hoeveelheid: float) -> None:
        self.__hoeveelheid = hoeveelheid

    def get_hoeveelheid(self) -> float:
        return self.__hoeveelheid

    def get_kcal(self) -> int:
        return self.__kcal

    def set_plantaardig_alternatief(
            self, 
            alternatief: "Ingredient"
            ) -> None:
        self.__plantaardig_alternatief = alternatief

    def get_ingredient(self, plantaardig: bool) -> "Ingredient":
        if plantaardig and self.__plantaardig_alternatief is not None:
            return self.__plantaardig_alternatief
        
        return self

    def __str__(self) -> str:
        return f"{self.__hoeveelheid:g} {self.__eenheid} {self.__naam}"