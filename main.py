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

    gehakt_quiche = Recept("Gehakt quiche met paprika", "Een heerlijke quiche met gehakt, kaas en paprika.")
    gehakt_quiche.voeg_ingredient_toe(Ingredient("rundergehakt", 400, "gram"))
    gehakt_quiche.voeg_ingredient_toe(Ingredient(" rode paprika", 1, "stuk"))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("ui", 1, "stuk"))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("quichedeeg", 2, "vellen"))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("ei", 1, "stuk"))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("knoflook", 2, "teentjes"))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("geraspte kaas", 150, "gram"))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("eieren", 3, "stuk"))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("kookroom", 200, "milliliter"))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("zout", 1, "theelepel"))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("peper", 1, "theelepel"))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("tijm", 1, "theelepel"))

    gehakt_quiche.voeg_stap_toe(Stap("Verwarm de oven voor op 180 graden Celsius."))
    gehakt_quiche.voeg_stap_toe(Stap("Snijd de ui, knoflook en paprika in kleine stukjes."))
    gehakt_quiche.voeg_stap_toe(Stap("Bak het gehakt in een pan totdat het bruin is. Voeg de ui, knoflook en paprika toe en bak dit mee totdat de groenten zacht zijn."))
    gehakt_quiche.voeg_stap_toe(Stap("Bekleed een quichevorm met het quichedeeg en prik gaatjes in de bodem met een vork."))
    gehakt_quiche.voeg_stap_toe(Stap("Klop de eieren los met de kookroom, zout, peper en tijm."))
    gehakt_quiche.voeg_stap_toe(Stap("Voeg het gehaktmengsel toe aan het eimengsel en roer goed door."))
    gehakt_quiche.voeg_stap_toe(Stap("Giet het mengsel in een ingevette quichevorm en bestrooi met geraspte kaas."))
    gehakt_quiche.voeg_stap_toe(Stap("Bak de quiche in de voorverwarmde oven gedurende 30-35 minuten tot hij goudbruin is."))

    recepten.append(gehakt_quiche)

    spaghetti_bolognese = Recept(
        "Spaghetti Bolognese", 
        "Een klassieke Italiaanse spaghetti bolognese met een rijke vlees- en tomatensaus.")
    
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("spaghetti", 400, "gram"))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("rundergehakt", 500, "gram"))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("ui", 1, "stuk"))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("knoflook", 2, "teentjes"))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("tomatenpuree", 2, "eetlepels"))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("gezeefde tomaten", 400, "gram"))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("basilicum", 1, "theelepel"))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("oregano", 1, "theelepel"))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("zout", 1, "theelepel"))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("peper", 1, "theelepel"))

    spaghetti_bolognese.voeg_stap_toe(Stap("Kook de spaghetti volgens de aanwijzingen op de verpakking."))
    spaghetti_bolognese.voeg_stap_toe(Stap("Verhit een beetje olie in een pan en bak het gehakt goudbruin."))
    spaghetti_bolognese.voeg_stap_toe(Stap("Voeg de gesnipperde ui en knoflook toe en bak dit mee."))
    spaghetti_bolognese.voeg_stap_toe(Stap("Voeg de tomatenpuree, gezeefde tomaten, basilicum, oregano, zout en peper toe."))
    spaghetti_bolognese.voeg_stap_toe(Stap("Laat de saus 15-20 minuten sudderen op laag vuur."))
    spaghetti_bolognese.voeg_stap_toe(Stap("Serveer de saus over de spaghetti."))

    recepten.append(spaghetti_bolognese)

if __name__ == "__main__":
    main()
