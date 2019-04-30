import random
count = 0
Guess = int(input("Guess a number from 1 to 100:"))
Correct = random.randint(0,100)

while Guess != Correct:
	Guess = int(input("Guess again:"))

	if(Guess > Correct):
  		print('lower')
  	elif(Guess < Correct):
 		print('higher')
  	else:
 		print('yeah')
