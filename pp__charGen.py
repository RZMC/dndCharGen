"""checks version and fixes raw_input for python 3 makign the code run on both 2.x and 3.x"""
import sys
if sys.version[0]=="3": raw_input=input
'''imports the command for generating random numbers'''
from random import randint
print("\n==========Program Start==========")
"""common Lines and zeroing"""
debug=False
menuSel="string"
mainReadout=991
charReadout=0
invalid=("Invalid selection please try again")
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
	print("")
	return




def charmenu():
	#global variable check
	global charReadout
	#debug Options
	charDebug1=""
	charDebug2=""
	if debug==True:
		charDebug1="+[11] Check Character Generation Modules\n"
		charDebug2="+[12] Check Character Generation Modules\n"
	elif debug==False:
		charDebug1=""
		charDebug2=""
	else:charDebug1=""
	#header
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n==========Character Generation==========\n")
	#readout for char
	if charReadout==0:print("\n")
	elif charReadout==1:dice.displayStatResults()
	elif charReadout==2:dice.statRolls()
	elif charReadout==11:ruleCheckList()
	elif charReadout==12:dice.moduleCheck()
	elif charReadout==999:print( "%s\n" % invalid)
	charReadout=0
	#Options list, it references debug options
	print("[1] Display Current Character Information\n%s%s[2] Roll for Attributes\n[/] or [t] Main Menu\n[*] or [q] Quit Program" % (charDebug1, charDebug2))
	#menu input for char
	menuSel=raw_input(plsEn)
	if (menuSel=="t")or(menuSel=="/"):return mainmenu()
	elif menuSel=="1":
		charReadout=1
		return charmenu()
	elif menuSel=="2":
		charReadout=2
		return charmenu()
	elif (menuSel=="*")or(menuSel=="q"):return quit()
	else:
		"""MainMenu Debug Options"""
		if debug==True:
			if menuSel=="11":
				print("")
				charReadout=11
				return charmenu()
			if menuSel=="12":
				print("")
				charReadout=12
				return charmenu()
			else:
				charReadout=999
				return charmenu()
		else:
			charReadout=999
			return charmenu()
	#character Generation
	#needs several options
	#option-1 is appearance
	#option-2 is dice rolls




def utilitymenu():
	"""the following line checks the global debug variable so it doesn't freak out for usign a variable not defined in the function"""
	global debug
	#header
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n==========Utilities==========\n")
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
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n==========Options==========\n\n[/] or [t] Main Menu\n[*] or [q] Quit Program")
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
	if debug==True:mainDebug1="+[11] Check Character Generation Modules\n"
	elif debug==False:mainDebug1=""
	#header
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n==========Main Menu==========\n")
	#readout for main
	if mainReadout==0:print("\n")
	elif mainReadout==11:ruleCheckList()
	elif mainReadout==991:
		ruleCheckList()
		dice.moduleCheck()
	elif mainReadout==999:print( "%s\n" % invalid)
	else:print("\n")
	mainReadout=0
	#Options list, it references debug options
	print("[1] Character Generation\n%s[2] Utilities\n[3] Options\n[*] or [q] Quit Program" % (mainDebug1))
	#menu input for main
	menuSel=raw_input(plsEn)
	if (menuSel=="t")or(menuSel=="/"):return mainmenu()
	elif menuSel=="1":return charmenu()
	elif menuSel=="2":return utilitymenu()
	elif menuSel=="3":return optionsmenu()
	elif (menuSel=="*")or(menuSel=="q"):return quit()
	else:
		"""MainMenu Debug Options"""
		if debug==True:
			if menuSel=="11":
				print("")
				mainReadout=11
				return mainmenu()
			else:
				mainReadout=999
				return mainmenu()
		else:
			mainReadout=999
			return mainmenu()








def quit():
	print("\nQuitting Program")
	raw_input("Press Enter to close the program")
mainmenu()
raw_input("Nothing left to run, press Enter to close the program")
'''debug branch upload from sgit on android'''

"""debug outline"""
#Done-main menu 1: lsit modules for character generation
#Done-Char Gen Menu 1: lsit modules for character generation
#Done-Char Gen Menu 2: Values for Dice Rolls
#UDone-tilities 1 Debug