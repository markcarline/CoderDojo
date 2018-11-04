import pygame
import time
import curses

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

e3 = pygame.mixer.Sound('/home/pi/CoderDojo/project07/Samples//E3.wav')
g3 = pygame.mixer.Sound('/home/pi/CoderDojo/project07/Samples/G3.wav')
a3 = pygame.mixer.Sound('/home/pi/CoderDojo/project07/Samples/A3.wav')
b3 = pygame.mixer.Sound('/home/pi/CoderDojo/project07/Samples/B3.wav')
bb3 = pygame.mixer.Sound('/home/pi/CoderDojo/project07/Samples/Bb3.wav')
c4 = pygame.mixer.Sound('/home/pi/CoderDojo/project07/Samples/C4.wav')
d4 = pygame.mixer.Sound('/home/pi/CoderDojo/project07/Samples/D4.wav')
e4 = pygame.mixer.Sound('/home/pi/CoderDojo/project07/Samples/E4.wav')

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

screen.clear()

while True:
	screen.addstr(1, 0, "Ready to accept up, down, left or right to play sounds or q to quit!")
	screen.addstr(2, 0, "To get to a new console press Alt-F2")

	event = screen.getch()

	screen.clear()

	if event == ord('q'):
		break
	elif event == curses.KEY_UP:
		screen.addstr(0, 0, "You pressed up! - Playing E3")
		e3.play()
	elif event == ord('g'):
		screen.clear()
		screen.addstr(0, 0, "You pressed g!- Playing G3")
		g3.play()
	elif event == curses.KEY_DOWN:
		screen.clear()
		screen.addstr(0, 0, "You pressed down! - Playing A3")
		a3.play()
	elif event == curses.KEY_LEFT:
		screen.clear()
		screen.addstr(0, 0, "You pressed left! - Playing B3")
		b3.play()
	elif event == ord('w'):
		screen.clear()
		screen.addstr(0, 0, "You pressed w! - Playing Bb3")
		bb3.play()
	elif event == curses.KEY_RIGHT:
		screen.clear()
		screen.addstr(0, 0, "You pressed right! - Playing C4")
		c4.play()
	elif event == ord('d'):
		screen.clear()
		screen.addstr(0, 0, "You pressed d! - Playing D4")
		d4.play()
        elif event == ord(' '):
		screen.clear()
		screen.addstr(0, 0, "You pressed space! - Playing E4")
		e4.play()
	else:
		screen.clear()
		screen.addstr(0, 0, "That key doesn't do anything!")

curses.endwin()
