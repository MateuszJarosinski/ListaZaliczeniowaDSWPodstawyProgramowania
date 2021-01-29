import calendar

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

# https://dateutil.readthedocs.io/en/stable/_modules/dateutil/easter.html

def easter(year): #method=3 - kalendarz gregoriański

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