# dndCharGen
Renpy dnd3.5 character generator, I don't know what I'm doing

##Goals
1. Visually represented in Ren'py
2. Preforms all char gen functions with limited hand holding and the ability to go back and change decisions like which stats go where and removal of gear after adding it on
3. avoid getting taken down by having all the licensed content be absent from the code and simply written up by users and imported as needed, like gear tables and class growth

I will add to the outline as I go

# Outline

##Over Menu

create a main menu that accesses the submenues
  
###Character Gen
  menu specificly for character generation, if the tables have not been loaded it should request basic tables
  1.Display Current Character Information
  2. Attribute Roll, selection, and modifiers
    1. be able to preform a single dice roll, a set of dice rolls or multiple sets of dice rolls.
    2. be able to set highest possible roll per die and lowest possible roll
    3. be able to disregard between 0 and all dice rolls, just because for the dynamicness of it
    4. be able to toggle mulligans on and off
    5. mulligans sould have a counter that can be toggled that counts the total ammoutn of tiems mulligans have been rolled
    6. requires a RULE file with all the relevant information, some GMs/DMs may want to change it up so at least 3 tables should be made with comments
    7. should request rule file if none is present so player does not have
    8. default table, 6 sets of rolls, 4 rolls per set, drop lowest in each set, mulligan on and mulligan counter on
    9. probably list current rules like "Mulligan: none" and "reroll lowest" just so peopel know what is going on
    10. Option to display current rolls
  3. Appearance
    1. Sex
    2. Race
      1. attribute modifiers from race, must be compatable with attribute table
      2. abilities from race as descriptive text
    3. body features
      1. hair color
      2. eye color
      3. skin color
      4. age
  4. Class
    1. Feats
    2. Spells
  5. Equipment(this needs to have a common item programming class where certain attributes are shared)
    1. Weapon attributes
      1. Common, Name
      2. Common, Weight
      3. Common, Description
      4. Common, Value
      5. Weapon, Attack Hit
      6. Weapon, Attack Damage
      7. Weapon, Damage Type
      8. Weapon, Finesse (True, False)
    2. Armor Attributes
      1. Common, Name
      2. Common, Weight
      3. Common, Description
      4. Common, Value
      5. Armor, defense
      6. Armor, Weight Class (light, medium, heavy)
    3. Misc Attributes
      1. Common, Name
      2. Common, Weight
      3. Common, Description
      4. Common, Value
      5. 
  5. 

###Utilities
1. Import Rules and Tables
  1. import files for character gen rules and reference tables
  2. should probably have a submenu or be split amongst utilities
  3. may want to have visual aid
  4. should probably have a config setting to automatically import rules and tables
  5. Debug Toggle(Probably belongs in options now that I think about it)

###Options



# current tasks
create basic 4d6 roll code for ren'py

edit mark 03-15-16
