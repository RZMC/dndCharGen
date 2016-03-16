#main file, run this one
print("\n==========Program Start==========")
#checks version and fixes raw_input for python 3 makign the code run on both 2.x and 3.x
import sys
if sys.version[0]=="3": raw_input=input
#imports the command for generating random numbers
from random import randint
#sets global/common variable Lines and zeroing
debug=False
invalid=("Invalid selection please try again")
plsEn="Please enter an option:"
blank=""
print("\n==========Checking Modules==========")
#Rule and table placeholder base, sets the false value for class objects that have nto been loaded, states when the user attempts to use a module that is not loaded by name
class nomod(object):
	ruleCheck=False
	def n(self):
		print("\nNo %s Module Loaded" % str(self.moduleName))
		return
#Rule and Table Placeholders
#this needs serious fixing, charmenu needs to become more dynamic so I can get rid of a lot of these placeholders
class attributeRolls(nomod):
	def __init__(self):self.moduleName="Dice Module"
	def moduleCheck(self):return self.n()
	def statRolls(self):return self.n()
	def displayStatResults(self):return self.n()
dice=attributeRolls()
class raceRules(nomod):
	def __init__(self):self.moduleName="Race Module"
race=raceRules()
#this is where a config file check that handles imports would go, IF I HAD ONE
from pp_module_diceRule import dice
#from pp_module_raceRule import race
#rule check method goes here, referenced later for checks
print("\n==========Setting up Menus==========")
def rulecheck(s):
	if s.ruleCheck:
		ruleCheck=True
		print("%s Rules: Present and %s." % (s.moduleName, s.ruleCheck))
		return
	else:
		print("%s Rules: Not Present and %s, please select" % (s.moduleName, s.ruleCheck))
		return
	#"""Rule Checks"""
	#"""Referenced Immediately and as option 5 of overmenu"""
	#"""checks to make sure rule has been loaded by checking 'ruleCheck' variable in each class using 'rulecheck' method created earlier in the prototype main file"""
def ruleCheckList():
	rulecheck(dice)
	rulecheck(race)
	return blank




def charmenu(cReadout):
	#debug Options
	cDebug1=""
	cDebug2=""
	if debug:
		cDebug1="+[11] Check Character Generation Modules\n"
		cDebug2="+[12] Check Character Generation Modules\n"
	#header
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n==========Character Generation==========\n")
	#readout for char
	if cReadout==999:print(invalid)
	elif cReadout==1:dice.displayStatResults()
		#cReadout 1 needs to be expanded to display all current character information
	elif cReadout==2:dice.statRolls()
	elif cReadout==11:ruleCheckList()
	elif cReadout==12:print(dice.moduleCheck())
	else:print("")
	#options list, it references debug options
	print("\n[1] Display Current Character Information\n%s%s[2] Roll for Attributes\n[/] or [t] Main Menu\n[*] or [q] Quit Program" % (cDebug1, cDebug2))
	#CharMenu input
	menuSel=raw_input(plsEn)
	if menuSel in("t","/"):return mainmenu(0)
	elif menuSel=="1": return charmenu(1)
	elif menuSel=="2":return charmenu(2)
	elif menuSel in ("*", "q"):return quit()
	#CharMenu Debug Options
	elif menuSel=="11" and debug:return charmenu(11)
	elif menuSel=="12" and debug:return charmenu(12)
	#Return invalid entry
	else:return charmenu(999)
	#needs appearance option
	#needs inventory option
	#-needs to be dynamic with a setting for number of descriptors (name, weight, description etc.)
	#-should use dictionary for each entry
	#-entry zero should have the descriptor names like name, weight, description




def utilitymenu(uReadout):
	"""the following line checks the global debug variable so it doesn't freak out for usign a variable not defined in the function"""
	global debug
	#header
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n==========Utilities==========\n")
	#readout for utility
	if uReadout==999:print(invalid)
	else:print("")
	#debug status
	if debug:print("\nDebug Options: Active\n")
	else:print("\nDebug Options: Inactive\n")
	#options list
	print("[1] Toggle Debug\n[/] or [t] Main Menu\n[*] or [q] Quit Program")
	#menu input for utility
	menuSel=raw_input(plsEn)
	if menuSel in("t","/"):return mainmenu(0)
	elif menuSel=="1":
		if debug:debug=False
		else:debug=True
		return utilitymenu(0)
	elif menuSel in ("*", "q"):return quit()
	else:return utilitymenu(999)




def optionsmenu(oReadout):
	#header
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n==========Options==========\n")
	#readout for options
	if oReadout==999:print(invalid)
	else:print("")
	#Options list
	print("\n[/] or [t] Main Menu\n[*] or [q] Quit Program")
	#menu input for options
	menuSel=raw_input(plsEn)
	if menuSel in("t","/"):return mainmenu(0)
	elif menuSel in ("*", "q"):return quit()
	else:return optionsmenu(999)




def mainmenu(mReadout):
	#debug readouts
	mDebug1=""
	if debug:mDebug1="+[11] Check Character Generation Modules\n"
	#header
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n==========Main Menu==========\n")
	#readout for main
	if mReadout==999:print(invalid)
	elif mReadout==11:ruleCheckList()
	elif mReadout==991:print("%s\n%s" % (ruleCheckList(), dice.moduleCheck()))
	else:print("")
	#Options list, it references debug options
	print("\n[1] Character Generation\n%s[2] Utilities\n[3] Options\n[*] or [q] Quit Program" % (mDebug1))
	#menu input for main
	menuSel=raw_input(plsEn)
	if menuSel in("t","/"):return mainmenu(0)
	elif menuSel=="1":return charmenu(0)
	elif menuSel=="2":return utilitymenu(0)
	elif menuSel=="3":return optionsmenu(0)
	#mainmenu debug inputs
	elif menuSel=="11" and debug:return mainmenu(11)
	elif menuSel in ("*", "q"):return quit()
	#Return invalid entry
	else:return mainmenu(999)




#may use this if I wish to avoid globals
#def startmenu():
	#mainmenu(debug, readout)




def quit():raw_input("\nQuitting Program\nPress Enter to close the program")

mainmenu(991)

raw_input("Nothing left to run, press Enter to close the program")

"""updates 030916"""
#added Debug stuff
#condensed  if statements, cleaned up the code, shifted some spacers around to reduce text

"""update 031016"""
#cleaned up a bunch of code because it seemed sloppy an unorganized to me leading me sicne I ahd a hard time reading it

"""update 031516"""
#I decided my dice rolling code was garbage and started rewriting it and may move it to the primary module when it's done

"""Condense Menu if"""
#change if and elif statements to read out as 'if/elif menuSel in ("t", "/"")' instead of 'if (menuSel=="t")or(menuSel=="/")' and 'menuSel in ("*", "q")' instead of '(menuSel=="*")or(menuSel=="q")'
#change debug if and elif statements to read more like 'if menuSel=="11" and debug' instead of having it nested in another if statement under the else statement and using '==True' becasues apparently you don't need that all the time


"""debug outline"""
#Done-main menu 1: lsit modules for character generation
#Done-Char Gen Menu 1: lsit modules for character generation
#Done-Char Gen Menu 2: Values for Dice Rolls
#UDone-tilities 1 Debug

"""importing info"""
#importing as in the following line does not work except for singular instances, just for reference
#import pp_module_diceRule