from ingredient import Ingredient
from recept import Recept 
from stap import Stap



def maak_recepten():
    recepten = []

    kip_kerrie = Recept(
        "Kip Kerrie", 
        "Een romige kip-kerrie met broccoli, sperziebonen en rijst."
     )
    kipfilet = Ingredient("kipfilet", 200, "gram", 330)
    kipfilet.set_plantaardig_alternatief(Ingredient("tofu", 200, "gram", 280))
    kip_kerrie.voeg_ingredient_toe(kipfilet)

    kip_kerrie.voeg_ingredient_toe(Ingredient("basmatirijst", 100, "gram", 350))
    kip_kerrie.voeg_ingredient_toe(Ingredient("sperziebonen", 150, "gram", 50))
    kip_kerrie.voeg_ingredient_toe(Ingredient("broccoli", 200, "gram", 70))
    kip_kerrie.voeg_ingredient_toe(Ingredient("kokosmelk", 100, "milliliter", 150))
    kip_kerrie.voeg_ingredient_toe(Ingredient("ui", 1, "stuk", 40))
    kip_kerrie.voeg_ingredient_toe(Ingredient("knoflook", 2, "teentjes", 10))
    kip_kerrie.voeg_ingredient_toe(Ingredient("kerriepoeder", 1, "eetlepel", 20))

    kip_kerrie.voeg_stap_toe(Stap("Kook de rijst en zet een pan water met een snuf zout op het vuur voor de sperziebonen.", "Zorg ervoor dat je de rijst op tijd begint te koken."))
    kip_kerrie.voeg_stap_toe(Stap("Snijd de kip in kleine blokjes, snipper het uitje, snijd de knoflook fijn en snijd de kontjes van de sperziebonen en snijd de broccoli (was de sperziebonen en broccoli ook even)."))
    kip_kerrie.voeg_stap_toe(Stap("Bak de kip in een beetje olie goudbruin. Voeg de ui en knoflook toe en bak dit even mee. Voeg de kerriepoeder toe en bak dit kort mee."))
    kip_kerrie.voeg_stap_toe(Stap("Voeg de kokosmelk toe en laat het geheel 10 minuten zachtjes koken."))
    kip_kerrie.voeg_stap_toe(Stap("Kook ondertussen de sperziebonen in 5 minuten beetgaar en kook de broccoli in 4 minuten beetgaar."))
    kip_kerrie.voeg_stap_toe(Stap("Serveer de kip-kerrie met de rijst, sperziebonen en broccoli."))
    recepten.append(kip_kerrie)

    gehakt_quiche = Recept("Gehakt quiche met paprika", "Een heerlijke quiche met gehakt, kaas en paprika.")

    quiche_gehakt = Ingredient("rundergehakt", 100, "gram", 250)
    quiche_gehakt.set_plantaardig_alternatief(
        Ingredient("plantaardig gehakt", 100, "gram", 180)
        )
    gehakt_quiche.voeg_ingredient_toe(quiche_gehakt)


    gehakt_quiche.voeg_ingredient_toe(Ingredient("rode paprika", 0.5, "stuk", 25))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("ui", 0.5, "stuk", 20))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("quichedeeg", 1, "vel", 200))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("knoflook", 1, "teentje", 5))

    kaas = Ingredient("geraspte kaas", 30, "gram", 90)
    kaas.set_plantaardig_alternatief(
        Ingredient("plantaardige kaas", 30, "gram", 70)
        )
    gehakt_quiche.voeg_ingredient_toe(kaas)



    ei = Ingredient("ei", 1, "stuk", 70)
    ei.set_plantaardig_alternatief(
        Ingredient("aquafaba", 45, "milliliter", 8)
    )
    gehakt_quiche.voeg_ingredient_toe(ei)

    kookroom = Ingredient("kookroom", 50, "milliliter", 100)
    kookroom.set_plantaardig_alternatief(
        Ingredient("plantaardige kookroom", 50, "milliliter", 80)
    )
    gehakt_quiche.voeg_ingredient_toe(kookroom)

    gehakt_quiche.voeg_ingredient_toe(Ingredient("zout", 0.25, "theelepel", 0))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("peper", 0.25, "theelepel", 2))
    gehakt_quiche.voeg_ingredient_toe(Ingredient("tijm", 0.25, "theelepel", 5))

    gehakt_quiche.voeg_stap_toe(Stap("Verwarm de oven voor op 180 graden Celsius.", "Zorg ervoor dat de oven goed voorverwarmd is."))
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
    
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("spaghetti", 100, "gram", 300))

    bolognese_gehakt = Ingredient("gehakt", 150, "gram", 400)
    bolognese_gehakt.set_plantaardig_alternatief(
        Ingredient("plantaardig gehakt", 150, "gram", 300)
    )
    spaghetti_bolognese.voeg_ingredient_toe(bolognese_gehakt)

    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("ui", 0.5, "stuk", 20))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("knoflook", 1, "teentje", 5))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("tomatenpuree", 1, "eetlepel", 25))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("gezeefde tomaten", 200, "gram", 70))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("basilicum", 0.5, "theelepel", 2))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("oregano", 0.5, "theelepel", 2))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("zout", 0.25, "theelepel", 0))
    spaghetti_bolognese.voeg_ingredient_toe(Ingredient("peper", 0.25, "theelepel", 2))

    spaghetti_bolognese.voeg_stap_toe(Stap("Kook de spaghetti volgens de aanwijzingen op de verpakking."))
    spaghetti_bolognese.voeg_stap_toe(Stap("Verhit een beetje olie in een pan en bak het gehakt goudbruin."))
    spaghetti_bolognese.voeg_stap_toe(Stap("Voeg de gesnipperde ui en knoflook toe en bak dit mee."))
    spaghetti_bolognese.voeg_stap_toe(Stap("Voeg de tomatenpuree, gezeefde tomaten, basilicum, oregano, zout en peper toe."))
    spaghetti_bolognese.voeg_stap_toe(Stap("Laat de saus 15-20 minuten sudderen op laag vuur.", "Roer af en toe door de saus."))
    spaghetti_bolognese.voeg_stap_toe(Stap("Serveer de saus over de spaghetti."))

    recepten.append(spaghetti_bolognese)

    return recepten

