import calendar
"""
Rok przestępny to taki którego numeracja podzielna jest przez 4, jednocześnie niepodzielna przez 100,
lub podzielna przez 400. Muszę go uwzględnić ze względnu na ilośc dni w lutym
"""
def isLapYear(year):
    if year%400 == 0:
        lapYear = True
    elif year%100 == 0:
        lapYear = False
    elif year % 4 == 0:
        lapYear = True
    else:
        lapYear = False

    return lapYear
"""
Obliczając następny dzień od wskazanej daty muszę uwzględnić:
- jeżeli podany dzień jest ostatnim dniem miesiąca to nowy dzień jest pierwszym dniem następnego miesiąca
  , trzeba to uwzględnić w zakeżności od ilości dni w miesiącu (luty(przestępny czy nie, miesiące o 30 dniach i 31 dniach)
- jeżeli podana data to 31 grudnia to nowa data będzie 1 stycznia następnego roku
- reszta dat obliczan jest poprzez dodanie jednego dnia
"""
def nextDay(day, month, year):
    next_day = day + 1
    lapYear = isLapYear(year)

    if month in (1, 3, 5, 7, 9, 11):
        if next_day > 31:
            day = 1
            month += 1
            return day, month, year
        else:
            day += 1
            return day, month, year

    if month in (4, 6, 8, 10):
        if next_day > 30:
            day = 1
            month += 1
            return day, month, year
        else:
            day += 1
            return day, month, year

    if month == 2:
        if lapYear:
            if next_day>29:
                day = 1
                month +=1
                return day, month, year
        elif next_day>28:
                day = 1
                month +=1
                return day, month, year
        else:
            return next_day, (month + 1), year
    if month == 12:
        if day == 31:
            day = 1
            month = 1
            year += 1
            return day, month, year
        else:
            day+=1
            return day, month, year
"""
Obliczając poprzedni dzień muszę uwzględnić:
- jeżeli jest to 1 stycznia to nową datąjest 31 grudnia poprzedniego roku
- jeżeli jest to 1 marca to dniem poprzednim jest 28/29 lutego w zależności czy jest to rok przestępny
- jeżeli jest to 1 dziń pozostałych miesięcy, muszę uwzględnic ile dni miał miesiąc poprzedni
- reszta dat obliczana jest poprzez odjęcie jednego dnia
"""
def previousDay(day, month, year):
    lapYear = isLapYear(year)
    if day == 1:
        if month == 1:
            day = 31
            month = 12
            year -=1
            return day, month, year
        if month == 3:
            if lapYear:
                day = 29
                month -= 1
                return day, month, year
            else:
                day = 28
                month -= 1
                return day, month, year
        if month in (2,4,6,8,9,11,):
            day = 31
            month -= 1
            return day, month, year
        if month in (5,7,10,12):
            day = 30
            month -= 1
            return day, month, year
    else:
        day -= 1
        return day, month, year
"""
Inspirowałem się tym wzorem chcąc obliczyć Wielkanoc dla kalendarza gregoriańskiego: 
https://dateutil.readthedocs.io/en/stable/_modules/dateutil/easter.html
"""
def easter(year):

    # g - Golden year - 1
    # c - Century
    # h - (23 - Epact) mod 30
    # i - Number of days from March 21 to Paschal Full Moon
    # j - Weekday for PFM (0=Sunday, etc)
    # p - Number of days from March 21 to Sunday on or before PFM
    #     (-6 to 28 methods 1 & 3, to 56 for method 2)
    # e - Extra days to add for method 2 (converting Julian
    #     date to Gregorian date)

    g = year % 19
    e = 0
    c = year//100
    h = (c - c//4 - (8*c + 13)//25 + 19*g + 15) % 30
    i = h - (h//28)*(1 - (h//28)*(29//(h + 1))*((21 - g)//11))
    j = (year + year//4 + i + 2 - c + c//4) % 7

    # p can be from -6 to 56 corresponding to dates 22 March to 23 May
    p = i - j + e

    day = 1 + (p + 27 + (p + 6)//40) % 31
    month = 3 + (p + 26)//30
    return day, month , year
"""
Obliczam dzień tygodnia moch urodzin dla podanego roku, korzystając z funkcji calendar
"""
def myBirthdayWeekday(year):
    weekDays=["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"]
    weekday = calendar.weekday(year,7,24)
    return weekDays[weekday]

def menu():
    print("Podaj datę w formacie dzień/miesiąc/rok: ")
    day = int(input("Dzień: "))
    month = int(input("Miesiąc: "))
    year = int(input("Rok: "))

    print("")
    print("Jutro będzie: ", nextDay(day, month, year))
    print("")
    print("Wczoraj był: ", previousDay(day, month, year))
    print("")
    print("W tym roku Wielkanoc wypada na: ", easter(year))
    print("")
    print("W tym roku moje urodziny wypadają w dzień tygodnia: ", myBirthdayWeekday(year))

print(menu())