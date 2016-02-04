#imports the command for generating random numbers
from random import randint

"""Rule Placeholders"""
class attributeRolls(object):
	ruleCheck=False
	def __init__(self):
		self.checkName="Dice"


'''rule check method goes here'''
def rulecheck(s):
	if s.ruleCheck == True:
		ruleCheck = True
		return print("%s Rules: Present" % s.checkName)
	elif s.ruleCheck == False:
		return print("%s Rules: Not Present please select" % s.checkName)


#'''config file check goes here'''


'''Rules for attribute rolls'''
class attributeRolls(object):
	'''sets the rule toggle to True so that the system will know that the rule has been loaded'''
	ruleCheck=True
	def __init__(self):
		self.checkName="Dice"
		pass


'''welcome message'''		
print("---Welcome to the prototype---")


print("")
"""Rule Checks"""
dice = attributeRolls()
rulecheck(dice)

	

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
	else:
		print("Please try again")
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




