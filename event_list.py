from constants import term
import constants
import blessed
import text_handler
import ui
import battle
import mobs_lib
import inventory
import random

class Maze():

    def exit(self, para=0):
        
        constants.maze_exit = True
        return ''

    def enter(self, tupe):
        constants.maze = True

        length_dict = {'short' : random.randint(2, 5), 'medium' : random.randint(6,9), 'longest' : random.randint(10, 15)}

        length, branch_tup = tupe[0], tupe[1]

        branch = []
        for i in range(len(branch_tup)):
            branch.append(branch_tup[i])

        file =open('branch.txt', 'r')
        data = file.read()
        file.close()
        para = data.split("\n\n") # open branch.txt and read it in.

        branch_options = []
        for i in range(len(para)):
            if i in branch:
                branch_options.append(para[i]) # make a list of the branching options specified in 'branch'.
                
        num_list = ['1', '2', '3', '4', '5'] # list of possible answers.
        branch_dict = {}
        
        for i, v in enumerate(branch_options): # iterate through the branchings option.
            choice_number = 0
            for j in v:                  # iterate through every character.
                if j in num_list:        # if the character is a number it is a choice the player can make.
                    choice_number += 1   # then add 1 to choice number.
                branch_dict[branch_tup[i]] = choice_number # now this dict contains, key = index of branch_option, value = number of choies in that branch option 

        for k, v in length_dict.items(): # check length dict to get the length of the maze
            if k == length: 
                maze_length = range(0, v+1) 
                coordinate_range = range(0, v)

        for i in maze_length:       # v is the randomised length, one for every maze event we are about to generate.
            #coordinate = ()
            top_func = (a.branch,)
            go_to_func = (a.go_to,)
            key = (str(i),)

            if i == 0:
                p = (branch[0],)
                branch.remove(branch[0])
            else:
                 p = random.choice(branch)
                 p = (p,)

            for k, v in branch_dict.items():
                if p[0] == k:
                    choices = range(1, v+1)

            coordinate_list = []
            for i in coordinate_range:
                coordinate_list.append(i+1)
            for i in choices:
                if len(coordinate_list) < len(choices):
                    coordinate_list.append(random.choice(coordinate_list))

            stem = key + top_func + p
            
            for i in choices:
                choice_num = (str(i),)
                coordinate = (random.choice(coordinate_list),)
                for co in coordinate_list:
                    if co == coordinate[0]:
                        coordinate_list.remove(co)

                stem = stem + choice_num + go_to_func + coordinate

            maze_dict[stem[0]] = stem[1:]
        maze_dict['99'] = (a.story, 5)

        file = open('dump.txt', 'a')
        file.write('\n maze =')
        for k, v in maze_dict.items():
            file.write('\n {} : {}'.format(str(k), str(v)))
        file.close()

# The event dictionary stores all game events in chronological order. k,v pairs are processed by the 'game_events' function in 'event_handler.py'
# 'Keys' in this dict are always numbers, in chronoligical order.
# Each key's 'value', is a tuple of 'values', in the format; function - parameters for that function, function - parameters for that function, and so on.
# The first 'value' in the tuple is a function call to whichever event type we currently want, i.e story text, 
# a battle, a choice to be made by the player etc. Lets call that the 'top level function'.
# 'Values' following the 'top level function' are fed to that function by the 'game_events' function in 'event_handler.py'.
# 'Values' following any other 'lower level function' in the tuple are fed to that function by the 'top level function'.
# As at 1/8/20 only the 'top level function' takes other function calls as arguments. 'lower level functions' only take parameter values. 

# dont forget that you cant pass a story element with another element as a tuple, dont know why but it doesnt wor.
# dont worry though, the blacksmith can still give you a sword and take your money simultaneously.

a = text_handler.Text_handler()
maze = Maze()

ui = ui.Ui()
inventory = inventory.Inventory(ui)
battle = battle.Battle(ui)


main_dict = {
    '0'  : (a.story, 0), # The story begins, the fire crackles gently.
    '1'  : (a.story, 1), # A man aproaches.
    '2'  : (a.branch, 0, '1', (a.go_to, 2.1, ui.gold_handler, 200), '2', a.game_over, 1), # Accept the quest?
        '2.1'  : (a.story, 2), # Quest accepted, his eyes light up.
    '3'  : (a.story, 3), # Reading the note.
    '4'  : (a.branch, 1, '1', a.go_to, 'empty', '2', a.go_to, 6), # Prepare for adventure.
    '5'  : (a.branch, 2, '1', a.go_to, 5.1, '2', a.go_to, 5.2, '3', a.go_to, 5.3, '4', a.go_to, 5.4, '5', a.go_to, 4), # The Retired Adventurers Arms.
        '5.1'  : (a.branch, 3, '1', (a.go_to, 5.1, ui.hp_handler, 999),'2', a.go_to, 5.11, '3', a.go_to, 5.12, '4', a.go_to, 5), # Your own room.
            '5.11' : (a.branch, 4, '1', (a.go_to, 5.11, inventory.add_item, 'Wooden Sword'), '2', (a.go_to, 5.11, inventory.add_item, 'Leather Buckler'), '3', a.go_to, 5.1), # Personal trunk
            '5.12' : (a.branch, 11, '1', a.go_to, 5.121, '2', a.go_to, 5.122, '3', a.go_to, 5.1), #questing journal
                '5.121' : (a.branch, 12, '1', a.go_to, 5.12), # inventory tutorial
                '5.122' : (a.branch, 13, '1', a.go_to, 5.123, '2', a.go_to, 5.12), # battle tutorial
                '5.123' : (a.branch, 14, '1', a.go_to, 5.12), # battle page 2
        '5.2' : (a.branch, 5, '1', a.go_to, 5.2, '2', a.go_to, 5.2, '3', a.go_to, 5),
        '5.3' : (a.branch, 6, '1', a.go_to, 5.3, '2', a.go_to, 5.3, '3', a.go_to, 5),
        '5.4' : (a.branch, 7, '1', a.go_to, 5.4, '2', a.go_to, 5.4, '3', a.go_to, 5),
    '6'  : (a.story, 4, maze.enter, ('short', (13, 14, 15))), # into the streets
    '7'  : (a.story, 7), # and through them
    '8'  : (a.story, 8), # and through them
        #'9.1' : ()
        #'9.1'

    }


maze_dict = {}

test_dict = {'0' : (a.story, 1),
             '1' : (a.story, 2, maze.exit)}
