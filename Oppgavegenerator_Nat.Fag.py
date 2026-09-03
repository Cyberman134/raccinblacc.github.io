import random

poeng = 0

print("Oppgavegenerator for repitisjon i Nat.fag:")

liste_arv = [
    "DNA", "RNA", "gen", "genetisk variasjon",
    "proteinsyntesen", "genotype", "fenotype",
    "krysningsskjema", "kromosom", "evolusjon"
    "mitose", "meiose", "recessivitet", "metylgrupper",
    "heterozygot",
]

liste_radioaktivitet = [
    "Alfa", "Beta", "Gamma", "gjennomtrengingsevne",
    "stråledose", "aktivitet", "bakgrunnsstråling",
    "ioniserende stråling", "C-14", "halveringstid"
    "medisinsk bruk av radioaktiv stråling",
    "mutasjon",
]

liste_kjemi = [
    "Ionebinding", "NaCl", "Atom", "grunnstoff",
    "kovalent binding", "metallbinding",
    "periodesystemet", "glukose",
    "organisk kjemi", "hydrogenbinding",
    "dipolbinding", "sterke bindinger",
    "svake bindinger",
]

liste_metode = [
    "Definer",
    "Tegn",
    "Forklar praktisk anvendelse av:",
    "Beskriv uten å bruke ordet (alias)",
    "Finn noe interessant på SNL/NDLA/Britannica siden om",

]


def oppgave(tema):
    global poeng

    metode = random.choice(liste_metode)

    if tema == "A":
        begrep = random.choice(liste_arv)

    elif tema == "R":
        begrep = random.choice(liste_radioaktivitet)

    elif tema == "K":
        begrep = random.choice(liste_kjemi)

    elif tema == "T":
        begrep = random.choice(liste_kjemi + liste_metode + liste_arv + liste_radioaktivitet)

    else:
        print("Ugyldig valg.\n")
        return

    print("\nOppgave:")
    print(metode, begrep)

    input("\nTrykk ENTER når du er ferdig...")

    poeng += 1
    print("Du har nå", poeng, "poeng!\n")


def start():
    while True:
        tema = input(
            #'\n'-en vil ikke virke i bl.a. VScode
            "\nSkriv 'A' for Arv,\n'R' for Radioaktivitet,\n'K' for Kjemi, \neller 'T' for en tilfeldig av alle: ").upper()
        oppgave(tema)


start()
