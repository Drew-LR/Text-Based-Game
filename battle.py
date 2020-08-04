from constants import term
import constants
import textwrap
import random
import time

class Mob():
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp 
        self.speed = speed 

        self.weapon = ['wooden sword',(4,6)]
        self.shield = ['leather jerk',(2,3)]
        self.item_1 = ['Ork tooth']
        self.item_2 = ['Fur ball']   
        self.action_list = ['Attack', 'Fumble'] 

        self.notes = constants.goblin_notes

class Battle():
    def __init__(self, player_ui):
        self.player_ui = player_ui
        self.mob_action = ''
        self.player_action_list = ['Attack', 'Defend', 'Item 1', 'Item 2']

    def init_battle_hud(self, mob):
        mob_hp = mob.hp

        while mob_hp != [] and self.player_ui.hp != []:

            self.player_action = ''
            mob_action = ''

            # print the line and the enemy stats. 
            print(term.home + term.move_down(9) + term.clear_eos)
            print(term.home + term.move_down(term.height-7))
            for i in range(0,term.width):
                print('_', end='')

            # column 1 enemy stats 
            print(term.home + term.move_down(term.height-5) + term.clear_eol + "{:>7}{:<}".format('Name: ', mob.name))
            print(term.clear_eol + "{:>7}{:<}".format('HP: ', ''.join(mob_hp)))
            print(term.clear_eol + "{:>7}{:<}".format('Speed: ', mob.speed))

            # column 2 enemy stats
            print(term.home + term.move_down(term.height-5) + term.move_right(term.width//3) + term.clear_eol + "{:>7}{:<}".format('Weapon: ', mob.weapon[0]))
            print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Shield: ', mob.shield[0]))
            print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 1: ', mob.item_1[0]))
            print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 2: ', mob.item_2[0])) 

            # print the players action choices, these are derived from weapon and items equipped.
            print(term.home + term.move_down(5  ) + " 1) Attack with {} {}".format(constants.weapon[0], term.orange2(constants.weapon[1])))
            print(" 2) Defend with {} {}".format(constants.shield[0], term.orange2(constants.shield[1])))
            print(" 3) Use {} {}".format(constants.item_1[0], term.orange2(constants.item_1[1])))
            print(" 4) Use {} {}".format(constants.item_2[0], term.orange2(constants.item_2[1])))

            print(" n) Display notes about {}".format(mob.name))

            key = ''
            while 1:
                key = term.inkey()                    
                if key == 'n':
                    print(term.home + term.move_down(term.height-5) + term.move_right(1) + term.clear_eos + "Notes: {}".format(textwrap.fill(mob.notes, term.width-7, break_long_words=False)))
                    term.inkey()
                    # column 1 enemy stats 
                    print(term.home + term.move_down(term.height-5) + term.clear_eol + "{:>7}{:<}".format('Name: ', mob.name))
                    print(term.clear_eol + "{:>7}{:<}".format('HP: ', ''.join(mob_hp)))
                    print(term.clear_eol + "{:>7}{:<}".format('Speed: ', mob.speed))

                    # column 2 enemy stats
                    print(term.home + term.move_down(term.height-5) + term.move_right(term.width//3) + term.clear_eol + "{:>7}{:<}".format('Weapon: ', mob.weapon[0]))
                    print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Shield: ', mob.shield[0]))
                    print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 1: ', mob.item_1[0]))
                    print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 2: ', mob.item_2[0])) 
    
                for i in range(len(self.player_action_list)):
                    if key == str(i+1):
                        print(term.home + term.move_down(11) + '{}?'.format(term.bold(self.player_action_list[i])) + ' Press enter to confirm.')
                        self.player_action = self.player_action_list[i]

                if key.is_sequence and key.name =='KEY_ENTER' and self.player_action != '':
                    break
            chance = random.randint(0, 3) # pick random number from range 0-2('up to, but not including' is pythons standard)
            if chance == 1: #if the number picked was one (1 in 3, or 30% chance)
                mob_action = mob.action_list[1] #set mob_action to 'Fumble'
            else:
                mob_action = mob.action_list[0] #set mob_action to 'Attack'

            if self.player_action == 'Attack':     
                print(term.home + term.move_down(11) + term.clear_eol +'{} {}s with {}'.format(self.player_ui.name, self.player_action, str(self.player_ui.weapon[0])))
                time.sleep(.5)
                dmg = random.randint(4,6) - random.randint(2,3)
                mob_hp = mob_hp[:-dmg]
                print(term.home + term.move_down(12) + term.clear_eol + "{} takes {} damage".format(mob.name, term.red(str(dmg))))
                time.sleep(.5)

            elif self.player_action == 'Defend':     
                print(term.home + term.move_down(11) + term.clear_eol +'{} {}s with {}'.format(self.player_ui.name, self.player_action, str(self.player_ui.shield[0])))
                time.sleep(.5)
                print('Defending halves damage from enemy attacks')
                time.sleep(.5)

            elif self.player_action == 'Item 1':     
                print(term.home + term.move_down(11) + term.clear_eol +'{} uses {}'.format(self.player_ui.name, str(self.player_ui.item_1[0])))
                dmg = random.randint(4,9) - random.randint(2,3)
                mob_hp = mob_hp[:-dmg]
                print(term.home + term.move_down(12) + term.clear_eol + "{} takes {} damage".format(mob.name, term.red(str(dmg))))
                time.sleep(.5)

            elif self.player_action == 'Item 2':     
                print(term.home + term.move_down(11) + term.clear_eol +'{} uses {}'.format(self.player_ui.name, str(self.player_ui.item_2[0])))               
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
                time.sleep(.5)
                
            # column 1 enemy stats 
            print(term.home + term.move_down(term.height-5) + term.clear_eol + "{:>7}{:<}".format('Name: ', mob.name))
            print(term.clear_eol + "{:>7}{:<}".format('HP: ', ''.join(mob_hp)))
            print(term.clear_eol + "{:>7}{:<}".format('Speed: ', mob.speed))

            # column 2 enemy stats
            print(term.home + term.move_down(term.height-5) + term.move_right(term.width//3) + term.clear_eol + "{:>7}{:<}".format('Weapon: ', mob.weapon[0]))
            print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Shield: ', mob.shield[0]))
            print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 1: ', mob.item_1[0]))
            print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 2: ', mob.item_2[0])) 

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
                print(term.home + term.move_down(14) + '{} {}s with {}'.format(mob.name, mob_action, str(mob.weapon[0])))  
                time.sleep(.5)
                dmg = random.randint(4,6) - random.randint(2,3)
                if self.player_action == 'Defend':
                    dmg = dmg//22
                self.player_ui.hp_handler(-dmg)
                print(term.home + term.move_down(15) + "{} takes {} damage".format(self.player_ui.name, term.red(str(dmg))))
                time.sleep(.5)

            if mob_action == 'Fumble':
                print(term.home + term.move_down(14) + '{} {}s'.format(mob.name, mob_action))  
                time.sleep(.5)
                dmg = 0
                print(term.home + term.move_down(15) + "{} takes {} damage".format(self.player_ui.name, term.red((str(dmg)))))
                time.sleep(.5)
            
            self.player_ui.ui_update()
            if self.player_ui.hp ==[]:
                break
            
            time.sleep(.5)
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