import random as Rand
from math import sin
from presets import *



global chosen_array

terrain_presets = [original1, original2, original3, plains, mountains, random_terrain, 
downslopes, upslopes, iceplains, hills, volcanism, spires, rollinghills, pinkhills, bloodspires, 
mesa]


def start_up():
	choose_option = str(input(" Choose an option. Valid options are 'Generate' and 'Help':\n  "))
	choose_option = choose_option.lower()
	if choose_option == "generate":
		beginGeneration()
	elif choose_option == "help":
		print("\n Here is a list of terrain presets:")
		print(terrain_presets)



		start_up()
	else:
		print("\nINVALID OPTION\n\n")
		start_up()



def beginGeneration():
	global chosen_array
	
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


start_up()
