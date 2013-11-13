###################################################################
#Author:				Matt Hall
#Description:			This script is intended to be a proof of
#						concept for a text-based game.
#
#Date Created:			10/09/2013
#Date Last Modified:	10/09/2013
###################################################################

##maybe a system that involves control a base or outpost
##and tracking some numbers
##perhaps some room to room movement or menu systems?

introduction = "This will be where I will explain the purpose of the game."
#consider restricting string length?
tribename_input = "By what name is your tribe known?"
tribename = str(input(tribename_input+"\n"))#use on status screen?

population_label = ["men", "women", "children"]
population_number = [0,0,0]

food_label = ["meat","fruit","grains"]
food_number = [0,0,0]

materials_label = ["wood","grasses","skins","bones"]
materials_number = [0,0,0,0]

##options for activity should involve things needed survival
##also future construction projects and combat may need to be
##considered.

##tribal menu?

def tribal_menu():
	#set menu strings
	menu_title_str = "Tribal Menu"
	current_action = ""
	gather_menu_str = "(G)ather"
	quit_game_str = "(Q)uit"
	hunt_menu_str = "(H)unt"

def gather_menu():
	#set menu strings
	#what gather actions are possible?
	#should time of year be tracked and
	#should it impact what actions are
	#available when?
	menu_title_str = "Gather Menu"

#should ask for tribe name, maybe some historical background
#generate inital lists for population, food, and materials.
def build_new_tribe():


