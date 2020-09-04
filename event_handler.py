from constants import term
import constants
import ui
import event_list
import inventory
import math

ui_ob = ui.Ui()
inventory_ob = inventory.Inventory(ui_ob)
# the game_events function is called by selecting 'new game' from the menu, 
# this function iterates over event_list.py's main_dict, which first clears and updates the ui on each loop.
# game_events evaluates the 'constants.skip' value, and (if 0) runs the current element of the dict, and continues running them in order
# until a branching option is offered to the player.
# branching options (events which require input from the player) modify 'constants.skip', therefore on the next loop game_events runs
# the correct outcome of the choice from a second dict called 'new_dict', the outcome is chosen based on a chronological decimal system,
# heres an example. if the branching option has key 3, it's answer will have key 4. for more than one answer, keys will be 4.1 ,4.2 etc.
# After the program displays the correct outcome from 'new_dict' it falls back into running events from the main_dict chronologically,
# and continues until the next branching option, and so on. 

def game_events(dictionary):
        print(term.clear) # clear the screen
        ui_ob.ui_update() # update ui

        constants.maze = False # if we've moved into a sub iteration (like a dungeon) reset this immediatley, lest you be trapped forever...which you will be, i tried, and im still here...

        index = 0
        while ui_ob.hp > 0 and constants.game_over == False:
            
            for k, v in dictionary.items(): # iterate over index and key of main_dict.

                if str(index) == k: # if the string version of index is equal to the key of any event
                    print(v[0](*v[1:])) # v[0] was not an int

                    if constants.maze == True:

                        file = open('dump.txt', 'a')
                        file.write('\n constants.maze? Index {}. Maze {}.'.format(index, constants.maze))
                        file.close()

                        game_events(event_list.maze_dict)

                    if constants.maze_exit == True:
                        constants.maze_exit = False

                        file = open('dump.txt', 'a')
                        file.write('\n constants.unmaze? Index {}. Maze {}. Unmaze {}'.format(index, constants.maze,constants.maze_exit))
                        file.close()

                        return ''

                    if constants.absolute != 0: # something has changed current branch, they want to go back.
                        index = constants.absolute
                        constants.absolute = 0 # its best to reset
                    
                        file = open('dump.txt', 'a')
                        file.write('\n constants.absolute? Index {}.'.format(index))
                        file.close()
                    
                    else: # nothing else has taken control, add 1 to index to procede in linier fasion.
                        index = math.trunc(index) # in case any branching occured remove the decimal place from index
                        index +=1

                        file = open('dump.txt', 'a')
                        file.write('\n next? {}.'.format(index))
                        file.close()

                if ui_ob.hp <= 0 or constants.game_over == True:
                    file = open('dump.txt', 'a')
                    file.write('\n game over {}. HP {}.'.format(constants.game_over, ui_ob.hp))
                    file.close()
                    break
                       
        ui_ob.reset() # if we arrived here player HP is 0. reset player stats for tne new game.
        constants.game_over = False
        file = open('dump.txt', 'a')
        file.write('\n leaving the game loop{}. hp {}'.format(constants.game_over, ui_ob.hp))
        file.close()
        return