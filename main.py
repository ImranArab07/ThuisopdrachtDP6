from ingredient import Ingredient
from recept import Recept 
from stap import Stap



def main():
    recepten = []

    kip_kerrie = Recept(
        "Kip Kerrie", 
        "Een romige kip-kerrie met broccoli, sperziebonen en rijst."
     )
    kip_kerrie.voeg_ingredient_toe(Ingredient("kipfilet", 300, "gram"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("basmatirijst", 200, "gram"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("sperziebonen", 150, "gram"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("broccoli", 200, "gram"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("kokosmelk", 100, "milliliter"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("ui", 1, "stuk"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("knoflook", 2, "teentjes"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("kerriepoeder", 1, "eetlepel"))

    

if __name__ == "__main__":
    main()
