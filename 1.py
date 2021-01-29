"""
Ubezpeiczenie społeczne: -składka emerytalna: 9,76% * kwota brutto
                         -składka rentowa: 1,5% * kwota brutto
                         -składka chorobowa: 2,45% * kwota brutto

Składka zdrowaotna: (kwota brutto - ubezpiecznie społeczne) * 9%

Zaliczka PIT: (ubezpieczenie społeczne + składka zdrowotna)*17% - (kwota wolna od podatku (43,76zł))
            - (ZUS(Ubezpieczenie społeczne * 7,75%)
            Przy czym jeżeli zaliczla PIT jest mniejsza od 0 to wynosi 0zł
"""

def kwotaNetto (kwotaBrutto):

    skladkaEmerytalna = kwotaBrutto * 0.0976
    skladkaRentowa = kwotaBrutto * 0.015
    skladkaChorobowa = kwotaBrutto * 0.0245

    ubezpieczenieSpoleczne = skladkaEmerytalna + skladkaRentowa + skladkaChorobowa


    skladkaZdrowotna = (kwotaBrutto - ubezpieczenieSpoleczne) * 0.09

    ZUS = ubezpieczenieSpoleczne * 0.0775
    zaliczkaPIT= (ubezpieczenieSpoleczne + skladkaZdrowotna) * 0.017 - 43.76 - ZUS
    if zaliczkaPIT < 0:
        zaliczkaPIT = 0

    netto = kwotaBrutto - (ubezpieczenieSpoleczne + skladkaZdrowotna + zaliczkaPIT)

    return netto

print("KALKULATOR PŁACY BRUTTO/NETTO")
kwotaBrutto = float(input("Podaj kwotę brutto: "))

print("Twoja kwota netto wynosi : ", kwotaNetto(kwotaBrutto), "zł")

