class Stap:
    def __init__(
            self,
            beschrijving: str,
            tip: str | None = None
            ) -> None:
        self.__beschrijving = beschrijving
        self.__tip = tip

    def __str__(self) -> str:
        if self.__tip:
            return f"{self.__beschrijving}\n (Tip: {self.__tip})"
        return self.__beschrijving
