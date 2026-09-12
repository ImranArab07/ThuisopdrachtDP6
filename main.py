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

    kip_kerrie.voeg_stap_toe(Stap("Kook de rijst en zet een pan water met een snuf zout op het vuur voor de sperziebonen."))
    kip_kerrie.voeg_stap_toe(Stap("Snijd de kip in kleine blokjes, snipper het uitje, snijd de knoflook fijn en snijd de kontjes van de sperziebonen en snijd de broccoli (was de sperziebonen en broccoli ook even)."))
    kip_kerrie.voeg_stap_toe(Stap("Bak de kip in een beetje olie goudbruin. Voeg de ui en knoflook toe en bak dit even mee. Voeg de kerriepoeder toe en bak dit kort mee."))
    kip_kerrie.voeg_stap_toe(Stap("Voeg de kokosmelk toe en laat het geheel 10 minuten zachtjes koken."))
    kip_kerrie.voeg_stap_toe(Stap("Kook ondertussen de sperziebonen in 5 minuten beetgaar en kook de broccoli in 4 minuten beetgaar."))
    kip_kerrie.voeg_stap_toe(Stap("Serveer de kip-kerrie met de rijst, sperziebonen en broccoli."))
    recepten.append(kip_kerrie)

    gehakt_quiche = Recept("Gehakt quiche met paprika", "Een heerlijke quiche met gehakt en paprika.")
    recepten.append(gehakt_quiche)

if __name__ == "__main__":
    main()
