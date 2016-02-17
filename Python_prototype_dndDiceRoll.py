'''imports the command for generating random numbers'''
from random import randint

print()
print("==========Program Start==========")
print()

print()
print("==========Checking Modules==========")
print()

"""Rule and Table Placeholders"""
class attributeRolls(object):
	ruleCheck=False
	def __init__(self):
		self.checkName="Dice"
class raceRules(object):
	ruleCheck=False
	def __init__(self):
		self.checkName="Race"

'''config file check that handles imports goes here'''
#from pp_module_diceRule import attributeRolls
from pp_module_diceRule import dice
#'''importing like in the following line does not work except for singular instances, just for reference'''
#import pp_module_diceRule

dice.statRolls()

print()



'''rule check method goes here, referenced later for checks'''
def rulecheck(s):
	if s.ruleCheck == True:
		ruleCheck = True
		print("%s Rules Status =" % s.checkName, s.ruleCheck)
		return print("%s Rules Status: Present" % s.checkName)
	elif s.ruleCheck == False:
		print("%s Rules Status =" % s.checkName, s.ruleCheck)
		return print("%s Rules Status: Not Present please select" % s.checkName)



'''welcome message'''		
print("==========Welcome to the prototype==========")


print("")
"""Rule Checks"""
"""Referenced Immediately and as option 5 of overmenu"""
"""checks to make sure rule has been loaded by checking 'ruleCheck' variable in each class using 'rulecheck' method created earlier in the prototype main file"""
def ruleCheckList():
	rulecheck(dice)
	rulecheck(raceRules())
	return

ruleCheckList()
print("")


#overmenu function
def overmenu():
	print("Please make a selection")
	print("(1) Character Generation")
	print("(2) Utilities")
	print("(3) Options")
	print("(4) Quit Program")

	menu1 =input()

	if menu1 == "1":
		print("You selected %s Character Generation" % menu1)
		#character Generation
		#needs several options
		#option-1 is appearance
		#option-2 is dice rolls
		charGenMenu = input()


		pass
	elif menu1 == "2":
		print("You selected %s Utilities" % menu1)
		#Utilities
		pass
	elif menu1 == "3":
		print("You selected %s Options" % menu1)
		#Options
		pass
	elif menu1 == "4":
		print("You selected %s Exit Program" % menu1)
		return quit()
		#Exit Program
	elif menu1 == "5":
		print("You selected %s Check Imports" % menu1)
		print()
		ruleCheckList()
		print()
		return overmenu()
		#Exit Program
	else:
		print()
		print("Invalid selection please try again")
		print()
		return overmenu()

def charGen_diceRollBasic():
	#this is where dice rolls and the handling of said dice rolls goes
	#needs 6 sets of 4d6 rolls
	#needs to drop the lowest for each set
	#needs to output each set to a list of three rolls within a list of 6 sets
	#needs Mulligan option where all 6 sets are rerolled but can only be run one time
	pass

def quit():
	input("Press Enter to close the program")

overmenu()

input("Nothing left to run, press Enter to close the program")




