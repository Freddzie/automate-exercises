#Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return 
# this value. If number is odd, then collatz() should print and return 3 * number + 1.
#Then, write a program that lets the user enter an integer and that keeps calling collatz() on that number until the function returns the value 1. 
#(Amazingly enough, this sequence actually works for any integer
#Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value. 
#To make the output more compact, the print() calls that print the numbers should have a end=' ' named parameter to print all values on one line.

#PLAN

# collatz() function: 
# take in a number assign it to number parameter.
# if even (number % 2 == 0) then print (number // 2) and return (number // 2) end = ''
# if odd (number % 2 == 1) then print and return (3 * number + 1) end = ''

#Main Program
#ask user for input and store it in a variable, convert to int
#try except to catch non int inputs
#while loop to force user to input whole number greater than 1
#try: input number, if number <= 1 or if number != int: continue. else: break

#then loop call collatz(number) with the loop condition being does number = 1
#so. while number != 1 do: number = collatz(number) this updates the number with the return value

def collatz(number):
    if number % 2 == 0: #check if even
        number //= 2
        print(number, end=' ')
        return(number) #returns number so it can be stored and come back.
    else: # if odd (not even) 
        number = 3 * number + 1
        print(number, end=' ')
        return(number)

#main
while True:
    try:
        print("please enter a number to callatzify!")
        number = int(input(">")) #gets user number input
        if number <= 1:
            continue #if number is not greater then 1 then go back to start
        else:
            print(number, end=' ') #print starting number and break loop to move on to main section
            break
    except ValueError:
        print("you have not entered a int") #catches any input thats not an int. then goes back to start
        continue

while number != 1: 
    number = collatz(number) #loops through function until done (returns 1 )

## README

# end of chapter 4 excersize from book "Automate the Boring Stuff with Python" by Al Sweigart
# notes above the code is my plan before writing the code.
# key concepts: string formatting, functions, try except blocks for user input, loops.
# main failure: i forgot to update number outside of the function when number was returned causing an infinite loop.