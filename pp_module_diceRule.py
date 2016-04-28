
'''Custom Variables, this is where you adjust the module for personal use'''
the_lowest_possible_roll=2
the_highest_possible_roll=6
the_number_of_rolls_in_a_set=4
the_number_of_sets_of_dice_rolls=6
reroll_if_equal_or_less=0
number_of_lowest_rolls_to_drop_in_a_set=1
number_of_highest_rolls_to_drop_in_a_set=0
minimum_average_attribute_or_else_reroll=3
#raising minimum_average_attribute_modifier_or_else_reroll above 2.5 is not recomended with Dungeons and Dragons stat rolls and with default recursion limit will crash the program
minimum_average_attribute_modifier_or_else_reroll=1

#mulligan_yes_or_no=True not implemented
moduleName="Dice Module"
#moduleName="The Lusty Orc Bride Dice Module"
"""Rules for attribute rolls, Do not alter anything past this line"""
#imports the command for generating random numbers
from random import randint
#import sys
#sys.setrecursionlimit(10000)
class attributeRolls(object):
	#sets the rule toggle to True so that the program will know that the rule has been loaded
	ruleCheck=True
	#sets the module name, the number of die sides, number rolled per set, total die sets rolled and the lists to empty so the program does not freak out and then sets the set batch number to 0
	def __init__(self, lowest_roll, die_sides, die_number, die_sets, reroll_die, low_drop, high_drop, att_avg, mod_avg):
		self.moduleName=moduleName
		self.the_lowest_possible_roll=lowest_roll
		self.the_highest_possible_roll=die_sides
		self.the_number_of_rolls_in_a_set=die_number
		self.the_number_of_sets_of_dice_rolls=die_sets
		self.reroll_if_equal_or_less=reroll_die
		self.number_of_lowest_rolls_to_drop_in_a_set=low_drop
		self.number_of_highest_rolls_to_drop_in_a_set=high_drop
		self.minimum_average_attribute_or_else_reroll=att_avg
		self.minimum_average_attribute_modifier_or_else_reroll=mod_avg
		self.attribute_average=0
		self.attribute_modifier_average=0
		self.list_of_roll_set_results=[""]
		self.list_of_roll_set_results_adjusted=[""]
		self.attribute_results=["No dice have been rolled"]
		self.attribute_results_modifier=[""]
		self.batch=0

	def moduleCheck(self):return ("//run module Check start//\nlowest possible roll =%s\nhighest possible roll = %s\nnumber of die rolled in a set = %s\nnumber of die sets rolled = %s\nreroll if less than or equal to = %s\nnumber of lowest rolls in a set to drop =%s\nnumber of highest rolls in a set to drop = %s\nlowest possible modifier average =%s\n//run module Check complete//" % (self.the_lowest_possible_roll, self.the_highest_possible_roll, self.the_number_of_rolls_in_a_set, self.the_number_of_sets_of_dice_rolls, self.reroll_if_equal_or_less, self.number_of_lowest_rolls_to_drop_in_a_set, self.number_of_highest_rolls_to_drop_in_a_set, self.minimum_average_attribute_modifier_or_else_reroll))

	def roll_set_of_dice(self):
		self.set_of_dice_rolls=[]
		self.set_of_dice_rolls_adjusted=[]
		for roll in range(the_number_of_rolls_in_a_set): 
			roll_result=(randint(the_lowest_possible_roll, the_highest_possible_roll))
			while roll_result<=reroll_if_equal_or_less:
				roll_result=(randint(the_lowest_possible_roll, the_highest_possible_roll))
				print("reroll %s" %roll_result)
			else:self.set_of_dice_rolls.append(roll_result)
		for roll_results in range(len(self.set_of_dice_rolls)):
			self.set_of_dice_rolls_adjusted.append(self.set_of_dice_rolls[roll_results])
		if (self.number_of_lowest_rolls_to_drop_in_a_set>0) or (self.number_of_highest_rolls_to_drop_in_a_set>0):
			if self.number_of_lowest_rolls_to_drop_in_a_set>0:
				drop_counter=0
				drop_counter+=self.number_of_lowest_rolls_to_drop_in_a_set
				while drop_counter>0:
					self.set_of_dice_rolls_adjusted.remove(min(self.set_of_dice_rolls_adjusted))
					drop_counter-=1
			if self.number_of_highest_rolls_to_drop_in_a_set>0:
				drop_counter=0
				drop_counter+=self.number_of_highest_rolls_to_drop_in_a_set
				while drop_counter>0:
					self.set_of_dice_rolls_adjusted.remove(max(self.set_of_dice_rolls_adjusted))
					drop_counter-=1
		return

	def statRolls(self):
		self.list_of_roll_set_results=[]
		self.list_of_roll_set_results_adjusted=[]
		self.attribute_results=[]
		self.attribute_results_modifier=[]
		self.attribute_average=0
		self.attribute_modifier_average=0
		for set_count_number in range(self.the_number_of_sets_of_dice_rolls):
			self.roll_set_of_dice()
			self.list_of_roll_set_results.append(self.set_of_dice_rolls)
			self.list_of_roll_set_results_adjusted.append(self.set_of_dice_rolls_adjusted)
		for batchSets in range(len(self.list_of_roll_set_results)): 
			at=0
			at_mod=0
			for batchRolls in range(len(self.list_of_roll_set_results_adjusted[batchSets])):at+=self.list_of_roll_set_results_adjusted[batchSets][batchRolls]
			self.attribute_results.append(at)
			self.attribute_average+=at
			at-=10
			if at==0:at_mod=at
			elif at % 2 == 0: at_mod=at/2
			elif at % 2 == 1:at_mod=(at-1)/2
			else:return dice.statRolls()
			self.attribute_results_modifier.append(int(at_mod))
			self.attribute_modifier_average+=at_mod
		self.attribute_average/=self.the_number_of_sets_of_dice_rolls
		self.attribute_modifier_average/=self.the_number_of_sets_of_dice_rolls
		if self.attribute_average < self.minimum_average_attribute_or_else_reroll:return dice.statRolls()
		elif self.attribute_modifier_average < self.minimum_average_attribute_modifier_or_else_reroll:return dice.statRolls()
		else:
			self.batch+=1
			print("batch attempt:"+str(self.batch)+"\nStat Rolls with Modifiers")
			for batchSets in range(len(self.list_of_roll_set_results)):
				print("%s  %s |%s" %((self.list_of_roll_set_results[batchSets]), str(self.attribute_results[batchSets]).rjust(2), str(self.attribute_results_modifier[batchSets]).rjust(3)))
			print("Average Attribute Minimum %.2f/%s\nAverage Modifier Minimum %.2f/%s"%(self.attribute_average, str(self.minimum_average_attribute_or_else_reroll).rjust(2), self.attribute_modifier_average, str(self.minimum_average_attribute_modifier_or_else_reroll).rjust(2)))
			return

	def displayStatResults(self):
		print("batch attempt:"+str(self.batch)+"\nStat Rolls with Modifiers")
		for batch_result_Item in range(len(self.list_of_roll_set_results)):print("%s  %s |%s" %((self.list_of_roll_set_results[batch_result_Item]),str(self.attribute_results[batch_result_Item]).rjust(2), str(self.attribute_results_modifier[batch_result_Item]).rjust(3)))
		print("Average Attribute Minimum %.2f/%s\nAverage Modifier Minimum %.2f/%s"%(self.attribute_average, str(self.minimum_average_attribute_or_else_reroll).rjust(2), self.attribute_modifier_average, str(self.minimum_average_attribute_modifier_or_else_reroll).rjust(2)))
		return

	def displayCurrent(self):
		print("batch attempt:"+str(self.batch)+"\nStat Rolls with Modifiers")
		for batch_result_Item in range(len(self.list_of_roll_set_results)):print("%s |%s" %(str(self.attribute_results[batch_result_Item]).rjust(2), str(self.attribute_results_modifier[batch_result_Item]).rjust(3)))
		return

