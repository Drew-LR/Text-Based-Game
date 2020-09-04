from constants import term
import constants
import textwrap
import random
import time
import items_lib

class Battle():
    def __init__(self, player_ui):
        self.player_ui = player_ui
        self.mob_action = ''
        self.player_action_list = ['Attack', 'Defend', 'Item 1', 'Item 2']

    def init_battle_hud(self, mob):
        print(term.home + term.move_down(9) + term.clear_eos) # clear the area below player UI
        mob_hp = mob.hp # bind the passed in mob object to a local object so the original object wont be modified. we'll want to reuse that.

        def update_hud(): #this function draws the battle HUD to the screen.
            # print the line and the enemy stats. 
            print(term.home + term.move_down(term.height-7))
            for i in range(0,term.width):
                print('_', end='')

            # column 1 enemy stats 
            print(term.home + term.move_down(term.height-5) + term.clear_eol + "{:>7}{:<}".format('Name: ', mob.name))
            print(term.clear_eol + "{:>7}{:<}".format('HP: ', ''.join(mob_hp)))
            print(term.clear_eol + "{:>7}{:<}".format('Speed: ', mob.speed))

            # column 2 enemy stats
            print(term.home + term.move_down(term.height-5) + term.move_right(term.width//3) + term.clear_eol + "{:>7}{:<}".format('Weapon: ', mob.weapon.name))
            print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Shield: ', mob.shield.name))
            print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 1: ', mob.item_1.name))
            print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 2: ', mob.item_2.name)) 

            # print the players action choices, these are derived from weapon and items equipped.
            print(term.home + term.move_down(5 ) + " 1) Attack with {}".format(self.player_ui.weapon.name) + term.orange(" ({}-{} damage)".format(self.player_ui.weapon.damage[0], self.player_ui.weapon.damage[1])))
            print(" 2) Defend with {}".format(self.player_ui.shield.name) + term.orange(" ({}-{} defence)".format(self.player_ui.shield.defence[0], self.player_ui.shield.defence[1])))
           
            if self.player_ui.item_1.name != '(Empty)':
                print(" 3) Use {}".format(self.player_ui.item_1.name) + term.orange2(" ({})".format(self.player_ui.item_1.battle_descrip)))
            else:
                print(" 3) {}".format(self.player_ui.item_1.name))
            if self.player_ui.item_2.name != '(Empty)':
                print(" 4) Use {}".format(self.player_ui.item_2.name) + term.orange2(" ({})".format(self.player_ui.item_2.battle_descrip)))
            else:
                print(" 4) {}".format(self.player_ui.item_2.name))

            print(" n) Display notes about {}".format(mob.name))

        while mob_hp != [] and self.player_ui.hp != []: # do this untill mob or player runs out of HP. 

            self.player_action = '' # initialise player and mob action, this is the action they choose each turn. 
            mob_action = ''

            update_hud() # print the battle HUD for the first time
    
            while 1: # begin the turn loop, allows the player to select action/note inputs, change their mind, and eventually confirm with ENTER.
                key = term.inkey() # reads key input from the player.                
                if key == 'n': # pressing 'n' shows some notes about the mob.
                    print(term.home + term.move_down(term.height-5) + term.move_right(1) + term.clear_eos + "Notes: {}".format(textwrap.fill(mob.notes, term.width-7, break_long_words=False)))
                    term.inkey() # pressing any key while note are showing hides them and brings back the battle HUD
                    update_hud() 
    
                for i in range(len(self.player_action_list)): # cheack each index of the players 'action_list' (0-3).
                    if key == str(i+1): # if key matches 'action_list' index (0-3), but plus 1 so (1-4) because we are using key 1-4. print a prompt shoing the player what they are choosing. 
                        print(term.home + term.move_down(11) + '{}?'.format(term.bold(self.player_action_list[i])) + ' Press enter to confirm.')
                        self.player_action = self.player_action_list[i] # set 'self.player_action' to whatever the player has selected.

                if key.is_sequence and key.name =='KEY_ENTER' and self.player_action != '': # if player presses enter their currently selected action is chosen.
                    break # we break out of the turn loop.

            # time to do the end-of-turn combobulations!!

            chance = random.randint(0, 3) # pick random number from range 0-2('up to, but not including' is pythons standard)
            if chance == 1: #if the number picked was one (1 in 3, or 30% chance)
                mob_action = mob.action_list[1] #set mob_action to 'Fumble'
            else:
                mob_action = mob.action_list[0] #set mob_action to 'Attack'

            if self.player_action == 'Attack':      
                print(term.home + term.move_down(11) + term.clear_eol +'{} {}s with {}'.format(self.player_ui.name, self.player_action, str(self.player_ui.weapon.name)))
                time.sleep(.3)
                dmg = random.randrange(self.player_ui.weapon.damage) - random.randrange(mob.shield.defence)
                mob_hp = mob_hp[:-dmg]
                print(term.home + term.move_down(12) + term.clear_eol + "{} takes {} damage".format(mob.name, term.red(str(dmg))))
                time.sleep(.3)

            elif self.player_action == 'Defend':     
                print(term.home + term.move_down(11) + term.clear_eol +'{} {}s with {}'.format(self.player_ui.name, self.player_action, str(self.player_ui.shield.name)))
                time.sleep(.3)
                print('Defending halves damage from enemy attacks')
                time.sleep(.3)

            elif self.player_action == 'Item 1':     
                print(term.home + term.move_down(11) + term.clear_eol +'{} uses {}'.format(self.player_ui.name, str(self.player_ui.item_1.name)))
                dmg = random.randint(4,9) - random.randrange(2,3)
                mob_hp = mob_hp[:-dmg]
                print(term.home + term.move_down(12) + term.clear_eol + "{} takes {} damage".format(mob.name, term.red(str(dmg))))
                time.sleep(.3)

            elif self.player_action == 'Item 2':     
                print(term.home + term.move_down(11) + term.clear_eol +'{} uses {}'.format(self.player_ui.name, str(self.player_ui.item_2.name)))               
                chance = random.randint(0,5) # pick random number from range 0-4('up to, but not including' is pythons standard)
                if chance == 1: #if the number picked was one (1 in 5, or 20% chance)
                    dmg = 999999999
                else:
                    dmg = 0
                if dmg != 0:
                    mob_hp = mob_hp[:-dmg]
                else:
                    mob_hp = mob_hp
                print(term.home + term.move_down(12) + term.clear_eol + "{} takes {} damage".format(mob.name, term.red(str(dmg))))
                time.sleep(.3)
                
            update_hud() # update battle HUD again to draw any changes to the screen

            if mob_hp ==[]:
                break

            time.sleep(.3)
            print(term.home + term.move_down(13) + '. ')
            time.sleep(.3)
            print(term.home + term.move_down(13) + term.move_right(1) + '. ')
            time.sleep(.3)
            print(term.home + term.move_down(13) + term.move_right(2) + '. ')
            time.sleep(.3)

            if mob_action =='Attack':
                print(term.home + term.move_down(14) + '{} {}s with {}'.format(mob.name, mob_action, str(mob.weapon.name)))  
                time.sleep(.3)
                dmg = random.randint(4,6) - random.randint(2,3)
                if self.player_action == 'Defend':
                    dmg = dmg//22
                self.player_ui.hp_handler(-dmg)
                print(term.home + term.move_down(15) + "{} takes {} damage".format(self.player_ui.name, term.red(str(dmg))))
                time.sleep(.3)

            if mob_action == 'Fumble':
                print(term.home + term.move_down(14) + '{} {}s'.format(mob.name, mob_action))  
                time.sleep(.3)
                dmg = 0
                print(term.home + term.move_down(15) + "{} takes {} damage".format(self.player_ui.name, term.red((str(dmg)))))
                time.sleep(.3)
            
            self.player_ui.ui_update()
            if self.player_ui.hp ==[]:
                break
            
            time.sleep(.3)
            print(term.home + term.move_down(17) + 'Press enter to start next turn.')

            if key.is_sequence:
                key = ''
            while 1:
                key = term.inkey()
                if key.is_sequence and key.name == "KEY_ENTER":
                    break      

        if mob_hp == []:
            return term.home + term.move_down(17) + term.clear_eol + '{} slays {}'.format(self.player_ui.name, mob.name)      
        elif self.player_ui.hp == []:
            return term.home + term.move_down(17) + term.clear_eol + 'You were slain by {}'.format(mob.name)

            # keyboard input while sleep            