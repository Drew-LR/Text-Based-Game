from constants import term
import constants
import textwrap
import random
import threader
import inventory
import ui

ui_ob = ui.Ui()
inventory_ob = inventory.Inventory(ui_ob)

class Text_handler(): # this class displaying text of various types and handles cases where the player responds to text by making choices.
    def __init__(self):
      
        self.press_continue = "\n\n" + " press Enter to continue..."
        self.press_confirm = "\n\n" + " press Enter to confirm..."
        self.start_battle = "\n\n" + " Press to Start Battle!"
        self.text_pos = term.home + term.move_down(8) # a standard cursor position for printing text in the right place(about half way down the window)

    def story(self, p, func=0, para=0): # print story element paragraph index [p], at standard text position with wrapping and pak end string prompt.
        def open_text():
            file = open('story.txt', 'r')
            data = file.read()
            file.close()
            paragraph = data.split("\n\n")
            
            file = open('story_list', 'w')
            for i,j in enumerate(paragraph):
                file.write('\n{}:\n{}\n'.format(i,j))
            file.close()
            return paragraph
        
        def update():
            print(self.text_pos + term.clear_eos + textwrap.fill(paragraph[p], term.width, break_long_words=False) + self.press_continue)
        
        def interact():
            while 1:
                key = term.inkey()
                if key == 'i':
                    inventory_ob.inventory()
                    update()

                if key.is_sequence and key.name == 'KEY_ENTER':
                    return

        paragraph = open_text()
        update()
        interact()
        ui_ob.ui_update()
        if func != 0:
            return func(para)
        else:
            return ''


    def branch(self, p, *argv): # function prints and handles open questions with any number of possible answers. it takes arguments in the format; ('p' for which paraghraph to read in from text file. 'p' variable is a positional argument, not an argv), (a number string, i.e. '1', which will match 'key'), (a function which will give some result), (a value to provide the function when it is returned) 
        def open_text():
            file = open('branch.txt', 'r')
            data = file.read()
            file.close()
            paragraph = data.split("\n\n")
            
            file = open('branch_list', 'w')
            for i,j in enumerate(paragraph):
                file.write('\n{}:\n{}\n'.format(i,j))
            file.close()
            return paragraph

        def update(bold=0, key_text=0): 
            print(term.home + term.move_down(7) + term.clear_eos) # clear the text area before iterating.
            for i in range(len(text1)): # iterate through each line in text1 and print them with wrapping.
                if i+1 == bold:
                    print(textwrap.fill(term.bold(text1[i]), term.width, break_long_words=False))
                else:
                    print(textwrap.fill(text1[i], term.width, break_long_words=False))
            if key_text != 0:
                print(key_text)

        def interact():
            #constants.static = True
            key_place = 0
            key_text = 0
            while 1:
                key = term.inkey() # wait for key press and bind it to variable 'key', number keys return a string of that number.
                #ui_ob.ui_update()
                for i in range(len(argv)): # iterate through each index in argv.
                    if argv[i] == str(key): # if an arg in argv matches the string stored in 'key', print (with text wrapping) the line in text2 which corresponds to that number. key is converted to int and used as the index of text2 (-1 because the optional args in argv always start at 1 so the player doesn't input a zeroth choice) 
                        if key == argv[-3]:
                            constants.absolute = constants.current_branch
                            
                        update(int(key)+2)
                        print (textwrap.fill(text2[int(key)-1], term.width, break_long_words=False) + self.press_confirm)
                        key_place = int(key)+2
                        key_text = textwrap.fill(text2[int(key)-1], term.width, break_long_words=False) + self.press_confirm
                        
                        res2 =0 # so we can check if its assigned another value
                        if type(argv[i+1]) == tuple:
                            res2, res3 = argv[i+1][0], argv[i+1][1]
                            res4, res5 = argv[i+1][2], argv[i+1][3]
                        else:    
                            res, res1 = argv[i+1], argv[i+2] # function, parameter
                        
                if key == 'i':
                    inventory_ob.inventory()
                    update(key_place, key_text)
                      
                if key.is_sequence and key.name == 'KEY_ENTER':

                    try:
                        if res2 == 0: # if res2 was assigned it means we found a tuple
                            return (res, res1) # no tuple
                        else:
                            return (res2, res3, res4, res5) # tuple
                    except:
                        pass
        paragraph = open_text()

        text1,text2 = paragraph[p].split('@') # split the text into two strings. text1 is the question and options. text2 contains the results, only the option chosen will be printed.
        text1 = text1.split('#') # seperate by line
        text2 = text2.split('#') # seperate by line

        update()
        res = interact()
        if len(res) == 2:
            if 'inventory' or 'go_to' not in str(res[0]): # as at 2/9/20 only inventory changes dont return something to print
                return res[0](res[1]) # this returns us directly to a print statement, if there's nothing to print it will print none.
            else:
                threader.return_func(res[0], res[1]) # for the non-print result
                return '' # then return a nothing string so that 'none' doesnt print
        else: # res has four elements
            
            if 'gold' in str(res[2]) and res[3] < 0 and res[3] < ui_ob.gold: # player tried to make a purchase, check they have enough gold.
                return res[2](res[3])
                # to expand here... if player has max hp, dont let them pay for healing. 
            else:
                things_that_print = ['hp', 'gold']
                for i in things_that_print:
                    if i in str(res[0]):# check if the first tuple is a function that prints
                        threader.print_func(res[0], res[1]) # if so feed it to threaders print function
                        break
                    else:
                        threader.return_func(res[0], res[1]) # if not feed it to threaders return function
                        break
                return res[2](res[3]) # if it changes player ui, return directly

    def game_over(self, p):
        text_string = ''
        def open_text():
            file = open('game_over.txt', 'r')
            data = file.read()
            file.close()
            paragraph = data.split("\n\n")
            
            file = open('game_over_list', 'w')
            for i,j in enumerate(paragraph):
                file.write('\n{}:\n{}\n'.format(i,j))
            file.close()
            return paragraph     
       
        def update():
            print(self.text_pos + term.clear_eos + textwrap.fill(paragraph[p], term.width, break_long_words=False) + self.press_continue)
        
        def interact():
            while 1:
                key = term.inkey()
                # if key == 'i':
                #     inventory_ob.inventory()
                #     update()

                if key.is_sequence and key.name == 'KEY_ENTER':
                    return  text_string

        paragraph = open_text()
        update()
        res = interact()
        constants.game_over = True
        ui_ob.ui_update()
        return res    

    def go_to(self, param):
        if param != 'empty':
            constants.absolute = param
            file = open('dump.txt', 'a')
            file.write('\n constants.absolute in txthndlr {}.'.format(constants.absolute))
            file.close()
            return ''
        else:
            return ''