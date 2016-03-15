#test_4_rolls
from random import randint

the_number_of_rolls_in_a_set=4
the_number_of_sides_on_a_die=6
the_lowest_possible_roll=1
reroll_if_equal_or_less=0
number_of_lowest_rolls_to_drop_in_a_set=0
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
	for roll_results in range(len(set_of_dice_rolls)):
		adjusted_set_of_dice_rolls.append(set_of_dice_rolls[roll_results])
	print("\n////Break////\n%s\n%s\n////Break////\n" % (set_of_dice_rolls, adjusted_set_of_dice_rolls))
	if (number_of_lowest_rolls_to_drop_in_a_set>0) or (number_of_highest_rolls_to_drop_in_a_set>0):
		if number_of_lowest_rolls_to_drop_in_a_set>0:
			drop_counter=0
			drop_counter+=number_of_lowest_rolls_to_drop_in_a_set
			while drop_counter>0:
				adjusted_set_of_dice_rolls.remove(min(adjusted_set_of_dice_rolls))
				drop_counter-=1
		if number_of_highest_rolls_to_drop_in_a_set>0:
			drop_counter=0
			drop_counter+=number_of_highest_rolls_to_drop_in_a_set
			while drop_counter>0:
				adjusted_set_of_dice_rolls.remove(max(adjusted_set_of_dice_rolls))
				drop_counter-=1
	print("\n////Break////\n%s\n%s\n////Break////\n" % (set_of_dice_rolls, adjusted_set_of_dice_rolls))
	return
roll_set_of_dice()