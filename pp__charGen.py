#checks version and fixes raw_input for python 3 makign the code run on both 2.x and 3.x
import sys
if sys.version[0]=="3": raw_input=input
#imports the command for generating random numbers
from random import randint
print("\n==========Program Start==========")
#common Lines and zeroing
debug=False
menuSel="string"
mReadout=991
cReadout=0
invalid=("Invalid selection please try again")
plsEn="Please enter an option:"
#Rule and table placeholder base
class nomod(object):
	ruleCheck=False
	def n(self):
		print("\nNo %s Module Loaded" % str(self.checkName))
		return
#Rule and Table Placeholders
class attributeRolls(nomod):
	def __init__(self):self.checkName="Dice Module"
	def moduleCheck(self):return self.n()
	def statRolls(self):return self.n()
	def displayStatResults(self):return self.n()
dice=attributeRolls()
class raceRules(nomod):
	def __init__(self):self.checkName="Race Module"
race=raceRules()
print("==========Checking Modules==========")
#config file check that handles imports goes here, until them import will just go here
from pp_module_diceRule import dice
#from pp_module_raceRule import race
print("")
dice.moduleCheck()

#importing as in the following line does not work except for singular instances, just for reference
#import pp_module_diceRule
#rule check method goes here, referenced later for checks
def rulecheck(s):
	if s.ruleCheck==True:
		ruleCheck=True
		print("%s Rules: Present and %s." % (s.checkName, s.ruleCheck))
		return
	elif s.ruleCheck==False:
		print("%s Rules: Not Present and %s, please select" % (s.checkName, s.ruleCheck))
		return
print("")
#"""Rule Checks"""
#"""Referenced Immediately and as option 5 of overmenu"""
#"""checks to make sure rule has been loaded by checking 'ruleCheck' variable in each class using 'rulecheck' method created earlier in the prototype main file"""
def ruleCheckList():
	x=""
	rulecheck(dice)
	rulecheck(race)
	return x




def cRead(x):
	global cReadout
	cReadout=x
	return charmenu()

def charmenu():
	#global variable check
	global cReadout
	#debug Options
	cDebug1=""
	cDebug2=""
	if debug==True:
		cDebug1="+[11] Check Character Generation Modules\n"
		cDebug2="+[12] Check Character Generation Modules\n"
	elif debug==False:
		cDebug1=""
		cDebug2=""
	else:cDebug1=""
	#header
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n==========Character Generation==========\n")
	#readout for char
	if cReadout==0:print("")
	elif cReadout==1:dice.displayStatResults()
		#cReadout 1 needs to be expanded to display all current character information
	elif cReadout==2:dice.statRolls()
	elif cReadout==11:ruleCheckList()
	elif cReadout==12:print(dice.moduleCheck())
	elif cReadout==999:print(invalid)
	cReadout=0
	#Options list, it references debug options
	print("\n[1] Display Current Character Information\n%s%s[2] Roll for Attributes\n[/] or [t] Main Menu\n[*] or [q] Quit Program" % (cDebug1, cDebug2))
	#CharMenu input
	menuSel=raw_input(plsEn)
	if menuSel in("t","/"):return mainmenu()
	elif menuSel=="1": return cRead(1)
	elif menuSel=="2":return cRead(2)
	elif menuSel in ("*", "q"):return quit()
	#CharMenu Debug Options
	elif menuSel=="11" and debug:return cRead(11)
	elif menuSel=="12" and debug:return cRead(12)
	#Return wrong entry
	else:return cRead(999)
	#needs appearance option
	#needs inventory option
	#-needs to be dynamic with a setting for number of descriptors (name, weight, description etc.)
	#-should use dictionary for each entry
	#-entry zero should have the descriptor names like name, weight, description




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
	if menuSel in("t","/"):return mainmenu()
	elif menuSel=="1":
		if debug==False:
			debug=True
		elif debug==True:
			debug=False
		return utilitymenu()
	elif menuSel in ("*", "q"):return quit()
	else:
		print(invalid)
		return utilitymenu()




def optionsmenu():
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n==========Options==========\n\n[/] or [t] Main Menu\n[*] or [q] Quit Program")
	#dice.statRolls()
	menuSel=raw_input(plsEn)
	if menuSel in("t","/"):return mainmenu()
	elif menuSel in ("*", "q"):return quit()
	else:
		print(invalid)
		return optionsmenu()




def mRead(x):
	global mReadout
	mReadout=x
	return mainmenu()

def mainmenu():
	#global variable check
	global mReadout
	#debug readouts
	mDebug1=""
	if debug==True:mDebug1="+[11] Check Character Generation Modules\n"
	elif debug==False:mDebug1=""
	#header
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n==========Main Menu==========\n")
	#readout for main
	if mReadout==0:print("")
	elif mReadout==11:ruleCheckList()
	elif mReadout==991:print("%s\n%s" % (ruleCheckList(), dice.moduleCheck()))
	elif mReadout==999:print(invalid)
	else:print("\n")
	mReadout=0
	#Options list, it references debug options
	print("\n[1] Character Generation\n%s[2] Utilities\n[3] Options\n[*] or [q] Quit Program" % (mDebug1))
	#menu input for main
	menuSel=raw_input(plsEn)
	if menuSel in("t","/"):return mainmenu()
	elif menuSel=="1":return charmenu()
	elif menuSel=="2":return utilitymenu()
	elif menuSel=="3":return optionsmenu()
	#mainmenu debug inputs
	elif menuSel=="11" and debug:return mRead(11)
	elif menuSel in ("*", "q"):return quit()
	#Return wrong entry
	else:return mRead(999)




def quit():raw_input("\nQuitting Program\nPress Enter to close the program")

mainmenu()

raw_input("Nothing left to run, press Enter to close the program")

"""updates"""
#added Debug stuff
#condensed  if statements, cleaned up the code, shifted some spacers around to reduce text

"""Condense Menu if"""
#change if and elif statements to read out as 'if/elif menuSel in ("t", "/"")' instead of 'if (menuSel=="t")or(menuSel=="/")' and 'menuSel in ("*", "q")' instead of '(menuSel=="*")or(menuSel=="q")'
#change debug if and elif statements to read more like 'if menuSel=="11" and debug' instead of having it nested in another if statement under the else statement and using '==True' becasues apparently you don't need that all the time


"""debug outline"""
#Done-main menu 1: lsit modules for character generation
#Done-Char Gen Menu 1: lsit modules for character generation
#Done-Char Gen Menu 2: Values for Dice Rolls
#UDone-tilities 1 Debug