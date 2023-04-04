import sys
from random import randint

first = int(sys.argv[1])
last = int(sys.argv[2])

print(f'first is {first} and last is {last}.')

x = randint(first, last)
got_it = False

while got_it is False:
    y = input(f'Say a number from {first} to {last}: ')
    try:
        if int(y) >= first and int(y) <= last:
            if x == int(y):
                print('You got it right!')
                got_it = True
            else:
                print('Nice try, keep trying.')
        else:
            print(f'Dude, I said from {first} to {last}.')
    except ValueError:
        print('Please enter a number')
        continue
