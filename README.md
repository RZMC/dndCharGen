# dndCharGen
Renpy dnd3.5 character generator, I don't know what I'm doing

I will add to the outline as I go

# Outline

Over Menu
  #create a main menu that accesses the submenues
1 Character Gen
  #menu specificly for character generation, if the tables have not been loaded it should request basic tables
  (1a) Appearance
    #preform dice rolls disregarding lowest and creating 6 lists of the three highest rolls for each set of rolls
    #requires a RULE file with all the relevant information, some GMs/DMs may want to change it up so at least 3 tables should be made with comments
    #should request rule file if none is present so player does not have
      #basic table, 6 sets of rolls, 4 rolls per set, drop lowest in each set, single mulligan option rule should be present
      #same as above, no mulligan
      #same as first table, reroll die on 1
    #probably list current rules like "Mulligan: none" and "reroll lowest" just so peopel know what is goign on
(1b) Attribute Roll, selection, and modifiers
(1c) Class
2 Utilities
(2a) Import Rules and Tables
  #import files for character gen rules and reference tables
  #should probably have a submenu or be split amongst utilities
  #may want to have visual aid
  #should probably have a config setting to automatically import rules and tables
3 Options


# current tasks
create basic 4d6 roll code for ren'py

edit mark 02-02-16
