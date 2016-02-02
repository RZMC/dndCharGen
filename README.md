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
  1. Appearance
    1. preform dice rolls disregarding lowest and creating 6 lists of the three highest rolls for each set of rolls
    2. requires a RULE file with all the relevant information, some GMs/DMs may want to change it up so at least 3 tables should be made with comments
    3. should request rule file if none is present so player does not have
    4. basic table, 6 sets of rolls, 4 rolls per set, drop lowest in each set, single mulligan option rule should be present
    5. same as above, no mulligan
    6. same as first table, reroll die on 1
    7. probably list current rules like "Mulligan: none" and "reroll lowest" just so peopel know what is goign on
  2. Attribute Roll, selection, and modifiers
  3. Class

###Utilities
1. Import Rules and Tables
  1. import files for character gen rules and reference tables
  2. should probably have a submenu or be split amongst utilities
  3. may want to have visual aid
  4. should probably have a config setting to automatically import rules and tables

###Options



# current tasks
create basic 4d6 roll code for ren'py

edit mark 02-02-16
