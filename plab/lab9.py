import random
secretnum=random.randint(1,20)
print("I am think of a number between 1 and 20")

for guesstaken in range(0,5):
    guessnum = int(input("Take a guess"))
    if guessnum < secretnum:
        print("Your guess is to low")
    elif guessnum > secretnum:
        print("your guess is too high")
    else:
        break
if guessnum==secretnum:
    print('Good job! You guessed my number in ' + str(guesstaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretnum))