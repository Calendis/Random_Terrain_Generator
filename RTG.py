import pygame
import random as Rand
from pygame.locals import *
from input_vars import *
print(chosen_array)
from math import sin
from lib import *

pygame.init()
screen = pygame.display.set_mode((1200, 900), RESIZABLE)
screen_width = pygame.Surface.get_width(screen)
screen_height = pygame.Surface.get_height(screen)

tree1 = pygame.image.load("tree.png")
tree2 = pygame.image.load("tree2.png")
tree3 = pygame.image.load("tree3.png")
tree4 = pygame.image.load("tree4.png")
#tree5 = pygame.image.load("tree5.png")

tree_array = [tree1, tree2, tree3, tree4]

global lastrand_array
lastrand_array =[]




def start_display():
	

	R = 0
	G = 0
	B = 0

	firstrand = False
	firstCrand = False
	done = False

	lastrand = 0
	subrand = 0

	i = 0

	while not done:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
		
		if i == 0:
			pygame.draw.rect(screen, (Rand.randint(0, 64), Rand.randint(16, 128), Rand.randint(64, 255)), pygame.Rect(0, 0, screen_width, screen_height)) #Draws the sky
			for i in range(0, pygame.Surface.get_width(screen)):
				
				'''chosen_array[3] contains an integer. This integer is the id of a terrain generation engine.
				the code that starts with if chosen_array[3] == (an integer) is the terrain generation based on the engine.'''

				if chosen_array[3] == 0:
					#Old generation: spiky hills.
					if firstrand == False:
						lastrand = Rand.randint(-chosen_array[0],chosen_array[0])
						firstrand = True
					else:
						lastrand += Rand.randint(-chosen_array[0],chosen_array[0])
				elif chosen_array[3] == 1:
					#Original generation: random spikes. Pretty bad. Only keeping for nostalgia's sake. It's only one line lol
					lastrand = Rand.randint(-chosen_array[0],chosen_array[0])
				elif chosen_array[3] == 2:
					#downslopes
					if firstrand == False:
						lastrand = Rand.randint(-chosen_array[0],chosen_array[0])
						firstrand = True
					else:
						lastrand += Rand.randint(0, 1)
				elif chosen_array[3] == 3:
					#upslopes
					if firstrand == False:
						lastrand = Rand.randint(-chosen_array[0], chosen_array[0])
						firstrand = True
					else:
						lastrand -= Rand.randint(0, 1)
				elif chosen_array[3] == 4:
					#Spiky hills with inverse bg effect. Only works if x-scale is 1
					if firstrand == False:
						lastrand = Rand.randint(-chosen_array[0], chosen_array[0])
						firstrand = True
					else:
						lastrand += Rand.randint(-chosen_array[0],chosen_array[0])
						lastrand = -lastrand
				elif chosen_array[3] == 5:
					#Bouldery hills? Used on old volcanism preset
					if firstrand == False:
						subrand = Rand.randint(-chosen_array[0],chosen_array[0])
						lastrand = Rand.randint(-chosen_array[0],chosen_array[0])
						firstrand = True
					else:
						subrand += Rand.randint(-chosen_array[0],chosen_array[0])
						subrand -= Rand.randint(-chosen_array[0],chosen_array[0])
						if subrand*10 != 0:
							lastrand += 1/subrand*chosen_array[0]
						else:
							subrand = Rand.randint(-chosen_array[0],chosen_array[0])
						
				elif chosen_array[3] == 6:
					#sawtooth mesa terrain
					if firstrand == False:
						subrand = Rand.randint(-chosen_array[0],chosen_array[0])
						lastrand = Rand.randint(-chosen_array[0],chosen_array[0])
						firstrand = True
					else:
						subrand += Rand.randint(-chosen_array[0],chosen_array[0])
						subrand -= Rand.randint(-chosen_array[0],chosen_array[0])
						lastrand += subrand*chosen_array[0]/2000
						if Rand.randint(0, 20) == 0:
							lastrand *= Rand.randint(-2, 2)
				elif chosen_array[3] == 7:
					#Similar to zero, but more intense and better suited to spires
					if firstrand == False:
						lastrand = Rand.randint(-chosen_array[0], chosen_array[0])
						firstrand = True
					else:
						lastrand += Rand.randint(-i, i)/7
				elif chosen_array[3] == 8:
					#Smooth hills
					if firstrand == False:
						subrand = Rand.randint(-chosen_array[0],chosen_array[0])
						lastrand = Rand.randint(-chosen_array[0],chosen_array[0])
						firstrand = True
					else:
						subrand += Rand.randint(-chosen_array[0],chosen_array[0])
						subrand -= Rand.randint(-chosen_array[0],chosen_array[0])
						lastrand += subrand*chosen_array[0]/2000
				elif chosen_array[3] == 9:
					#Sine wave
					if firstrand == False:
						lastrand = Rand.randint(-chosen_array[0], chosen_array[0])
						firstrand = True
					else:
						lastrand = sin(i/50)*chosen_array[0]
				elif chosen_array[4] == 10:
					#WIP. Next engine not yet planned.
					pass
						

				'''End of terrain generating code and start of colour generating code'''

				hR = round(chosen_array[4]/2) 
				hG = round(chosen_array[5]/2)
				hB = round(chosen_array[6]/2)
				
				
				

				if firstCrand == False:
					if chosen_array[4] == chosen_array[5] and chosen_array[5] == chosen_array[6]:
						R = Rand.randint(hR, chosen_array[4])
						G = R
						B = G
					else:
						R = Rand.randint(hR, chosen_array[4])
						G = Rand.randint(hG, chosen_array[5])
						B = Rand.randint(hB, chosen_array[6])

					firstCrand = True
				else:
					lastCrand = Rand.randint(0, chosen_array[7])
					if Rand.randint(0, 2) == 0:
						if Rand.randint(0, 1) == 0:
							if R + chosen_array[7] < chosen_array[4]:
								R += lastCrand
							if G + chosen_array[7] < chosen_array[5]:
								G += lastCrand
							if B + chosen_array[7] < chosen_array[6]:
								B += lastCrand
						else:
							if R - chosen_array[7] > hR:
								R -= lastCrand
							if G - chosen_array[7] > hG:
								G -= lastCrand
							if B - chosen_array[7] >hB:
								B -= lastCrand


				'''End of colour generating code. Start of ACTUAL GENERATION.'''

				'''The following is a check to see if the terrain has gone off
				of the screen or below it. If true, it makes it generate back on-screen, with some leway

				The check only works with terrain generation engines 5, 6, and 8.'''



				if(chosen_array[1]-lastrand > screen_height + 50):
					#print("WARNING: Terrain above screen height!")
					subrand *= -0.5
					
				if(chosen_array[1]-lastrand < -50):
					#print("WARNING: Terrain below screen height!" + str(Rand.randint(99, 10000)))
					subrand *= -0.5




				'''The important line of code is:'''
				#pygame.draw.rect(screen, (R, G, B), pygame.Rect(i, screen_height-chosen_array[1]+lastrand, 1*chosen_array[2], chosen_array[1]-lastrand))
				'''It does the generation with all the support of the engine and the terrain preset array!'''
				
				pygame.draw.rect(screen, (R, G, B), pygame.Rect(i, screen_height-chosen_array[1]+lastrand, 1*chosen_array[2], chosen_array[1]-lastrand))
				
				lastrand_array.append(lastrand)
				
				#pygame.display.flip() #Comment out this line to disable viewing the terrain generate line-by-line

			'''This code generates trees along the top of the terrain, using data from the array lastrand_array.'''
			for i in range(0, pygame.Surface.get_width(screen)):
				if Rand.randint(1, 101) <= chosen_array[8]:
					if Rand.randint(0, 9) == 0:
						chosen_tree = Rand.randint(0, len(tree_array)-1)
						screen.blit(tree_array[chosen_tree], (i, screen_height-chosen_array[1]+lastrand_array[i]- (lastrand_array[i-1]-lastrand_array[i])-25 ))
						
						#pygame.display.flip()
					

		pygame.display.flip()


<<<<<<< HEAD
start_display()
=======
start_display()
>>>>>>> 93df8da647be5b1268b74d9e507c41b9ba245ab9
