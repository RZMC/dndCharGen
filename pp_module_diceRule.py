from random import randint
'''Custom Variables, this is where you adjust the module for personal use'''

die_sides = 6
die_number_per_set = 4
sets_of_dice_rolls = 6

moduleName = "Dice Module (with flavor text)"

'''Rules for attribute rolls, Do not alter anythign past this line'''
class attributeRolls(object):
	'''sets the rule toggle to True so that the system will know that the rule has been loaded'''
	ruleCheck=True
	def __init__(self, die_number, die_sides):
		self.checkName = moduleName
		self.number = die_number_per_set
		self.dSides = die_sides
		self.sets = sets_of_dice_rolls
	def statRolls(self):
		print("2 placeholder")
		sets = []
		for s in range(self.sets):
			rolls = []
			for r in range(self.number):
				rolls.append(randint(1, self.dSides))
			sets.append(rolls)
		print(sets)
		pass
		#list with 6 sets
		#each set contains the three highest rolls after 4 rolls
		#should end up with6 sets of 3 dice rolls
		#may as well jsut add them and produce the total to save on list coding but still print the results of the rolls
dice = attributeRolls(die_number_per_set, die_sides)
#print("%s imported" % moduleName)
#print("%s check = %s" % (moduleName, attributeRolls.ruleCheck))
print("sides = %s" % dice.number)
print("faces = %s" % dice.dSides)