import os

preis_erwachsene = 5.0
preis_jugendliche = 3.5
preis_kinder = 2.5
preis_premium = 3.0
preis_basis = 4.0
 

def sekt(preis):
    print(" ### Wenn sie für 0,75€ Aufpreis ein Glas Sekt wollen, geben sie 'y' ein ### ")
    antwort = input()
    if antwort == "y":
        print(" Preis: ", preis+0.75 , " Euro ")
        return preis+0.75
    return preis

def halbtag(preis):
    preistag = preis
    print(" ### Wollen sie für ein halben Tag oder ganzen Tag im Museum bleiben ###")
    print(" ### Wenn sie den ganzen Tag bleiben wollen, geben sie 'y' ein ###")
    print(" ### Wenn sie den halben Tag bleiben wollen, drücken Sie eine beliebige andere Taste. ### ")
    antwort = input()
    if antwort == "y":
        print(" Preis: ", preis*2 , " Euro ")
        return preis*2
    else: 
        print(" Preis: ", preis, " Euro ")
        return preis


def function():
    preis_person = 0
    print(" Hallo, geben Sie bitte Ihr Alter ein.")
    alter_gast = int(input())
    if alter_gast < 14:
        print(" ### Eintritt Kinder ### ")
        print(" Preis: ", preis_kinder, " Euro ")
        preis_person = preis_kinder
    elif alter_gast < 18:
        print(" ### Eintritt Jugendliche ### ")
        print(" Preis: ", preis_jugendliche, " Euro ")
        preis_person = preis_jugendliche
    else:
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Wenn Sie Premium-Mitglied sind, geben Sie 'p' ein.")
        print(" Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein.")
        print(" Wenn Sie kein Mitglied sind, drücken Sie eine beliebige andere Taste. ")
        antwort_rabatt = input();
        if antwort_rabatt == "p":
            print(" ### Eintritt Premium-Mitglied ### ")
            preis_person = halbtag(preis_premium)
            preis_person = sekt(preis_person)
        elif antwort_rabatt == "b":
            print(" ### Eintritt Basis-Mitglied ### ")
            preis_person = halbtag(preis_basis)
        else:
            print(" ### Eintritt Erwachsene (voller Preis) ### ")
            preis_person = halbtag(preis_erwachsene)
    print(" ### Wollen sie noch ein Tarif ### ")
    print(" ### Wenn sie noch ein Tarifbuchen wollen, geben sie 'y' ein ### ")
    print(" ### Wenn sie nicht noch ein Tarifbuchen wollen, drücken Sie eine beliebige andere Taste. ### ")
    return preis_person


preis_ges = 0

print(" ### Tarifauskunftsrechner Museum XXX ### ")
preis_ges += function()
antwort = input();

while antwort == "y":
    preis_ges += function()
    antwort = input();

os.system('cls')

print(" ### Wenn sie den gesammt Preis sehen wollen, geben sie 'y' ein ### ")
antwort = input();
if antwort == "y":
    print(" ### Gesammtpreis beträgt:", preis_ges)

print("### Viel Spaß ###")
