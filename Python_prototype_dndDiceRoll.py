print("Welcome to the prototype")

#overmenu
def overmenu():
	print("Please make a selection")
	print("(1) Character Generation")
	print("(2) Utilities")
	print("(3) Options")
	print("(4) Quit Program")

	menu1 =input()
	print("you entered %s" % menu1)

	if menu1 == "1":
		#character Generation
		#needs several options
		#option-1 is appearance
		#option-2 is dice rolls
		charGenMenu = input()

		pass
	elif menu1 == "2":
		#Utilities
		pass
	elif menu1 == "3":
		#Options
		pass
	elif menu1 == "4":
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


def quit():
	input("Press Enter to close the program")

overmenu()
input("Nothing left to run, press Enter to close the program")