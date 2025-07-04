import random

number = random.randint(1, 10)

gusses = 0
i = 10
while i >= 0:
    taxmin = int(input('Son kiriting >>>'))
    if taxmin == number:
        print('Tugri topdingiz !!! ')
        break
    i -= 1

    if gusses > 3:
        print('Siz yutqazdingiz')
        break


    


