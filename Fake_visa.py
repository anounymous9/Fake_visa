from math import exp
from os import system
import random, time

#colors
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'


print(f'''\033[34m
   __      _                  _           
  / _|    | |                (_)          
 | |_ __ _| | _____    __   ___ ___  __ _ 
 |  _/ _` | |/ / _ \   \ \ / / / __|/ _` |
 | || (_| |   <  __/    \ V /| \__ \ (_| |
 |_| \__,_|_|\_\___|     \_/ |_|___/\__,_|

\033[33mBy Saif AL-klbani | My Instagram : dr.anonymous9
''')


print( '\033[32m' +"/ This generator only generates Visa credit cards. \ ")
nb_nitros = int(input('\033[35m' + "Please enter the number of cards to generate : "))
nb = 1
print("Generation of the credit card...")
print("(This operation may take some second) ")
while nb <= nb_nitros:
    exp_date2 = str(random.randint(1, 12))
    if exp_date2 == str(1):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(2):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(3):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(4):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(5):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(6):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(7):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(8):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(9):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(10):
        pass
    elif exp_date2 == str(11):
        pass
    elif exp_date2 == str(12):
        pass
    card = "454003" + str(random.randint(10, 99)) + "" + str(random.randint(1000, 9999)) + "" + str(random.randint(1000, 9999)) + " | " + exp_date2 + "/"  + str(random.randint(23, 28)) + " | " + str(random.randint(100, 999))
    f = open('Cods.txt', "a+")
    f.write(f'{card}\n')
    f.close()

    print(f" \033[31m [GENERATED] - \033[34m {card} ")
    time.sleep(0.025)
    nb += 1

print('\033[33m'+"Your cards are saved in Code.txt"+'\033[37m')

