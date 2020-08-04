from constants import term
import constants
import text_handler
import time
import textwrap

consequence_ob = text_handler.Text_handler('consequences.txt')

class Ui():
    name = ''
    gold = constants.gold
    hp = constants.hp

    speed = constants.speed
    weapon = constants.weapon
    shield = constants.shield
    item_1 = constants.item_1
    item_2 = constants.item_2


    player_has_moved = False

    @classmethod
    def reset(cls):
        cls.name = ''
        cls.gold = constants.gold
        cls.hp = constants.hp
        cls.speed = constants.speed


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
            cls.ui_update()
            return term.home + term.move_down(1) + "{:>7}{:<}".format('Gold: ', cls.gold) + " " + term.green("+{} Gold ").format(gold_change)
        else:
            if abs(gold_change) > cls.gold:
                cls.gold = 0
                return consequence_ob.consequence_returner(0)
            cls.gold += gold_change
            cls.ui_update()
            return term.home + term.move_down(1) + "{:>7}{:<}".format('Gold: ', cls.gold) + " " + term.red("{} Gold ").format(gold_change)
    
    @classmethod
    def hp_handler(cls, hp_change):

        if hp_change >= 0:
            for i in range(hp_change):
                cls.hp.append('#')
            cls.ui_update()
            return term.home + term.move_down(2) + "{:>7}{:<}".format('HP: ', ''.join(cls.hp)) + " " + term.green("+{} HP ").format(hp_change)
        else:
            for i in range(hp_change, 0, 1):
                cls.hp = cls.hp[:-1]
                if cls.hp == []:
                    constants.skip = 99
            cls.ui_update()        
            return term.home + term.move_down(2) + "{:>7}{:<}".format('HP: ', ''.join(cls.hp)) + " " + term.red("{} HP ").format(hp_change)
    
        
    @classmethod
    def ui_update(cls):
        for i in range(0,4):
            print(term.move_xy(0,0+i) + term.clear_eol()) # Clear the top 9 rows
            print(term.home)

        # column 1
        print(term.home + term.clear_eol + "{:>7}{:<}".format('Name: ', cls.name))
        print(term.home + term.move_down(1) + term.clear_eol + "{:>7}{:<}".format('Gold: ', cls.gold))
        print(term.home + term.move_down(2) + term.clear_eol + "{:>7}{:<}".format('HP: ', ''.join(cls.hp)))
        print(term.home + term.move_down(3) + term.clear_eol + "{:>7}{:<}".format('Speed: ', cls.speed))

        # column 2
        print(term.home + term.move_right(term.width//3) + term.clear_eol + "{:>7}{:<}".format('Weapon: ', cls.weapon[0]))
        print(term.home + term.move_down(1) + term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Shield: ', cls.shield[0]))
        print(term.home + term.move_down(2) + term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 1: ', cls.item_1[0]))
        print(term.home + term.move_down(3) + term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 2: ', cls.item_2[0])) 

        # print a line
        print(term.home + term.move_down(3))
        for i in range(0,term.width):
            print('_', end='')
         

    def empty(self, empty=''):
        if empty == 'empty':
            return ''

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
