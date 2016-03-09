"""checks version and fixes raw_input for python 3 makign the code run on both 2.x and 3.x"""
import sys
if sys.version[0]=="3": raw_input=input
'''imports the command for generating random numbers'''
from random import randint
print("\n==========Program Start==========")
"""common Lines and zeroing"""
debug=False
menuSel="string"
mainReadout=1
charDebugReadout=0
invalid=("\nInvalid selection please try again")
plsEn="Please enter an option:"

"""Rule and table placeholder base"""
class nomod(object):
	ruleCheck=False
	def n(self):
		print("\nNo %s Module Loaded" % str(self.checkName))
		return

"""Rule and Table Placeholders"""
class attributeRolls(nomod):
	def __init__(self):
		self.checkName="Dice Module"
	def moduleCheck(self):
		return self.n()
	def statRolls(self):
		return self.n()
	def displayStatResults(self):
		return self.n()
dice=attributeRolls()
class raceRules(nomod):
	def __init__(self):
		self.checkName="Race Module"
race=raceRules()
print("==========Checking Modules==========")
'''config file check that handles imports goes here, until them import will just go here'''
from pp_module_diceRule import dice
#from pp_module_raceRule import race
print("")
dice.moduleCheck()

'''importing like in the following line does not work except for singular instances, just for reference'''
#import pp_module_diceRule
'''rule check method goes here, referenced later for checks'''
def rulecheck(s):
	if s.ruleCheck==True:
		ruleCheck=True
		print("%s Rules: Present and %s." % (s.checkName, s.ruleCheck))
		return
	elif s.ruleCheck==False:
		print("%s Rules: Not Present and %s, please select" % (s.checkName, s.ruleCheck))
		return
print("")
"""Rule Checks"""
"""Referenced Immediately and as option 5 of overmenu"""
"""checks to make sure rule has been loaded by checking 'ruleCheck' variable in each class using 'rulecheck' method created earlier in the prototype main file"""
def ruleCheckList():
	rulecheck(dice)
	rulecheck(race)
	return












def charmenu():

	print("\n==========Character Generation==========\n\n[1] Display Current Character Information\n[2] Roll for Attributes\n[/] or [t] Main Menu\n[*] or [q] Quit Program")
	menuSel=raw_input(plsEn)
	if (menuSel=="t")or(menuSel=="/"):
		return mainmenu()
	elif menuSel=="1":
		dice.displayStatResults()
		return charmenu()
	elif menuSel=="2":
		dice.statRolls()
		return charmenu()
	elif (menuSel=="*")or(menuSel=="q"):
		return quit()
	else:
		print(invalid)
		return charmenu()
	#character Generation
	#needs several options
	#option-1 is appearance
	#option-2 is dice rolls












def utilitymenu():
	"""the following line checks the global debug variable so it doesn't freak out for usign a variable not defined in the function"""
	global debug
	print("\n==========Utilities==========\n")
	if debug==False:
		print("Debug Options: Inactive\n")
	elif debug==True:
		print("Debug Options: Active\n")
	print("[1] Toggle Debug\n[/] or [t] Main Menu\n[*] or [q] Quit Program")
	menuSel=raw_input(plsEn)
	if (menuSel=="t")or(menuSel=="/"):
		return mainmenu()
	elif menuSel=="1":
		if debug==False:
			debug=True
		elif debug==True:
			debug=False
		return utilitymenu()
	elif (menuSel=="*")or(menuSel=="q"):
		return quit()
	else:
		print(invalid)
		return utilitymenu()












def optionsmenu():
	print("\n==========Options==========\n\n[/] or [t] Main Menu\n[*] or [q] Quit Program")
	#dice.statRolls()
	menuSel=raw_input(plsEn)
	if (menuSel=="t")or(menuSel=="/"):
		return mainmenu()
	elif (menuSel=="*")or(menuSel=="q"):
		return quit()
	else:
		print(invalid)
		return optionsmenu()












def mainmenu():
	#global variable check
	global mainReadout
	#debug Options
	mainDebug1=""
	if debug==True:
		mainDebug1="+[11] Check Character Generation Modules\n"
	elif debug==False:
		mainDebug1==""
	#header
	print("\n==========Main Menu==========\n")
	#main readout
	if mainReadout==1:
		ruleCheckList()
		print("")
	mainReadout=0
	#Options list, it references debug options
	print("[1] Character Generation\n%s[2] Utilities\n[3] Options\n[4] check imports\n[*] or [q] Quit Program" % (mainDebug1))
	menuSel=raw_input(plsEn)
	if (menuSel=="t")or(menuSel=="/"):
		return mainmenu()
	elif menuSel=="1":
		return charmenu()
	elif menuSel=="2":
		return utilitymenu()
	elif menuSel=="3":
		return optionsmenu()
	elif menuSel=="4":
		print("You selected %s Check Imports\n"  % menuSel)
		ruleCheckList()
		return mainmenu()
	elif (menuSel=="*")or(menuSel=="q"):
		return quit()
	else:
		"""MainMenu Debug Options"""
		if debug==True:
			if menuSel=="11":
				print("")
				mainReadout=1
				return mainmenu()
			else:
				print(invalid)
				return mainmenu()
		else:
			print(invalid)
			return mainmenu()












def quit():
	print("\nQuitting Program")
	raw_input("Press Enter to close the program")
mainmenu()
raw_input("Nothing left to run, press Enter to close the program")
'''debug branch upload from sgit on android'''

"""debug outline"""
#Done-main menu 1: lsit modules for character generation
#Char Gen Menu 1: lsit modules for character generation
#Char Gen Menu 2: Values for Dice Rolls
#UDone-tilities 1 Debug