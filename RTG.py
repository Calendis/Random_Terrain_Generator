import pygame
import random as Rand
from input_vars import *
print(chosen_array)
from math import sin

pygame.init()
screen = pygame.display.set_mode((1200, 900))
screen_width = pygame.Surface.get_width(screen)
screen_height = pygame.Surface.get_height(screen)

def start_display():
	R = 0
	G = 0
	B = 0

	firstrand = False
	firstCrand = False
	done = False
	i = 0

	while not done:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
		
		if i == 0:
			pygame.draw.rect(screen, (Rand.randint(0, 64), Rand.randint(16, 128), Rand.randint(64, 255)), pygame.Rect(0, 0, screen_width, screen_height)) #Draws the sky
			for i in range(0, pygame.Surface.get_width(screen)):
				
				if chosen_array[3] == 0:
					if firstrand == False:
						lastrand = Rand.randint(-chosen_array[0],chosen_array[0])
						firstrand = True
					else:
						lastrand += Rand.randint(-chosen_array[0],chosen_array[0])
				elif chosen_array[3] == 1:
					lastrand = Rand.randint(-chosen_array[0],chosen_array[0])
				elif chosen_array[3] == 2:
					if firstrand == False:
						lastrand = Rand.randint(-chosen_array[0],chosen_array[0])
						firstrand = True
					else:
						lastrand += Rand.randint(0, 1)
				elif chosen_array[3] == 3:
					if firstrand == False:
						lastrand = Rand.randint(-chosen_array[0], chosen_array[0])
						firstrand = True
					else:
						lastrand -= Rand.randint(0, 1)
				elif chosen_array[3] == 4:
					if firstrand == False:
						lastrand = Rand.randint(-chosen_array[0], chosen_array[0])
						firstrand = True
					else:
						lastrand += Rand.randint(-chosen_array[0],chosen_array[0])
						lastrand = -lastrand
				elif chosen_array[3] == 5:
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
					if firstrand == False:
						lastrand = Rand.randint(-chosen_array[0], chosen_array[0])
						firstrand = True
					else:
						lastrand += Rand.randint(-i, i)/7
				elif chosen_array[3] == 8:
					if firstrand == False:
						subrand = Rand.randint(-chosen_array[0],chosen_array[0])
						lastrand = Rand.randint(-chosen_array[0],chosen_array[0])
						firstrand = True
					else:
						subrand += Rand.randint(-chosen_array[0],chosen_array[0])
						subrand -= Rand.randint(-chosen_array[0],chosen_array[0])
						lastrand += subrand*chosen_array[0]/2000
				elif chosen_array[3] == 9:
					if firstrand == False:
						lastrand = Rand.randint(-chosen_array[0], chosen_array[0])
						firstrand = True
					else:
						lastrand = sin(i/50)*chosen_array[0]
					
					
						


						



				

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



				pygame.draw.rect(screen, (R, G, B), pygame.Rect(i, screen_height-chosen_array[1]+lastrand, 1*chosen_array[2], chosen_array[1]-lastrand))

				

				
				pygame.display.flip()
		pygame.display.flip()


start_display()
