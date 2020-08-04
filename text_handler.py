from constants import term
import constants
import textwrap
import random

class Text_handler(): # this class displaying text of various types and handles cases where the player responds to text by making choices.
    def __init__(self, filename):
        file = open(filename, "r")  # each instance of this class opens, reads in and closes a file designated on instantiation
        self.data = file.read()
        file.close

        # End strings, these are frequently repeated strings (which usually print at the end of other text and prompt the user).
        self.pak = "\n\n" + " press any key to continue..."
        self.yn = "\n\n" + " y/n..."
        self.not_gold = "\n\n" + " Not engough gold..."
        self.Not_hp = "\n\n" + " HP reduced to 0. You have died..."
        self.start_battle = "\n\n" + " Press to Start Battle!"

        self.text_pos = term.home + term.move_down(9) # a standard cursor position for printing text in the right place(about half way down the window)
        self.paragraph = self.data.split("\n\n") # This seperates the text document by paragragh, allowing the function call to access a specific paragragh, yes/no question or open question instance.

    def yn_txt(self, p, y_con, y_dict, n_con, n_dict): # prints yes/no question text and allows the player to answer. passed arguments take the form: ('p' for which paraghraph to read in from text file), (function which initiates the yes condition, 'y_con'), (a value to pass to y_con if returned, 'y_dict'). same format again for n_con/n_dict.
        text = self.paragraph[p].split('#') # seperate text by line with a '#'. splitting by line may not always be appropriate as question text might be any length, doing it this way seperates it into: text[0]=(question), text[1]=(yes outcome), text[2]=(no outcome).
        print(self.text_pos + term.clear_eos + textwrap.fill(text[0], term.width, break_long_words=False) + self.yn) # prints the question at the standard text position followed by the 'yn' end string prompt

        key = '' # initialise key as blank string
        while key != 'y' or key != 'n': # loop until the player has entered 'y' or 'n'.
            key = term.inkey() # bind keystroke to variable 'key'
            if key == 'y': # if 'y' is input, print a newline for asthetic space, then the yes answer text at text[1](wrapped). 
                print ("\n" + textwrap.fill(text[1], term.width, break_long_words=False) + self.pak)
                constants.skip = 1
                return y_con(y_dict) # return function 'y_con' with parameter and value and 'y_dict'.
            
            if key == 'n': # in 'n' is input, print a newline for asthetic space, then the no answer text at text[2](wrapped). 
                print("\n" + textwrap.fill(text[2], term.width, break_long_words=False) + self.pak)
                constants.skip = 2
                return n_con(n_dict) # return function 'n_con' with parameter and value and 'n_dict'.

    def open_q(self, p, *argv): # function prints and handles open questions with any number of possible answers. it takes arguments in the format; ('p' for which paraghraph to read in from text file. 'p' variable is a positional argument, not an argv), (a number string, i.e. '1', which will match 'key'), (a function which will give some result), (a value to provide the function when it is returned) 
        text1,text2 = self.paragraph[p].split('@') # split the text into two strings. text1 is the question and options. text2 contains the results, only the option chosen will be printed.
        text1 = text1.split('#') # seperate by line
        text2 = text2.split('#') # seperate by line
        print(term.home + term.move_down(8) + term.clear_eos) # clear the text area before iterating.
        for i in range(len(text1)): # iterate through each line in text1 and print them with wrapping.
            print(textwrap.fill(text1[i], term.width, break_long_words=False))

        while 1:
            key = term.inkey() # wait for key press and bind it to variable 'key', number keys return a string of that number.
            for i in range(len(argv)): # iterate through each index in argv.
                if argv[i] == key: # if an arg in argv matches the string stored in 'key', print (with text wrapping) the line in text2 which corresponds to that number. key is converted to int and used as the index of text2 (-1 because the optional args in argv always start at 1 so the player doesn't input a zeroth choice) 
                    print (textwrap.fill(text2[int(key)-1], term.width, break_long_words=False) + self.pak)
                    constants.skip += int(key)
                    return argv[i+1](argv[i+2]) # having matched argv[i] with key, we now know which answer was selected, according to the argument input format we return the function of the ith answer, necessarilly i+1, and then pass it the parameter stored at i+2.
                    
    def story_txt(self, p): # print story element paragraph index [p], at standard text position with wrapping and pak end string prompt. 
        return self.text_pos + term.clear_eos + textwrap.fill(self.paragraph[p], term.width, break_long_words=False) + self.pak 
    
    def consequence_returner(self, p): #returns a randomly selected consequence text from the category at 'p', e.g death category.
        text = self.paragraph[p].splitlines() #splits self.paragraph(the category selected by 'p') into a list of lines
        return (term.clear + self.text_pos + textwrap.fill(random.choice(text), term.width, break_long_words=False)) # prints a randomly selected, wrapped, string from category 'p'  

    def game_over(self, p):
        text = self.paragraph[p].splitlines() #splits self.paragraph(the category selected by 'p') into a list of lines
        if p == 0:
            return (term.clear + self.text_pos + term.move_right(term.width//2- len(text[p])//2) + textwrap.fill(random.choice(text), term.width, break_long_words=False)) # prints a randomly selected, wrapped, string from category 'p' 
        else:
            constants.skip = 100
            return (term.clear + self.text_pos + term.move_right(term.width//2- len(self.paragraph[p])//2) + textwrap.fill(self.paragraph[p], term.width, break_long_words=False)) # prints a randomly selected, wrapped, string from category 'p'  

    def battle_text(self, p, func, func_var): # takes 'p' as the index of the paragraph to access from a file.
        print(self.text_pos + term.clear_eos + textwrap.fill(self.paragraph[p], term.width, break_long_words=False) + self.start_battle)
        while 1:
            key = term.inkey()
            if key.is_sequence and key.name == 'KEY_ENTER':
                break
        return func(func_var)
