import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Steven'
    elif answerNumber == 2:
        return 'Peter'
    elif answerNumber == 3:
        return 'Susan'
    elif answerNumber == 4:
        return 'Mary'
    elif answerNumber == 5:
        return 'Tom'
    elif answerNumber == 6:
        return 'Daisy'
    elif answerNumber == 7:
        return 'Louis'
    elif answerNumber == 8:
        return 'Sammy'
    elif answerNumber == 9:
        return 'Lucky'
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)