import random

quotes = ['this is a quote', 'another quote', 'a third quote']
quote = random.randint(0 , 2)


def guess2():
    while True:
        guess2 = int(input('pick a number: '))

        if guess2 == quote:
            print(f'your quote is:  {quotes[quote]}')
            break
        elif guess2 > 2:
            print('out of bounds, pick a lower number')
        else:
            print('guess another number')
guess2()