# Error Handling
while True:
    try:
        age = int(input('what is your age? '))
        10/age
        print(age)
        # we can use raise instead of except if we want to cut the process because it is a huge error
        #raise ValueError('Hey! Cut it out')
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('Please enter age higher than 0')
        break
    else:
        print('Thanks')
        break
    finally:
        # finally runs always, no matter what error pops out
        print('ok, i am finally done')
    print('can you hear me?')


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'Please enter numbers {err}')


print(sum('1', 2))
