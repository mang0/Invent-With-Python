## This is a guess the number game ##
##
#This import brings in the random library/module to the program, allowing me
#to generate random crap (in this case, numbers).
import random

guessesTaken = 0 #This var will store the guesses taken by the user - currently 0

#These next two lines are the same as in helloworld.py
print ("Hello! What is your name?")
myName = input("Enter: ")

number = random.randint(1, 20) #assigns a random integer to the variable 'number' Because
#prefix of random. is to tell program that randint is a function from the module random.
print ("Well, " + myName + ", I am thinking of a number between 1 and 20.")

while guessesTaken <6:
	print ("Take a guess.")
	guess = input("Enter: ")
	guess = int(guess)
	
	guessesTaken = guessesTaken + 1
	
	if guess < number:
		print ("Your guess is too low.")
		
	if guess > number:
		print ("Your guess is too high.")
		
	if guess == number:
		break
		
if guess == number:
	guessesTaken = str(guessesTaken)
	print("Good job, " + myName + "! You guessed my number in " + guessesTaken + " guesses!")
	
	if guess != number:
		number = str(number)
		print ("Nope. The number I was thinking of was " + number)