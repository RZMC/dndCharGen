'''imports the command for generating random numbers'''
from random import randint
print()
print("==========Program Start==========")
"""Rule and table placeholder base"""
class nomod(object):
	ruleCheck=False
	def n(self):
		print()
		return print("No %s Module Loaded" % str(self.checkName))
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
dice = attributeRolls()
class raceRules(nomod):
	def __init__(self):
		self.checkName="Race Module"
race = raceRules()
print("==========Checking Modules==========")
'''config file check that handles imports goes here, until them import will just go here'''
from pp_module_diceRule import dice
#from pp_module_raceRule import race
#print()
#dice.moduleCheck()
'''importing like in the following line does not work except for singular instances, just for reference'''
#import pp_module_diceRule
'''rule check method goes here, referenced later for checks'''
def rulecheck(s):
	if s.ruleCheck == True:
		ruleCheck = True
		return print("%s Rules: Present and %s." % (s.checkName, s.ruleCheck))
	elif s.ruleCheck == False:
		return print("%s Rules: Not Present and %s, please select" % (s.checkName, s.ruleCheck))
print("")
"""Rule Checks"""
"""Referenced Immediately and as option 5 of overmenu"""
"""checks to make sure rule has been loaded by checking 'ruleCheck' variable in each class using 'rulecheck' method created earlier in the prototype main file"""
def ruleCheckList():
	rulecheck(dice)
	rulecheck(race)
	return
ruleCheckList()
def charmenu():
	print()
	print("==========Character Generation==========")
	print()
	print("(1) Display Current Character Information")
	print("(2) Roll for Attributes")
	print("(t) Main Menu")
	print("(q) Quit Program")
	#dice.statRolls()
	charMenu = input("Please enter an option:")
	if charMenu == "t":
		return mainmenu()
	elif charMenu == "1":
		dice.displayStatResults()
		return charmenu()
	elif charMenu == "2":
		dice.statRolls()
		return charmenu()
	elif charMenu == "q":
		return quit()
	else:
		print()
		print("Invalid selection please try again")
		return charmenu()
	#character Generation
	#needs several options
	#option-1 is appearance
	#option-2 is dice rolls
def utilitymenu():
	print()
	print("==========Utilities==========")
	print()
	print("(t) Main Menu")
	print("(q) Quit Program")
	#dice.statRolls()
	utilMenu = input("Please enter an option:")
	if utilMenu == "t":
		return mainmenu()
	elif utilMenu == "q":
		return quit()
	else:
		print()
		print("Invalid selection please try again")
		return utilitymenu()
def optionsmenu():
	print()
	print("==========Options==========")
	print()
	print("(t) Main Menu")
	print("(q) Quit Program")
	#dice.statRolls()
	optionMenu = input("Please enter an option:")
	if optionMenu == "t":
		return mainmenu()
	elif optionMenu == "q":
		return quit()
	else:
		print()
		print("Invalid selection please try again")
		return optionsmenu()
def mainmenu():
	print()
	print("==========Main Menu==========")
	print()
	print("(1) Character Generation")
	print("(2) Utilities")
	print("(3) Options")
	print("(4) check imports")
	print("(q) Quit Program")
	menuTop =input("Please enter an option:")
	if menuTop =="t":
		return mainmenu()
	elif menuTop == "1":
		return charmenu()
	elif menuTop == "2":
		return utilitymenu()
	elif menuTop == "3":
		return optionsmenu()
	elif menuTop == "4":
		print("You selected %s Check Imports" % menuTop)
		print()
		ruleCheckList()
		return mainmenu()
	elif menuTop == "q":
		return quit()
	else:
		print()
		print("Invalid selection please try again")
		return mainmenu()
def quit():
	print()
	print("Quitting Program")
	input("Press Enter to close the program")
mainmenu()
input("Nothing left to run, press Enter to close the program")