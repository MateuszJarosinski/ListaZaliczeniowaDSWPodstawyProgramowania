# nie zorientowałem się że zadanie 3 mało być zrbione z plikiem zewnętrznym a szkoda mi było tego to zostawiłęm ;)

import random

def scoreCalculator(score):
    if score <= 2:
        return "Uzyskałeś/aś ocenę niedostateczną :c"
    elif score <=5:
        return "Uzyskałeś/aś ocenę dopuszczającą"
    elif score <=7:
        return "Uzyskałeś/aś ocenę dostateczną"
    elif score <=8:
        return "Uzyskałeś/aś ocenę dobrą"
    elif score <=9:
        return "Uzyskałeś/aś ocenę bardzo dobrą"
    else:
        return "Uzyskałeś/aś ocenę celującą! "


def questionGenerator():

    questionList = []
    questionList.append(["HTML to język programowania.", "NIE"])                                     # w każdej z list element z indeksem 0 będzie pytaniem
    questionList.append(["JavaScript to zamienna nazwa dla Java.", "NIE"])                           # a element z indeksem 1 będzie odpowiedzią tak lub nie
    questionList.append(["Adobe PhotoShop to nazwa sklepu w którym sprzedaje się zdjęcia.", "NIE"])
    questionList.append(["Python jest językiem intepretowanym", "TAK"])
    questionList.append(["Wyszukiwarka Google służy do wyszukiwania zdjęć z kotami", "TAK"])
    questionList.append(["Przykładem pętli w Pythonie jest 'while' ", "TAK"])
    questionList.append(["Steve Jobs jest założycielem Apple", "TAK"])
    questionList.append(["Megabajt to więcej niż Gigabajt", "NIE"])
    questionList.append(["GPU to procesor graficzny", "TAK"])
    questionList.append(["Pierwszy w historii komputer nosił nazwę ENIAC", "TAK"])


    return questionList

def quizStart():

    print("POWAŻNY TEST WIEDZY Z INFORMATYKI")

    questios = questionGenerator()                    # pobiera pytania z funkcji questionGenerator
    random.shuffle(questios)                          # "tasueje" pytania z listy

    score = 0

    for element in questios:
        print(element[0])
        answer = input("Wpisz tak lub nie: ")

        if answer.upper() == element[1]:
            print("Poprawna odpowiedź!")
            print("")                      #ten print dla estetyki ;)
            score += 1
        else:
            print("Niepoprawna odpowiedź :c")
            print("")                      #ten też

    return scoreCalculator(score)

print(quizStart())
