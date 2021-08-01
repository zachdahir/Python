# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Zachary Dahir>
# Creation Date: <7-27-21>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	#print('''You are in a land full of dragons. In front of you,
	#you see two caves. In one cave, the dragon is friendly
	#and will share his treasure with you. The other dragon
	#is greedy and hungry, and will eat you on sight.''')
	#print()
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight. \n''')
	#I removed the additional print() and replaced it with a \n for a new line
	

def chooseCave():
    #cave = ''
	cave = ''
	#fixed inproper spacing

	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	#return caves
	return cave
	#fixed varible name

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')

	#sleep for 2 seconds
	#time.sleep(3)
	time.sleep(2)
	#set sleep timer to match comment


	#print('A large dragon jumps out in front of you! He opens his jaws and...')
	#print()
	print('A large dragon jumps out in front of you! He opens his jaws and... \n')
	#removed additional print statement

	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		#print 'Gobbles you down in one bite!'
		print('Gobbles you down in one bite!')
		#added parenthesis to print statement

playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
#added = to fix syntax
	displayIntro()
	#caveNumber = choosecave()
	caveNumber = chooseCave()
	#fixed capitalization
	checkCave(caveNumber)
    
	#print('Do you want to play again? (yes or no)')
	#playAgain = input()
	playAgain = input('Do you want to play again? (yes or no)')
	#combined the input and print statement
	
	if playAgain == "no":
		#print("Thanks for planing")
		print("Thanks for playing")
		#fixed spelling