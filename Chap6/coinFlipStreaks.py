# For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an H for each heads and a T for each tails, 
# you’ll create a list that looks like T T T T H H H H T T. If you ask a human to make up 100 random coin flips, you’ll probably end up with 
# alternating heads-tails results like H T H T H H T H T T—which looks random (to humans), but isn’t mathematically random. A human will 
# almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips. 
# Humans are predictably bad at being random.
# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of 
# 100 heads and tails. Your program should break up the experiment into two parts: the first part generates a list of 100 randomly 
# selected 'H' and 'T' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats 
# the experiment 10,000 times so that you can find out what percentage of the coin flips contains a streak of six heads or six 
# tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50 percent of the time and a 1 value the 
# other 50 percent of the time.

#PLAN----------------------------
#generate list of 100 H or T:

#----------random choice of [H, T]
#append to list
#-----------check if there is a streak of 6 or more of H or T:
#have a count variable and sideOfCoin variable
#if sideOfCoin != list item then replace sideOfCoin with it and reset count to 1
#if sideOfCoin is the same as list item then only add one to count
#if count is == 6 then add one to score and break out of loop by returning either true or false
#loop for length of list

#repeat 10,000 times
#percentage of times contained = score / 10000 * 100

#--------------------------------
import random, sys, logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL) #disables the not so important logs


logging.info('start program')
FLIPS = 100 #how many flips per run
SAMPLES_SIZE = 10000 #how many times will we run the flip function
STREAK = 6 #size of streak we are counting for

score = 0

def flipStreak(i):
    logging.info('start flipStreak Func num: ' +str(i))
    result = []
    sideOfCoin = '' 
    counter = 1

    for i in range(FLIPS):
        result.append(random.choice(['H', 'T']))
        logging.debug('i = '+ str(i)+ 'Flip = '+str(result[-1]))
        if result[-1] != sideOfCoin: #if last item in list != last result then
            sideOfCoin = result[-1]
            counter = 1
        else:
            counter += 1

        if counter == STREAK:
            return True
    return False

for i in range(SAMPLES_SIZE):
    if flipStreak(i):
        score += 1

print(round((score/SAMPLES_SIZE)*100,2))


#this is a big imporvement from the comma separator, i wrote a better plan and tweeked it while coding when i realised using one fuction would
#be more efficient. i figured out how the logging worked better and i set constant variables. overall happpy with it.