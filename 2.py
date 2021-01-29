"""

ubezpieczenie emerytalne: 9,76% * kwota brutto

składka rentowa: 6,5% * kwota brutto

składka wypadkowa: 1,67 * kwota brutto

fundusz pracy: 2,45% * kwota brutto

skłądka na Fundusz Gwarantowanych Świadczeń Pracowniczych: 0.10% * kwota brutto

+ pensja praownika brutto

"""

def employerCosts(kwotaBrutto):
    ubezpieczenieEmerytalne = 0.0976 * kwotaBrutto
    skladkaRentowa = 0.065 * kwotaBrutto
    skladkaWypadkowa = 0.0167 * kwotaBrutto
    funduszPracy = 0.0245 * kwotaBrutto
    FGSP = 0.001 * kwotaBrutto

    totalCost = ubezpieczenieEmerytalne + skladkaRentowa + skladkaWypadkowa + funduszPracy + FGSP +  kwotaBrutto
    return totalCost

brutto = float(input("Podaj kowtę prutto pracownika: "))
print("Aby zatrudnić pracownika musisz łącznie wydać ", employerCosts(brutto), "zł.")