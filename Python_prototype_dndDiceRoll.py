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

def quit():
	input("Press Enter to close the program")

overmenu()
input("Nothing left to run, press Enter to close the program")