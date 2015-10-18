import random as Rand
from math import sin
from presets import *


custom_chosen = False
global chosen_array

terrain_presets = [original1, original2, original3, plains, mountains, random_terrain, 
downslopes, upslopes, iceplains, hills, forest, spires, rollinghills, pinkhills, bloodspires, 
mesa, sinewave, purple_mountains, slight_hills, void_rip, blue_spires,
 marc_hills, bars, obsidian, icebergs, ecf, mountains2]


def start_up():
	choose_option = str(input(" Choose an option. Valid options are 'Generate', 'Custom', and 'Help':\n  "))
	choose_option = choose_option.lower()
	if choose_option == "generate":
		beginGeneration()
	elif choose_option == "help":
		print("\n Here is a list of terrain presets:")
		print(terrain_presets)
	elif choose_option == "custom":
		beginCustom()



		start_up()
	else:
		print("\nINVALID OPTION\n\n")
		start_up()



def beginGeneration():
	global chosen_array, custom_chosen
	
	if custom_chosen == False:
		chosen_array = input("  Enter a terrain preset ID.\n\n   Valid IDs are from 0 to " + str(len(terrain_presets)-1) + ": ")
		try:
			int(chosen_array)
		except:
			print("Invalid ID: Enter an integer.")
			beginGeneration()
	
		chosen_array = int(chosen_array)
		if chosen_array > len(terrain_presets)-1:
			print("Invalid ID: Number too high.\n")
			beginGeneration()
		elif chosen_array < 0:
			print("Invalid ID: Number too low.\n")
			beginGeneration()
		else:
			chosen_array = terrain_presets[chosen_array]
	else:
		chosen_array = chosen_array



def beginCustom():
	custom_terrain_intensity = int(input(" Enter an intensity: "))
	custom_terrain_height = int(input(" Enter a height: "))
	custom_terrain_scalex = int(input(" Enter a scale x: "))
	custom_terrain_engine = int(input(" Enter an ID of a terrain generation engine: "))
	custom_terrain_R = int(input(" Enter an RGB red value: "))
	custom_terrain_G = int(input(" Enter an RGB green value: "))
	custom_terrain_B = int(input(" Enter a RGB blue value: "))
	custom_terrain_coloursharpness = int(input(" Enter a colour sharpness: "))
	custom_terrain_treechance = int(input(" Enter a tree chance: "))

	global chosen_array
	chosen_array = [custom_terrain_intensity, custom_terrain_height, custom_terrain_scalex, custom_terrain_engine,
	custom_terrain_R, custom_terrain_G, custom_terrain_B, custom_terrain_coloursharpness, custom_terrain_treechance]
	global custom_chosen
	custom_chosen = True
	beginGeneration()



<<<<<<< HEAD
start_up()
=======
start_up()
>>>>>>> 93df8da647be5b1268b74d9e507c41b9ba245ab9
