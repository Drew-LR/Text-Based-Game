from constants import term
import constants
import items_lib
import textwrap

master_weapon_list = [items_lib.wooden_sword, items_lib.stone_club, items_lib.tree_branch]
master_shield_list = [items_lib.leather_buckler, items_lib.pot_lid, items_lib.uber_aegis]
master_items_list = [items_lib.ork_teeth, items_lib.fur_ball, items_lib.magic_beans]

class Inventory():
    weapon_list = [items_lib.no_item]
    shield_list = [items_lib.leather_buckler, items_lib.pot_lid]
    item_list = [items_lib.magic_beans, items_lib.fur_ball]
    def __init__(self, player_ui):
        
        self.player_ui = player_ui
        self.menu = ['Weapon', 'Shield', 'Item 1', 'Item 2']
  

    def print_list(self, current_menu, current_item): # print the list selected by the menu
        print(term.home + term.move_down(5) + term.clear_eos) # clear the area below player UI

        print(term.home + term.move_down(4))
        for idx, row in enumerate(self.menu):
            if idx == current_menu: 
                print(term.move_right(1) + term.on_white + term.black + term.bold(row))
            else:
                print(term.move_right(1) + row)
        print(term.home + term.move_down(5))
        print(term.move_up(2))
        for i in range(0,17):
            print(term.move_right(60) + '|') # draw a dividing line.
        print(term.move_right(60) + term.underline('Press enter to equip'))


        if current_menu == 0: # weapon list
            print(term.home + term.move_down(5) + term.move_right(67) + term.underline('Weapons'))
            for i, n in enumerate(self.weapon_list):
                if n.name == '(Empty)':
                    continue
                if i == current_item:
                    print(term.move_right(61) + term.bold('{}) '.format(i+1) + n.name))
                else:
                    print(term.move_right(61) + '{}) '.format(i+1) + n.name)

            print(term.home + term.move_down(10) + 'Notes on {}: '.format(self.weapon_list[current_item].name))
            print(textwrap.fill(self.weapon_list[current_item].descrip, 60, break_long_words=False))
            print(term.move_down(1) + 'Damage: ' + term.orange('({}-{})'.format(self.weapon_list[current_item].damage[0], self.weapon_list[current_item].damage[1])))
            print('Defence: ' + term.orange('({}-{})'.format(self.weapon_list[current_item].defence[0], self.weapon_list[current_item].defence[0])))
            print('Chance to hit: ' + term.orange('{}%'.format(self.weapon_list[current_item].chance)))
            print('Passive: ' + term.orange('{}'.format(self.weapon_list[current_item].passive)))

        elif current_menu == 1: # shield list
            print(term.home + term.move_down(5) + term.move_right(67) + term.underline('Shields'))
            for i, n in enumerate(self.shield_list):
                if n.name == '(Empty)':
                    continue
                if i == current_item:
                    print(term.move_right(61) + term.bold('{}) '.format(i+1) + n.name))
                else:
                    print(term.move_right(61) + '{}) '.format(i+1) + n.name)

            print(term.home + term.move_down(10) + 'Notes on {}: '.format(self.shield_list[current_item].name))
            print(textwrap.fill(self.shield_list[current_item].descrip, 60, break_long_words=False))
            print(term.move_down(1) + 'Damage: ' + term.orange('({}-{})'.format(self.shield_list[current_item].damage[0], self.shield_list[current_item].damage[1])))
            print('Defence: ' + term.orange('({}-{})'.format(self.shield_list[current_item].defence[0], self.shield_list[current_item].defence[1])))
            print('Chance to hit: ' + term.orange('{}%'.format(self.shield_list[current_item].chance)))
            print('Passive: ' + term.orange('{}'.format(self.shield_list[current_item].passive)))



        elif current_menu == 2 or current_menu == 3: # item list
            print(term.home + term.move_down(5) + term.move_right(68) + term.underline('Items'))
            for i, n in enumerate(self.item_list):
                if n.name == '(Empty)':
                    continue
                if i == current_item:
                    print(term.move_right(61) + term.bold('{}) '.format(i+1) + n.name))
                else:
                    print(term.move_right(61) + '{}) '.format(i+1) + n.name)

            print(term.home + term.move_down(10) + 'Notes on {}: '.format(self.item_list[current_item].name))
            print(textwrap.fill(self.item_list[current_item].descrip, 60, break_long_words=False))
            print(term.move_down(1) + 'Damage: ' + term.orange('({}-{})'.format(self.item_list[current_item].damage[0], self.item_list[current_item].damage[1])))
            print('Defence: ' + term.orange('({}-{})'.format(self.item_list[current_item].defence[0], self.item_list[current_item].defence[0])))
            print('Chance to hit: ' + term.orange('{}%'.format(self.item_list[current_item].chance)))
            print('Passive: ' + term.orange('{}'.format(self.item_list[current_item].passive)))

    @classmethod
    def add_item(cls, name):
        for i in master_weapon_list:
            if name == str(i.name):
                for j in cls.weapon_list:
                    if j == items_lib.no_item:
                        cls.weapon_list.remove(j)
                cls.weapon_list.append(i)
        
        for i in master_shield_list:
            if name == str(i.name):
                for j in cls.shield_list:
                    if j == items_lib.no_item:
                        cls.shield_list.remove(j)
                cls.shield_list.append(i)
        
        for i in master_items_list:
            if name == str(i.name):
                for j in cls.item_list:
                    if j == items_lib.no_item:
                        cls.item_list.remove(j)
                cls.item_list.append(i)

    
    def inventory(self):
        current_row = 0  # 0=weapon_list, 1=shield_list, 2=item_list
        current_item = 0
        #self.print_menu(current_row)
        self.print_list(current_row, current_item)

        while 1:
            key = term.inkey()
            if key == 'i':
                print(term.home + term.move_down(5) + term.clear_eos)
                break
            if current_row == 0: # if in weapon menu
                if len(self.weapon_list)%2 ==0:
                    self.weapon_list.append(items_lib.no_item)
                for i in range(len(self.weapon_list)): # traverse length of weapon menu
                    if key == str(i+1): # if we find key in the indecies of weapon menu
                        current_item = i # currently selected weapon is chosen to be bold
                        self.print_list(current_row, current_item) # print updated weapon list, to show the bold
                    if key.is_sequence and key.name == "KEY_ENTER":

                        self.player_ui.weapon = self.weapon_list[current_item]
                        self.player_ui.item_handler('weapon', current_item, self.weapon_list) 
                        self.player_ui.ui_update()

            if current_row == 1: # if in shield menu
                if len(self.shield_list)%2 ==0:
                    self.shield_list.append(items_lib.no_item)
                for i in range(len(self.shield_list)): # traverse length of shield menu
                    if key == str(i+1): # if we find key in the indecies of shield menu
                        current_item = i # currently selected shield is chosen to be bold
                        self.print_list(current_row, current_item) # print updated shield list
                    if key.is_sequence and key.name == "KEY_ENTER":
                        
                        self.player_ui.shield = self.shield_list[current_item]
                        self.player_ui.item_handler('shield', current_item, self.shield_list) 
                        self.player_ui.ui_update()

            if current_row == 2: # if in item menu, but for equipping item 1
                if len(self.item_list)%2 ==0:
                    self.item_list.append(items_lib.no_item)
                for i in range(len(self.item_list)): # traverse length of item menu
                    if key == str(i+1): # if we find key in the indecies of item menu
                        current_item = i # currently selected item is chosen to be bold
                        self.print_list(current_row, current_item) # print updated item list
                    if key.is_sequence and key.name == "KEY_ENTER":
                        self.player_ui.item_1 = self.item_list[current_item]
                        self.player_ui.item_handler('item_1', current_item, self.item_list) 
                        self.player_ui.ui_update()

            if current_row == 3: # if in item menu but for equipping item 2
                if len(self.item_list)%2 ==0:
                    self.item_list.append(items_lib.no_item)
                for i in range(len(self.item_list)): # traverse length of item menu
                    if key == str(i+1): # if we find key in the indecies of item menu
                        current_item = i # currently selected item is chosen to be bold
                        self.print_list(current_row, current_item) # print updated item list
                    if key.is_sequence and key.name == "KEY_ENTER":
                        self.player_ui.item_2 = self.item_list[current_item]
                        self.player_ui.item_handler('item_2', current_item, self.item_list) 
                        self.player_ui.ui_update()
                        #print(term.home + str(i) + 'enter')

            if key.is_sequence:

                if key.name == 'KEY_UP' and current_row > 0:
                    current_row -= 1
                    current_item = 0
                    
                elif key.name == 'KEY_DOWN' and current_row < len(self.menu) -1:
                    current_row += 1
                    current_item = 0
                #self.print_menu(current_row)
                self.print_list(current_row, current_item)

