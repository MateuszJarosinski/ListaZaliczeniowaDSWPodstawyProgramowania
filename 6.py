"""
wzór na przeliczenie Celcjusza na Fahrenheit'a:

    F = C * 1.8 + 32

wzór na przeliczenie Kelwina na Fahrenheit'a:

    F = (K - 273.15)*1.8 + 32

wzór na przelicznie Fahrenheit'a na Kelwina:

    K = (F - 32)/1.8 + 273.15

wzór na przeliczenie Kelwina na Celcjusza

    C = K - 273.15

wzór na przelicznie Celcjusza na Kelwina

    K = C + 273.15

skala Rankine'a:
Jest to skala absolutna, tzn. zero w tej skali oznacza najniższą możliwą temperaturę,
jaką może mieć kryształ doskonały, w którym ustały wszelkie drgania cząsteczek (zero bezwzględne).

    R = 9/5 * K

"""

def CelsiusToFahrenheitConverter(celsius):
    fahrenheit = (celsius * 1.8) + 32
    if fahrenheit <= 32:
        print("Woda zamarza!")
    if fahrenheit >= 212:
        print("Woda wrze!")
    print("Podana przez Ciebie temperatura w stopniach Fahrenheit'a ma wartośc:")
    return fahrenheit

def KelwinToFahrenheitConverter(kelwin):
    fahrenheit = (kelwin - 273.15)*1.8 + 32
    if fahrenheit <= 32:
        print("Woda zamarza!")
    if fahrenheit >= 212:
        print("Woda wrze!")
    print("Podana przez Ciebie temperatura w stopniach Fahrenheit'a ma wartośc:")
    return fahrenheit

def FahrenheitToKelwinConverter(fahrenheit):
    kelwin = (fahrenheit - 32)/1.8 + 273.15
    if kelwin <= 273.15:
        print("Woda zamarza!")
    if kelwin >= 373.15:
        print("Woda wrze!")
    print("Podana przez Ciebie temperatura w stopniach Kelwina ma wartośc:")
    return kelwin

def KelwinToCelsiusConverter(kelwin):
    celsius = kelwin - 273.15
    if celsius <= 0:
        print("Woda zamarza!")
    if celsius >= 100:
        print("Woda wrze!")
    print("Podana przez Ciebie temperatura w stopniach Celcjusza ma wartośc:")
    return celsius

def CelsiusToKelwinConverter(celsius):
    kelwin = celsius + 273.15
    if kelwin <= 273.15:
        print("Woda zamarza!")
    if kelwin >= 373.15:
        print("Woda wrze!")
    print("Podana przez Ciebie temperatura w stopniach Kelwina ma wartośc:")
    return kelwin

def KelwinToRankineConverter(kelwin):
    rankine = 9/5 * kelwin
    if rankine <= 491.4:
        print("Woda zamarza!")
    if rankine >= 671.4:
        print("Woda wrze!")
    print("Podana przez Ciebie temperatura w stopniach Rankine'a ma wartośc:")
    return rankine

def choiceMenu():
    print("PRZELICZNIK TEMPERATURY")
    print("Wybierz jeden z dostępnych przeliczników temperatur:")
    choice = input('''
    Celcjusz na Fahrenheit'a (CF)
    Kelwin na Fahrenheit'a   (KF)
    Fahrenheit na Kelwina    (FK)
    Kelwin na Celcjusza      (KC)
    Celcjusz na Kelwina      (CK)
    Kelwin na Rankine'a      (KR)
    ''')
    if choice.upper() == "CF":
        celsius = float(input("Podaj temperaturę w stopniach Celcjusza"))
        return CelsiusToFahrenheitConverter(celsius)
    if choice.upper() == "KF":
        kelwin = float(input("Podaj temperaturę w stopniach Kelwina"))
        return KelwinToFahrenheitConverter(kelwin)
    if choice.upper() == "FK":
        fahrenheit = float(input("Podaj temperaturę w stopniach Fahrenheit'a"))
        return FahrenheitToKelwinConverter(fahrenheit)
    if choice.upper() == "KC":
        kelwin = float(input("Podaj temperaturę w stopniach Kelwina"))
        return KelwinToCelsiusConverter(kelwin)
    if choice.upper() == "CK":
        celsius = float(input("Podaj temperaturę w stopniach Celcjusza"))
        return CelsiusToKelwinConverter(celsius)
    if choice.upper() == "KR":
        kelwin = float(input("Podaj temperaturę w stopniach Kelwina"))
        return KelwinToRankineConverter(kelwin)

print(choiceMenu())