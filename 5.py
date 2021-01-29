primaryCurrency = input("Jaką walutę chcesz przeliczyć? (USD, THB, BTC, BTN. MRO, ETH, SASIN) ")
finalCurrency = input("Na jaką walutę chcesz przeliczyć? ")
value = float(input("Podaj wartość:"))

def currencyCalculator(primaryCurrency, finalCurrency, value):
    if primaryCurrency.upper()=="USD":
        converter = {
            "THB": 0.033,
            "BTC": 32424.8,
            "BTN": 0.014,
            "MRO": 0.027,
            "ETH": 1326.69,
            "SASIN": 259259259.259
        }
        if finalCurrency.upper() in converter:                         #do przelicznia walut używam tego samego słownika,
            finalValue = value / converter[finalCurrency.upper()]      #ponieważ wystarczy zamienić znak mnożenia na dzielenie
            return finalValue                                          #przy czym przelicznia wciąż będą poprawne
    elif primaryCurrency != "USD":
        converter = {
            "THB": 0.033,
            "BTC": 32424.80,
            "BTN": 0.014,
            "MRO": 0.027,
            "ETH": 1326.69,
            "SASIN": 259259259.259
        }
        if primaryCurrency.upper() in converter:
            finalValue = value * converter[primaryCurrency.upper()]
            return finalValue
    else:
        print("Kalkulator nie obsługuje takiergo przelicznika :c")

print(currencyCalculator(primaryCurrency, finalCurrency, value))


