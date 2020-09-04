from constants import term
import constants
#import text_handler
import time
import textwrap
import items_lib

#consequence_ob = text_handler.Text_handler('consequences.txt')

class Ui():
    name = 'Lonk'
    gold = 5
    hp = 30
    hp_max = 30
    speed = 8
    weapon = items_lib.no_item
    shield = items_lib.no_item
    item_1 = items_lib.no_item
    item_2 = items_lib.no_item

    player_has_moved = False

    @classmethod
    def reset(cls):
        cls.name = ''
        cls.gold = 5
        cls.hp = 30
        cls.speed = 8

        cls.weapon = items_lib.no_item
        cls.shield = items_lib.no_item
        cls.item_1 = items_lib.no_item
        cls.item_2 = items_lib.no_item

    @classmethod
    def item_handler(cls, item, index, list):
        unequip = items_lib.no_item
        if item == 'weapon':
            if cls.weapon == list[index]:
                cls.weapon = unequip
            else:
                cls.weapon = list[index]
        elif item == 'shield':
            if cls.shield == list[index]:
                cls.shield = unequip
            else:
                cls.shield = list[index]
        elif item == 'item_1':
            if cls.item_1 == list[index]:
                cls.item_1 = unequip
            elif cls.item_2 == list[index]:
                cls.item_2 = unequip
                cls.item_1 = list[index]
            else:
                cls.item_1 = list[index] 
        elif item == 'item_2':
            if cls.item_2 == list[index]:
                cls.item_2 = unequip
            elif cls.item_1 == list[index]:
                cls.item_1 = unequip
                cls.item_2 = list[index]
            else:
                cls.item_2 = list[index] 
    
    @classmethod
    def speed_handler(cls, speed_change):

            if speed_change >= 0:
                cls.speed += speed_change
                cls.ui_update()
                return term.home + term.move_down(3) + "{:>7}{:<}".format('Speed: ', cls.speed) + " " + term.green("+{} Speed ").format(speed_change)
            else:
                cls.speed += speed_change
                cls.ui_update()
                return term.home + term.move_down(3) + "{:>7}{:<}".format('Speed: ', cls.speed) + " " + term.red("{} Speed ").format(speed_change)  

    @classmethod
    def gold_handler(cls, gold_change):

        if gold_change >= 0:
            cls.gold += gold_change
            #cls.ui_update()
            return term.home + term.move_down(1) + "{:>7}{:<}".format('Gold: ', cls.gold) + " " + term.green("+{} Gold ").format(gold_change)
        else:
            if abs(gold_change) > cls.gold:
                #cls.gold = 0
                #cls.ui_update()
                return term.home + term.move_down(1) + "{:>7}{:<}".format('Gold: ', cls.gold) + " " + term.red("Insufficient gold ")
            cls.gold += gold_change
            #cls.ui_update()
            return term.home + term.move_down(1) + "{:>7}{:<}".format('Gold: ', cls.gold) + " " + term.red("{} Gold ").format(gold_change)
    
    @classmethod
    def hp_handler(cls, hp_change):

        if hp_change >= 0:
            cls.hp += hp_change
            if cls.hp > cls.hp_max:
                cls.hp = cls.hp_max
                #cls.ui_update()
                return term.home + term.move_down(2) + "{:>7}{:<}".format('HP: ', cls.hp) + " " + term.green("{} HP ").format('MAX')
            #cls.ui_update()
            return term.home + term.move_down(2) + "{:>7}{:<}".format('HP: ', cls.hp) + " " + term.green("+{} HP ").format(hp_change)
        else:
            cls.hp += hp_change
            if cls.hp <= 0:
                cls.hp = 0
                constants.skip = 99
            #   cls.ui_update()        
            return term.home + term.move_down(2) + "{:>7}{:<}".format('HP: ', cls.hp) + " " + term.red("{} HP ").format(hp_change)
    
        
    @classmethod
    def ui_update(cls):
        for i in range(0,4):
            print(term.move_xy(0,0+i) + term.clear_eol()) # Clear the top 9 rows
            print(term.home)

        # column 1
        print(term.home + term.clear_eol + "{:>7}{:<}".format('Name: ', cls.name))
        print(term.home + term.move_down(1) + term.clear_eol + "{:>7}{:<}".format('Gold: ', cls.gold))
        if cls.hp <= 3:
            print(term.home + term.move_down(2) + term.clear_eol + term.red("{:>7}{:<}").format('HP: ', cls.hp))
        else:
            print(term.home + term.move_down(2) + term.clear_eol + "{:>7}{:<}".format('HP: ', cls.hp))
        
        print(term.home + term.move_down(3) + term.clear_eol + "{:>7}{:<}".format('Speed: ', cls.speed))

        # column 2
        print(term.home + term.move_right(term.width//3) + term.clear_eol + "{:>7}{:<}".format('Weapon: ', cls.weapon.name))
        print(term.home + term.move_down(1) + term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Shield: ', cls.shield.name))
        print(term.home + term.move_down(2) + term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 1: ', cls.item_1.name))
        print(term.home + term.move_down(3) + term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 2: ', cls.item_2.name)) 

        # column 3
        print(term.home + term.move_right(term.width-15) + 'I for inventory'
)
        # print a line
        print(term.home + term.move_down(3))
        for i in range(0,term.width):
            print('_', end='')
         

    @classmethod
    def enter_name(cls):
        print(term.clear + term.home + "Enter you name: ")
        name = []
        while 1:
            key = term.inkey()
            if key in 'abcdefghijklmnopqrstuvwxyz':
                if name == []:
                    name.append(key.upper())
                    print(term.home + term.move_right(17) + ''.join(name))
                else:
                    name.append(key)
                    print(term.home + term.move_right(17) + ''.join(name))

            elif key.is_sequence and key.name == "KEY_BACKSPACE":
                name = name[:-1]
                print(term.home + term.move_right(17) + term.clear_eol + ''.join(name))

        
            elif name != [] and key.is_sequence and key.name == 'KEY_ENTER':
                cls.name = ''.join(name)
                break
        while 1:
            if cls.name == 'Link':
                    print('{} is a fine name for a hero. '.format(''.join(name)) + 'Press enter to continue...')
                    while 1:
                        key = term.inkey()
                        if key.is_sequence and key.name == 'KEY_ENTER':
                            return

            if cls.name != 'Link':
                print("Are you sure {} is your name? y/n: ".format(''.join(name)))
                key = term.inkey()
                if key == 'y':
                    print("Really? " + ''.join(name) + "?, and not something like Link? y/n: ")
                    key = term.inkey()
                    if key == 'y':
                        print(textwrap.fill("Fine then have it you way it's your name anyway and it's not as if link is a better name at least you don't seem to think so enjoy your adventure I'm sure you'll be great at it really.", term.width, break_long_words=False) + " Press enter to continue...")
                        while 1:
                            key = term.inkey()
                            if key.is_sequence and key.name == 'KEY_ENTER':
                                return
                    elif key =='n':
                        continue   
                elif key =='n':
                    continue

