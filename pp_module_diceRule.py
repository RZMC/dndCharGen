from random import randint
'''Custom Variables, this is where you adjust the module for personal use'''
number_of_sides_on_die=6
die_number_per_set=4
sets_of_dice_rolls=6
lowest_possible_roll=1
#reroll Die =
#Drop Lowest =
moduleName="Dice Module"
#moduleName="The Lusty Orc Dice Module"
'''Rules for attribute rolls, Do not alter anything past this line'''
class attributeRolls(object):
	'''sets the rule toggle to True so that the system will know that the rule has been loaded'''
	ruleCheck=True
	def __init__(self, die_sides, die_number, die_sets):
		self.checkName=moduleName
		"""sets the module name"""
		self.dSides=die_sides
		"""sets the number of sides on a die"""
		self.dSetNumber=die_number
		"""sets the number of dice rolled per die set"""
		self.dSets=die_sets
		"""sets the number of totl die sets rolled"""
		self.rollSets=["", "No dice have been rolled"]
		"""set's the self.rollSets list to empty so the program does not freak out if statRollsDisplay is called"""
		self.droppedSets=["", ""]
		self.rolledAttributes=["", ""]
		self.batch=0
		'''sets number of dice batch rolls to zero'''
	def moduleCheck(self):
		print("//run module Check start//\nnumber of sides on each die = %s\nnumber of die in a set = %s\nnumber of die sets = %s\n//run module Check complete//\n" % (self.dSides, self.dSetNumber, self.dSets))
	def statRolls(self):
		"""this is the method that is called to roll attribute values for a character for the first time, DND3.5 default is 6 sets of 4 rolls of 6 sided dice, however this is designed so that can be adjusted"""
		#'''clears lists'''
		self.rollSets=[]
		self.droppedSets=[]
		self.rolledAttributes=[]
		"""creats the Top Set Container that will house all of the sets or if it exists zeroes out the values"""
		for s in range(self.dSets):
			"""creates Recursion loop that ends after a number of times equal to sets_of_dice_rolls variable"""
			#'''creates lsits and sets them to clear'''
			rolls=[]
			dropped=[]
			"""while the rollSets recursion loop is running a roll container is set to empty so that values can be added to it"""
			for r in range(self.dSetNumber):
				"""creates another recursion loop that runs for as many times as die_number_per_set and addes a random number roll to rolls and dropped lists using the x variable"""
				x=(randint(lowest_possible_roll, self.dSides))
				rolls.append(x)
				dropped.append(x)
				"""adds to theresult of a roll that starts at 1 and ends at the value of number_of_sides_on_die to the rolls set container and the dropped set container after the lowest has been dropped"""
			self.rollSets.append(rolls)
			dropped.remove(min(dropped))
			self.droppedSets.append(dropped)
			"""after the rolls are done, normally 4 of them, the set is added to the rollSets variable container as well as adding to the dropped sets container and adding to the batcch number"""
		self.batch+=1
		print("\nnumber of batch attempts:"+str(self.batch)+"\nStat Rolls")
		"""after all of the sets have been added to the set container the sets are printed out, the following 3 lines make it print the sets vertically"""
		for rs in range(len(self.rollSets)): 
			at=0
			for rls in range(len(self.droppedSets[rs])):
				at+=self.droppedSets[rs][rls]
			self.rolledAttributes.append(at)
			print((self.rollSets[rs]), (self.rolledAttributes[rs]))
		print("")
	def displayStatResults(self):
		"""This method when called will print the results of the rollSets and the sum of the three highest rolls, or it will state that no rolls have been made"""
		print("\nbatch attempt:"+str(self.batch)+"\nStat Rolls")
		for rs in range(len(self.rollSets)):
			print((self.rollSets[rs]), (self.rolledAttributes[rs]))
		print("")
		return
		#each set contains the three highest rolls after 4 rolls
		#should end up with6 sets of 3 dice rolls
		#may as well just add them and produce the total to save on list coding but still print the results of the rolls
dice=attributeRolls(number_of_sides_on_die, die_number_per_set, sets_of_dice_rolls)


'''needs equation to produce modifiers, check for divite by 2, cant just subtract by 10'''
'''statRolls and displayStatRolls still needs dynamic reroll for lowest or threshhold, drop lowest and totaling that will print out next to the set rolls like "[3, 4, 3, 4] 1" or something, maybe attribute modifiers too'''
'''Also Manual input with a statement that says they were manually input'''
'''probably number of times rolled statement too for mulligans until I can figure out some good mulligan rules'''

'''focus on a container for attributes that can be assigned to individual attributes'''
'''something like score1 - score6 where each set of rolls assigns score(number) in a for statement'''
'''needs variables for names of attributes'''
'''then a method to assign attributes to the respective names'''