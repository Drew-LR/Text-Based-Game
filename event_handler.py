from constants import term
import constants
import ui
import event_list

ui_ob = ui.Ui()
# the game_events function is called by selecting 'new game' from the menu, 
# this function iterates over event_list.py's main_dict, which first clears and updates the ui on each loop.
# game_events evaluates the 'constants.skip' value, and (if 0) runs the current element of the dict, and continues running them in order
# until a branching option is offered to the player.
# branching options (events which require input from the player) modify 'constants.skip', therefore on the next loop game_events runs
# the correct outcome of the choice from a second dict called 'new_dict', the outcome is chosen based on a chronological decimal system,
# heres an example. if the branching option has key 3, it's answer will have key 4. for more than one answer, keys will be 4.1 ,4.2 etc.
# After the program displays the correct outcome from 'new_dict' it falls back into running events from the main_dict chronologically,
# and continues until the next branching option, and so on. 

def game_events():
        print(term.clear) # clear the screen
        ui_ob.ui_update() # update ui

        while constants.skip < 99: # untill 'constants.skip' equals 99, keep doing the following. 

            for i,k in enumerate(event_list.main_dict.items()): # iterate over index and key of main_dict.
                print(term.clear) # clear the screen
                if constants.skip >= 99:
                    break
                ui_ob.ui_update() # update ui

                if constants.skip != 0: # if 'constants.skip' is not 0 or 99
                    dict_key_part = str(i) # dict_key provides the fist element of the decimal cordinate which points to the chosen outcome. it is 'i', and is converted to a string to match with the key of current event. 
                    dict_key = dict_key_part + ".{}".format(str(constants.skip)) # the value of constants.skip represents which choice the player made, it is appended onto 'dict_key' after a decimal point.

                    try: # check if there is a branching outcome, not all choices cause branching, some just change stats etc and move on with the story.
                        key_elem = event_list.new_dict[dict_key] # from 'new_list' take the element whose key matches the decimal cordinate. this is the players chosen option.
                        func = key_elem[0] # the first variable for this key is a function to be called, the 'top level function'
                        constants.skip = 0 # 'reset constants.skip' for the next iteration
                        print(func(*key_elem[1:])) # feed all other variables to the 'top level function', some may also be functions (see event_list.py) 
                        while 1: # wait until the player presses 'KEY_ENTER', then continue with the iteration of 'main_dict'.
                            key = term.inkey()
                            if key.is_sequence and key.name == 'KEY_ENTER':
                                break
                    except: # if branching outcome happens to be empty, just continue running events from 'main_dict', something other than the story changed, player HP for example.
                        constants.skip = 0 # before we pass on an empty (a key with no variables), we have to reset constants.skip for the next iteration.
                        pass

                if constants.skip >= 99:
                    break
                key_elem = event_list.main_dict[str(i)] # if 'constants.skip' remains 0, run the i'th element from 'main_dict' (the current one).
                func = key_elem[0] # it's first variable is the 'top layer function'
                constants.skip = 0 # 'reset constants.skip' for the next iteration
                print(func(*key_elem[1:])) # feed those other variables to the 'top layer function' for a good time.
                while 1: # wait until the player presses 'KEY_ENTER' to start the next iteration of the loop.
                    key = term.inkey()
                    if key.is_sequence and key.name == 'KEY_ENTER':
                        break

        if constants.skip == 99: # if hp < 0.
            key_elem = event_list.new_dict[str(constants.skip)] # run the event in 'new_dict', at key '99'.
            func = key_elem[0] # the 'top layer function' for this event is allways ui.game_over. it displays a random game over message. 
            print(func(*key_elem[1:])) # feed the parameter 'p' to ui.game over. it selects the text which the game over message will be chosen from.

            while 1: # wait until the player presses 'KEY_ENTER' to move past the game over screen.
                key = term.inkey()
                if key.is_sequence and key.name == 'KEY_ENTER':
                    break # breaks out of the 'main_dict' iteration of events.
                break # breaks out of the top while loop and back to the main menu.

        constants.skip = 0 # reset this to zero for the new game.
        ui_ob.reset() # reset player stats for tne new game.
        return