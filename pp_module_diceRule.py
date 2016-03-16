#this file is explicitly for rolling dice
from random import randint
'''Custom Variables, this is where you adjust the module for personal use'''
number_of_sides_on_die=6
die_number_per_set=4
sets_of_dice_rolls=6
lowest_possible_roll=1
#mulligan_yes_or_no=True not implemented
#reroll Die= not implemented
#Drop Lowest= not implemented
moduleName="Dice Module"
#moduleName="The Lusty Orc Dice Module"
#Rules for attribute rolls, Do not alter anything past this line
class attributeRolls(object):
	#sets the rule toggle to True so that the program will know that the rule has been loaded
	ruleCheck=True
	#sets the module name, the number of die sides, number rolled per set, total die sets rolled and the lists to empty so the program does not freak out and then sets the set batch number to 0
	def __init__(self, die_sides, die_number, die_sets):
		self.moduleName=moduleName
		self.dieSides=die_sides
		self.setDieNumber=die_number
		self.dieSets=die_sets
		self.rollBatch=["", "No dice have been rolled"]
		self.droppedBatch=["", ""]
		self.attributeResults=["", ""]
		self.batch=0
	def moduleCheck(self):return ("//run module Check start//\nnumber of sides on each die = %s\nnumber of die in a set = %s\nnumber of die sets = %s\n//run module Check complete//" % (self.dieSides, self.setDieNumber, self.dieSets))
	#this is the method that is called to roll attribute values for a character for the first time, DND3.5 default is 6 sets of 4 rolls of 6 sided dice, however this is designed so that can be adjusted
	def statRolls(self):
		#creats and clears lists at start of stat generation the Top Set Container that will house all of the sets or if it exists zeroes out the values
		self.rollBatch=[]
		self.droppedBatch=[]
		self.attributeResults=[]

		#creates Recursion loop that ends after sets_of_dice_rolls number of times, each time creating and clearing sub lists
		for setNumber in range(self.dieSets):
			rolls=[]
			dropped=[]
			#creates another recursion loop that runs for die_number_per_set times and addes a random roll result to the rolls and dropped lists using the x variable, each roll is between the values lowest_possible_roll and number_of_sides_on_die
			for roll in range(self.setDieNumber):
				r=(randint(lowest_possible_roll, self.dieSides))
				rolls.append(r)
				dropped.append(r)
			#after the rolls are done, normally 4 of them, the set is added to the rollBatch variable container as well as adding to the dropped sets container
			self.rollBatch.append(rolls)
			dropped.remove(min(dropped))
			self.droppedBatch.append(dropped)


		#after the roll sets have been added to the batch the batch count is incremented up one
		self.batch+=1


		#after the numbers have been generated and appended to the batch the sets are printed out vertically
		print("number of batch attempts:"+str(self.batch)+"\nStat Rolls")
		for batchSets in range(len(self.rollBatch)): 
			at=0
			for batchRolls in range(len(self.droppedBatch[batchSets])):at+=self.droppedBatch[batchSets][batchRolls]
			self.attributeResults.append(at)
			print((self.rollBatch[batchSets]), (self.attributeResults[batchSets]))
	#This method when called will print the results of the rollBatch and the sum of the three highest rolls, or it will state that no rolls have been made
	def displayStatResults(self):
		print("batch attempt:"+str(self.batch)+"\nStat Rolls")
		for batch_result_Item in range(len(self.rollBatch)):print((self.rollBatch[batch_result_Item]), (self.attributeResults[batch_result_Item]))
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

"""Update 03-10-16"""
#changed variable and list parts so I could look at it and understand what my own code was saying because I forgot and could barely follow
#changed the comments because the """ and ''' comments in bright yellow were making it hard for me to see the actual code, also condensed the comments