from constants import term
import time
import textwrap
import constants
import ui

ui_ob = ui.Ui()
print(term.clear)

def enter_name():
    name = input("Enter you name: ")
    ui_ob.name = name
    
    if name != 'link' or name != 'Link':
        key = input("Are you sure {} is your name? y/n: ".format(name))
        
        if key == 'y':
            key1 = input("Really? " + name + "?, and not something like Link? y/n: ")
            if key1 == 'y':
                print(textwrap.fill("Fine then have it you way it's your name anyway and it's not as if link is a better name at least you don't seem to think so enjoy your adventure I'm sure you'll be great at it really", term.width, break_long_words=False))
                time.sleep(2)
                return
            elif key1 == 'n':
                enter_name()
        elif key == 'n':
            enter_name()

    elif name == 'link':
        print('{} is fine name for a hero'.format(name))
        time.sleep(2)
        return 
