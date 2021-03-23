import random

guessesTaken = 0

print('Hi!!! What is your name?')
myName = input()

numberToGuess = random.randint(1,9)
print('So,'+myName+' , I am thinking of a random no between 1 and 9')

for guessesTaken in range(5):
    print('So, guess')
    noGuessesTaken = input()
    noGuessesTaken = int(guessesTaken)

    if(noGuessesTaken<numberToGuess):
        print('Sorry, your guess is too low')

    if(noGuessesTaken>numberToGuess):
        print('Sorry, your guess is too high')

    if(noGuessesTaken==numberToGuess):
        break

if(noGuessesTaken==numberToGuess):
    guessesTaken = str(guessesTaken+1)
    print('Good Job, '+myName+'! You guessed the no in'+guessesTaken+' guesses!')

if(noGuessesTaken!=numberToGuess):
    numberToGuess = str(numberToGuess)
    print('You didnt guess, but the no I was thinking of was'+numberToGuess)
