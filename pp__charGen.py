'''imports the command for generating random numbers'''
from random import randint
print("\n==========Program Start==========")
"""common Lines and zeroing"""
invalid=("\nInvalid selection please try again")
plsEn="Please enter an option:"
"""Rule and table placeholder base"""
class nomod(object):
	ruleCheck=False
	def n(self):
		return print("\nNo %s Module Loaded" % str(self.checkName))
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
print()
dice.moduleCheck()
'''importing like in the following line does not work except for singular instances, just for reference'''
#import pp_module_diceRule
'''rule check method goes here, referenced later for checks'''
def rulecheck(s):
	if s.ruleCheck==True:
		ruleCheck=True
		return print("%s Rules: Present and %s." % (s.checkName, s.ruleCheck))
	elif s.ruleCheck==False:
		return print("%s Rules: Not Present and %s, please select" % (s.checkName, s.ruleCheck))
print()
"""Rule Checks"""
"""Referenced Immediately and as option 5 of overmenu"""
"""checks to make sure rule has been loaded by checking 'ruleCheck' variable in each class using 'rulecheck' method created earlier in the prototype main file"""
def ruleCheckList():
	rulecheck(dice)
	rulecheck(race)
	return
ruleCheckList()
def charmenu():
	print("\n==========Character Generation==========\n\n[1] Display Current Character Information\n[2] Roll for Attributes\n[/] or [t] Main Menu\n[*] or [q] Quit Program")
	menuSel=input(plsEn)
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
	print("\n==========Utilities==========\n\n[/] or [t] Main Menu\n[*] or [q] Quit Program")
	#dice.statRolls()
	menuSel=input(plsEn)
	if (menuSel=="t")or(menuSel=="/"):
		return mainmenu()
	elif (menuSel=="*")or(menuSel=="q"):
		return quit()
	else:
		print(invalid)
		return utilitymenu()
def optionsmenu():
	print("\n==========Options==========\n\n[/] or [t] Main Menu\n[*] or [q] Quit Program")
	#dice.statRolls()
	menuSel=input(plsEn)
	if (menuSel=="t")or(menuSel=="/"):
		return mainmenu()
	elif (menuSel=="*")or(menuSel=="q"):
		return quit()
	else:
		print(invalid)
		return optionsmenu()
def mainmenu():
	print("\n==========Main Menu==========\n\n[1] Character Generation\n[2] Utilities\n[3] Options\n[4] check imports\n[*] or [q] Quit Program")
	menuSel =input(plsEn)

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
		print(invalid)
		return mainmenu()
def quit():
	print("\nQuitting Program")
	input("Press Enter to close the program")
mainmenu()
input("Nothing left to run, press Enter to close the program")