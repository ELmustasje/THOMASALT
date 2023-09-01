from range_key_dict import RangeKeyDict
import pyinputplus


nm = RangeKeyDict(
    {
        (380, 450): "Voilet",
        (451, 485): "Blue",
        (486, 500): "Cyan",
        (501, 565): "Green",
        (566, 590): "Yellow",
        (591, 625): "Orange",
        (626, 750): "Red",
    }
)
THz = RangeKeyDict(
    {
        (670, 790): "Voilet",
        (620, 669): "Blue",
        (600, 619): "Cyan",
        (530, 599): "Green",
        (510, 529): "Yellow",
        (480, 509): "Orange",
        (400, 479): "Red",
    }
)


def nm_THz(input):
    if input == "nm" or input == "THz":
        return input
    else:
        raise Exception(f"må være nm eler THz, det kan ikke være {input}.")


def synlig_lys(valg):
    if valg == "nm":
        verdi = pyinputplus.inputInt("Angi verdi i nm: ")
        if verdi >= 400 and verdi <= 790:
            print(nm[verdi])
        else:
            print(f"{verdi} nm er utenfor det synlige spekteret.")

    if valg == "THz":
        verdi = pyinputplus.inputInt("Angi verdi i THz: ")
        if verdi >= 380 and verdi <= 750:
            print(THz[verdi])
        else:
            print(f"{verdi} THz er utenfor det synlige spekteret.")


valg = pyinputplus.inputCustom(nm_THz, "Angi enhet (nm eller THz): ")
synlig_lys(valg)