dice=attributeRolls(the_lowest_possible_roll, the_highest_possible_roll, the_number_of_rolls_in_a_set, the_number_of_sets_of_dice_rolls, reroll_if_equal_or_less, number_of_lowest_rolls_to_drop_in_a_set, number_of_highest_rolls_to_drop_in_a_set, minimum_average_attribute_or_else_reroll, minimum_average_attribute_modifier_or_else_reroll)


'''needs equation to produce modifiers, check for divite by 2, cant just subtract by 10'''
'''statRolls and displayStatRolls still needs dynamic reroll for lowest or threshhold, drop lowest and totaling that will print out next to the set rolls like "[3, 4, 3, 4] 1" or something, maybe attribute modifiers too'''
'''Also Manual input with a statement that says they were manually input'''
'''probably number of times rolled statement too for mulligans until I can figure out some good mulligan rules'''

'''focus on a container for attributes that can be assigned to individual attributes'''
'''something like score1 - score6 where each set of rolls assigns score(number) in a for statement'''
'''needs variables for names of attributes'''
'''then a method to assign attributes to the respective names'''

'''NEEDS toggle for attribut result and modifier result averages'''
"""NEEDS SINGLE ROLL MULLIGANS"""

"""Update 03-10-16"""
#changed variable and list parts so I could look at it and understand what my own code was saying because I forgot and could barely follow
#changed the comments because the """ and ''' comments in bright yellow were making it hard for me to see the actual code, also condensed the comments

"""Update 03-29-16"""
#replaced the current dice roll code with the tested roll code
#reworked the set roll code and added in modifiers
#changed the way Stat Results are displayed
#still need to rework the character generation menu to have a dice rolls sub menu with roll action, previous batch result list, current batch result list, toggle for attribut result and modifier result averages

"""Update 03-31-16"""
#Added option for minimum possible Attribute average
#Added option for minimum possible modifier average
#realized i had wasted space with shit code in the attribute modifier