import random

number = random.randint(1, 10)

i = 10
while i >= 0:
    taxmin = int(input('Son kiriting >>>'))
    if taxmin == number:
        print('Tugri topdingiz !!! ')
        break
    i -= 1

    


