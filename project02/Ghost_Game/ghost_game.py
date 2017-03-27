# Ghost Game

from random import randint

print('\nGhost Game')

feeling_brave = True
score = 0

while feeling_brave:
	ghost_door = randint(1, 3)
	print('\nThree doors ahead....')
	print('A ghost behind one!')
	print('Which door will you open?')
	door = input('1, 2, or 3? ')
	door_num = int(door)
	if door_num == ghost_door:
		print('AGGHHH GHOST!!!')
		feeling_brave = False
	else:
		print('\nNo ghost! pheww!')
		print('You enter the next room..')
		score = score + 1
	
print('Run awayyyy!')
print('\nGame Over! You scored', score)