def toon_recepten(recepten):
    print("Receptenboek")

    for nummer, recept in enumerate(recepten, start=1):
        print(f"{nummer}. {recept.get_naam()}")

def kies_recept(recepten):
    while True:
        keuze = input(
            "Kies een receptnummer (of 'q' om te stoppen): "
            ).strip()

        if keuze.lower() == 'q':
            return None

        if keuze.isdigit():
            receptnummer = int(keuze)

            if 1 <= receptnummer <= len(recepten):
                return recepten[receptnummer - 1] # omdat pythonlijsten beginnen bij 0
            
            print("Recept niet gevonden.")
            print()
            toon_recepten(recepten)

def vraag_aantal_personen():
    while True:
        invoer = input(
            "Voor hoeveel personen wil je het recept aanpassen? "
        ).strip()

        if invoer.isdigit() and int(invoer) > 0:
            return int(invoer)

        print("Ongeldige invoer. Voer een getal in.")

def vraag_plantaardig():
    while True:
        keuze = input(
            "Wil je een plantaardig alternatief gebruiken? (ja/nee) "
        ).strip().lower()

        if keuze == "ja":
            return True
        
        if keuze == "nee":
            return False

        print("Ongeldige invoer. Voer 'ja' of 'nee' in.")

def main():

    recepten = maak_recepten()
    toon_recepten(recepten)
    gekozen_recept = kies_recept(recepten)

    if gekozen_recept is None:
        return

    aantal_personen = vraag_aantal_personen()
    gekozen_recept.set_aantal_personen(aantal_personen)

    plantaardig = vraag_plantaardig()

    print()
    print(
        gekozen_recept.get_plantaardig_recept(plantaardig)
    )

if __name__ == "__main__":
    main()
