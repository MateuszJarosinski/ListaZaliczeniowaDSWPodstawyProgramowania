# tutaj na json

import json
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

def questionGenerator(questionsJSON):
    text = open(questionsJSON, "r").read()
    questions = json.loads(text)
    questions = random.sample(questions.items(), 10)

    score = 0

    for question, answer in questions:
        print(question)
        userAnswer = input("Wpisz tak lub nie: ")

        if userAnswer.upper() == answer:
            print("Poprawna odpowiedź!")
            print("")
            score += 1
        else:
            print("Niepoprawna odpowiedź :c")
            print("")

    return scoreCalculator(score)

print(questionGenerator("questions.JSON"))