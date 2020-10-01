from constants import term
import constants
import blessed
import text_handler
import ui
import battle
import mobs_lib
import inventory
import random
import maze_handler
import event_handler


     

# The event dictionary stores all game events in chronological order. k,v pairs are processed by the 'game_events' function in 'event_handler.py'
# 'Keys' in this dict are always numbers, in chronoligical order.
# Each key's 'value', is a tuple of 'values', in the format; function - parameters for that function, function - parameters for that function, and so on.
# The first 'value' in the tuple is a function call to whichever event type we currently want, i.e story text, 
# a battle, a choice to be made by the player etc. Lets call that the 'top level function'.
# 'Values' following the 'top level function' are fed to that function by the 'game_events' function in 'event_handler.py'.
# 'Values' following any other 'lower level function' in the tuple are fed to that function by the 'top level function'.
# As at 1/8/20 only the 'top level function' takes other function calls as arguments. 'lower level functions' only take parameter values. 

# dont forget that you cant pass a story element with another element as a tuple, dont know why but it doesnt work.
# dont worry though, the blacksmith can still give you a sword and take your money simultaneously.

a = text_handler.Text_handler()
maze = maze_handler.Maze()
event = event_handler.Game_events()

ui = ui.Ui()
inventory = inventory.Inventory(ui)
battle = battle.Battle(ui)


main_dict = {
    # The story begins, the fire crackles gently.
    '0'  : (a.story, 0), 
    # A man aproaches.
    '1'  : (a.story, 1), 
    # Accept the quest? 1 = yes, 2 = no
    '2'  : (a.branch, 0, '1', (a.go_to, 2.1, ui.gold_handler, 200), '2', a.game_over, 1), 
        # Quest accepted, his eyes light up.
        '2.1'  : (a.story, 2), 
    # Reading the note.    
    '3'  : (a.story, 3), 
    # Prepare for adventure. 1 = visit tavern, 2 = embark
    '4'  : (a.branch, 1, '1', a.go_to, 'empty', '2', (a.story, 4, maze.enter, (4, 6, 'old_town', 'reversed'))),
    # The Retired Adventurers Arms. 1 = own room, 2 = bar, 3 = potions, 4 = smith, 5 = back
    '5'  : (a.branch, 2, '1', a.go_to, 5.1, '2', a.go_to, 5.2, '3', a.go_to, 5.3, '4', a.go_to, 5.4, '5', a.go_to, 4), 
        # Your own room. 1 = rest, 2 = trunk, 3 = tutorial, 4 = back
        '5.1'  : (a.branch, 3, '1', (a.go_to, 5.1, ui.hp_handler, 999),'2', a.go_to, 5.11, '3', a.go_to, 5.12, '4', a.go_to, 5), 
            # Personal trunk. 1 = take sword, 2 = take shield, 3 = back
            '5.11' : (a.branch, 4, '1', (a.go_to, 5.11, inventory.add_item, 'Wooden Sword'), '2', (a.go_to, 5.11, inventory.add_item, 'Leather Buckler'), '3', a.go_to, 5.1), 
            # Questing journal. 1 = inventory tutorial, 2 = battle turorial, 3 = back 
            '5.12' : (a.branch, 8, '1', a.go_to, 5.121, '2', a.go_to, 5.122, '3', a.go_to, 5.1), 
                # Inventory tutorial. 1 = back
                '5.121' : (a.branch, 9, '1', a.go_to, 5.12), 
                # Battle tutorial. 1 = next page, 2 = back
                '5.122' : (a.branch, 10, '1', a.go_to, 5.123, '2', a.go_to, 5.12), 
                # Battle page 2. 1 = back
                '5.123' : (a.branch, 11, '1', a.go_to, 5.12), 
        # Bar. 
        '5.2' : (a.branch, 5, '1', a.go_to, 5.2, '2', a.go_to, 5.2, '3', a.go_to, 5), 
        # Potions.
        '5.3' : (a.branch, 6, '1', a.go_to, 5.3, '2', a.go_to, 5.3, '3', a.go_to, 5), 
        # Smith.
        '5.4' : (a.branch, 7, '1', a.go_to, 5.4, '2', a.go_to, 5.4, '3', a.go_to, 5), 
    #outside the library STORY. 1 = go in, 2 = go back into the maze
    '6'  : (a.branch, 15, '1', a.go_to, 7, '2', (a.story, 11, maze.enter, (5, 6, 'old_town'))),
    # Into the streets
    '7'  : (a.story, 5),
    # Wake the librarian? 1 = drop a book, 2 = explore
    '8'  : (a.branch, 12, '1', a.go_to, 8.1, '2', a.go_to, 10.2), 
        # Dropping the book!
        '8.1'  : (a.story, 6), 
    # Fairytales and childrens books
    '9'  : (a.story, 7), 
    # Try again, 1 = question more, 2 = explore, 3 = leave
    '10'  : (a.branch, 13, '1', a.go_to, 10.1, '2', a.go_to, 10.2, '3', a.go_to, 11), 
        # Look at the maps. 1 = explore, 2 = leave
        '10.1'  : (a.branch, 14, '1', a.go_to, 10.2, '2', a.go_to, 11), 
        # Explore the library (unfinshed, branch 18)
        '10.2'  : (a.branch, 18, '1', a.go_to, 10),
    # Outside the library GENERIC. 1 = go in, 2 = go back, 3 = inner city
    '11'  : (a.branch, 16, '1', a.go_to, 10.1, '2', a.go_to, 10.2, '3', (a.story, 8, maze.enter, (11, 12, 'inner_city', 'reversed'))),
    # Arriving at the checkpoint
    '12'  : (a.story, 9),
    # Old man complains, 1 = respond
    '13'  : (a.branch, 17, '1', a.go_to, 13.1),
        # Your response
        '13.1'  : (a.story, 10),
    }

# branch template ''  : (a.branch, , '1', a.go_to, , '2', a.go_to, )


# test_dict = {'0' : (a.room, 3, ('West', 'South', 'North'), '1', a.go_to, 5.2, '2', a.go_to, 5.2, '3', a.go_to, 5),
#              '1' : (a.story, 2, maze.exit)}
