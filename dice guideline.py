#dice guideline
from random import randint


#FOR program module
moduleName="Dice Module"
#moduleName="The Lusty Orc Dice Module"

#FOR dice rolls
#mulligan_yes_or_no=True not implemented
#the_number_of_dice_roll_sets_in_a_batch=6 not implemented
the_number_of_rolls_in_a_set=4
the_number_of_sides_on_a_die=6
the_lowest_possible_roll=1
reroll_if_equal_or_less=5
number_of_lowest_rolls_to_drop_in_a_set=1
number_of_highest_rolls_to_drop_in_a_set=1


#Rules for attribute rolls, Do not alter anything past this line




"""NEEDS SINGLE ROLL MULLIGANS"""










'''
def dicerollbatch():
	WorkingBatch=[]

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

'''















''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#test_4_rolls_print
from random import randint

The_number_of_rolls_in_a_set=4
The_number_of_sides_on_a_die=6
the_lowest_possible_roll=1

#the followign 6 lines of code roll 4 numbers between 1 and 6 and then prints them out vertically
def roll_set_of_dice():
	for roll in range(The_number_of_rolls_in_a_set): 
		roll_result=(randint(the_lowest_possible_roll, The_number_of_sides_on_a_die))
		print("%s" % roll_result)
	return
#roll_set_of_dice()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#test_4_rolls_output_to_list_print_list
from random import randint

the_number_of_rolls_in_a_set=4
the_number_of_sides_on_a_die=6
the_lowest_possible_roll=1

#the following 8 lines of code rolls 4 6 sided dice and copies the reuslts to a lsit and then print's the list
def roll_set_of_dice():
	set_of_dice_rolls=[]
	for roll in range(the_number_of_rolls_in_a_set): 
		roll_result=(randint(the_lowest_possible_roll, the_number_of_sides_on_a_die))
		set_of_dice_rolls.append(roll_result)
	print(set_of_dice_rolls)
	return
#roll_set_of_dice()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#test_4_rolls with reroll and output
from random import randint

the_number_of_rolls_in_a_set=4
the_number_of_sides_on_a_die=6
the_lowest_possible_roll=1
reroll_if_equal_or_less=5

#rolls 4 dice between 1 and 6 and rerolls all results that are 5 or less then outputs them to roll_set_of_dice
def roll_set_of_dice():
	set_of_dice_rolls=[]
	for roll in range(the_number_of_rolls_in_a_set): 
		roll_result=(randint(the_lowest_possible_roll, the_number_of_sides_on_a_die))
		while roll_result<=reroll_if_equal_or_less:
			roll_result=(randint(the_lowest_possible_roll, the_number_of_sides_on_a_die))
			print("reroll %s" %roll_result)
		else:set_of_dice_rolls.append(roll_result)
	print(set_of_dice_rolls)
	return
#roll_set_of_dice()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#test_4_rolls if drop lowest or highest is greater than zero copy set_of_dice_rolls to adjusted_set_of_dice_rolls
from random import randint

the_number_of_rolls_in_a_set=4
the_number_of_sides_on_a_die=6
the_lowest_possible_roll=1
reroll_if_equal_or_less=0
number_of_lowest_rolls_to_drop_in_a_set=1
number_of_highest_rolls_to_drop_in_a_set=0

#rolls 4 dice between 1 and 6 and rerolls all results that are 5 or less then outputs them to roll_set_of_dice
def roll_set_of_dice():
	set_of_dice_rolls=[]
	adjusted_set_of_dice_rolls=[]
	for roll in range(the_number_of_rolls_in_a_set): 
		roll_result=(randint(the_lowest_possible_roll, the_number_of_sides_on_a_die))
		while roll_result<=reroll_if_equal_or_less:
			roll_result=(randint(the_lowest_possible_roll, the_number_of_sides_on_a_die))
			print("reroll %s" %roll_result)
		else:set_of_dice_rolls.append(roll_result)
	if (number_of_lowest_rolls_to_drop_in_a_set>0) or (number_of_highest_rolls_to_drop_in_a_set>0):
		for roll_results in range(len(set_of_dice_rolls)):
			adjusted_set_of_dice_rolls.append(set_of_dice_rolls[roll_results])
		print(adjusted_set_of_dice_rolls)
	print(set_of_dice_rolls)
	return
#roll_set_of_dice()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#test_4_rolls drop highest and lowest
from random import randint

the_number_of_rolls_in_a_set=4
the_number_of_sides_on_a_die=6
the_lowest_possible_roll=1
reroll_if_equal_or_less=0
number_of_lowest_rolls_to_drop_in_a_set=1
number_of_highest_rolls_to_drop_in_a_set=1

#rolls 4 dice between 1 and 6 and rerolls all results that are 5 or less then outputs them to roll_set_of_dice
def roll_set_of_dice():
	set_of_dice_rolls=[]
	adjusted_set_of_dice_rolls=[]
	for roll in range(the_number_of_rolls_in_a_set): 
		roll_result=(randint(the_lowest_possible_roll, the_number_of_sides_on_a_die))
		while roll_result<=reroll_if_equal_or_less:
			roll_result=(randint(the_lowest_possible_roll, the_number_of_sides_on_a_die))
			print("reroll %s" %roll_result)
		else:set_of_dice_rolls.append(roll_result)
	for roll_results in range(len(set_of_dice_rolls)):
		adjusted_set_of_dice_rolls.append(set_of_dice_rolls[roll_results])
	print("\n////Break////\n%s\n%s\n////Break////\n" % (set_of_dice_rolls, adjusted_set_of_dice_rolls))
	if (number_of_lowest_rolls_to_drop_in_a_set>0) or (number_of_highest_rolls_to_drop_in_a_set>0):
		if number_of_lowest_rolls_to_drop_in_a_set>0:
			drop_counter=0
			drop_counter+=number_of_lowest_rolls_to_drop_in_a_set
			#print(adjusted_set_of_dice_rolls)
			#print(drop_counter)
			while drop_counter>0:
				adjusted_set_of_dice_rolls.remove(min(adjusted_set_of_dice_rolls))
				#print(adjusted_set_of_dice_rolls)
				drop_counter-=1
				#print(drop_counter)
		if number_of_highest_rolls_to_drop_in_a_set>0:
			drop_counter=0
			drop_counter+=number_of_highest_rolls_to_drop_in_a_set
			#print(adjusted_set_of_dice_rolls)
			#print(drop_counter)
			while drop_counter>0:
				adjusted_set_of_dice_rolls.remove(max(adjusted_set_of_dice_rolls))
				#print(adjusted_set_of_dice_rolls)
				drop_counter-=1
				#print(drop_counter)
	print("\n////Break////\n%s\n%s\n////Break////\n" % (set_of_dice_rolls, adjusted_set_of_dice_rolls))
	return
roll_set_of_dice()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''