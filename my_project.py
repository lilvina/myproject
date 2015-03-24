import random

def my_project():
	x = int(raw_input("How many times do you want to play?"))
	for i in range(x):
		objects = ['rock', 'paper', 'scissors']
		computer_choice = random.choice(objects)
		print computer_choice
		player1_choice = raw_input('What do you want to play?')
		if computer_choice == 'rock' and player1_choice == 'paper':
			print "player1 will beat the computer"
		if computer_choice == 'paper' and player1_choice == 'scissors':
			print "player1 will beat the computer"
		if computer_choice == 'scissors' and  player1_choice == 'rock':
			print "player1 will beat the computer"
		if computer_choice == 'paper' and player1_choice == 'paper':
			print "It will be a tie"
		if computer_choice == 'rock' and player1_choice == 'scissors':
			print "the computer will beat player1"
		if computer_choice == 'rock' and player1_choice == 'rock':
			print "It will be a tie"
		if computer_choice == 'paper' and player1_choice == 'rock':
			print "the computer will beat player1"
		if computer_choice == 'scissors' and player1_choice == 'paper':
			print "the computer will beat player1"
		if computer_choice == 'scissors' and player1_choice == 'scissors':
			print "It will be a tie"						
	# computer_choice = random.choice(objects)
	# print player1_choice
	# player2_choice = raw_input('What do you want to play?')
	# if player1_choice == 'rock' and player2_choice == 'paper':
	# 	print "player2 will beat player1"
	# if player1_choice == 'paper' and player2_choice == 'scissors':
	# 	print "player2 will beat player1"
	# if player1_choice == 'scissors' and player2_choice == 'rock':
	# 	print "player2 will beat player1"
	# if player1_choice == 'paper' and player2_choice == 'paper':
	# 	print "It will be a tie"
	# if player1_choice == 'rock' and player2_choice == 'scissors':
	# 	print "player1 will beat player2"
	# if player1_choice == 'rock' and player2_choice == 'rock':
	# 	print "It will be a tie"	
	# if player1_choice == 'paper' and player2_choice == 'rock':
	# 	print "player1 will beat player2"
	# if player1_choice == 'scissors' and player2_choice == 'paper':
	# 	print "player1 will beat player2"
	# if player1_choice == 'scissors' and player2_choice == 'scissors':
	# 	print "It will be a tie"								
	
my_project()

 		





