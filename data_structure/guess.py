import random
guesses = []
    
number = random.randint(1, 100)
    

def guess():
    while True:
        guess = int(input('what number am i thinking of?: '))
        guesses.append(guess)

        if guess == number:
            print(f'congratulations! you have guessed the number in {len(guesses)} attempts')
            break
        elif guess < number:
            print('guess higher')
        else:
            print('guess lower')

guess()