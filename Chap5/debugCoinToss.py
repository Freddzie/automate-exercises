import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
# logging.basicConfig(filename='coinFlipLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s') 
logging.disable(logging.DEBUG) #stops the debugging from happening
logging.debug('Start of program')

import random
guess = ''

while True:
    try:
        print("Guess the coin toss! Enter 'h' or 't':")
        guess = input(">")
        logging.debug('guess is ' + str(guess))
        if guess not in ('h', 't'):
            raise ValueError
        else:
            break
    except ValueError:
        print("input must be 'h' or 't'")


toss = random.randint(0, 1)  # 0 is tails, 1 is heads
logging.debug('toss is ' + str(toss))
if toss == 1:
    toss = "h"
else:
    toss = "t"
logging.debug('toss is ' + str(toss))

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input(">")
    logging.debug('guess is ' + str(guess))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')