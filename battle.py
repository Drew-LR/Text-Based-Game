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
        self.player_action_list = []
        self.player_items = []
        self.move_list = []

    # def mobs_special_moves(move):
    #     special_dict = ['Fumble': fumble()]

    #     if move in special_dict.items():
    #         return #the corresponding function
        
    #     def fumble():
    #         #goblin does x

    def player_local_stat_setter(self, stat_type): # sets up passive stat boosts at start of battle.

        #self.player_items = [self.player_ui.weapon, self.player_ui.shield, self.player_ui.item_1, self.player_ui.item_2]
        stat = (0,0)
        for i in self.player_items: 
            if vars(i)['passive'] == 'Yes':
                if stat_type in vars(i):
                    stat = tuple(map(lambda x, y: x + y, stat, vars(i)[stat_type]))
        return stat

    def stat_buffer(self, stat_type, fighter_items):
        stat = (0,0)
        for i in fighter_items: 
            if stat_type in vars(i):
                stat = tuple(map(lambda x, y: x + y, stat, vars(i)[stat_type]))
        return stat        

    def init_battle_hud(self, mob):

        def update_hud(): #this function draws the battle HUD to the screen.

            # print the line and the enemy stats. 
            print(term.home + term.move_down(term.height-7))
            for i in range(0,term.width):
                print('_', end='')

            # column 1 enemy stats 
            print(term.home + term.move_down(term.height-5) + term.clear_eol + "{:>7}{:<}".format('Name: ', mob.name))
            if mob_local.hp <= 0:
                mob_local.hp = 0
                print(term.clear_eol + term.red("{:>7}{:<}").format('HP: ', mob_local.hp))
            elif mob_local.hp <= 3:
                print(term.clear_eol + term.red("{:>7}{:<}").format('HP: ', mob_local.hp))
            else:
                print(term.clear_eol + "{:>7}{:<}".format('HP: ', mob_local.hp))
            print(term.clear_eol + "{:>7}{:<}".format('Speed: ', mob_local.speed))

            # column 2 enemy stats
            print(term.home + term.move_down(term.height-5) + term.move_right(term.width//3) + term.clear_eol + "{:>7}{:<}".format('Weapon: ', mob.weapon.name))
            print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Shield: ', mob_local.shield.name))
            print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 1: ', mob_local.item_1.name))
            print(term.move_right(term.width//3) + term.clear_eol + "{:>8}{:<}".format('Item 2: ', mob_local.item_2.name)) 

            # print the players action choices, these are derived from weapon and items equipped.
            str_1 = term.home + term.move_down(6) + " 1) "
            str_2 = term.home + term.move_down(7) + " 2) "
            str_3 = term.home + term.move_down(8) + " 3) "
            str_4 = term.home + term.move_down(9) + " 4) "

            move_list_place = [str_1, str_2, str_3, str_4]

            for i in range(len(self.move_list)):
                print(move_list_place[i] + self.move_list[i])

            print(term.home + term.move_down(5) +" n) Display notes about {}".format(mob.name))
        
        def player_acts(go, go_string):

            if self.player_ui.speed < mob_local.speed//2:
                print(go +'{} is so slow they appear to be standing still!'.format(self.player_ui.name))
                time.sleep(.3)
                print(go + term.move_down(1) + term.clear_eol + "{} moves again".format(mob.name))
                self.player_ui.speed_handler(+1) #initiative modifier

                return

            # --- PLAYER ATTACK ---
            if self.player_action == 'Attack': #if player selects attack print 'player attacks with weapon' message.  
                print(go +'{} {}s with {}'.format(self.player_ui.name, self.player_action, str(self.player_ui.weapon.name)))
                time.sleep(.3) #wait for dramatic effect
                dmg = random.randint(self.player_ui.weapon.damage[0] + player_attack_local[0], self.player_ui.weapon.damage[1] + player_attack_local[1]) - random.randint(mob.shield.defence[0], mob.shield.defence[1])
                crit = random.randint(1,10)
                if crit == 1 or crit == 2 and go_string == 'first':
                    dmg *= 10
                if mob_action == 'Defend': # and go_string == 'second':
                    dmg = dmg//2
                if dmg < 0:
                    dmg = 0
                mob_local.hp = mob_local.hp -dmg # pick random int from weapons attack range, subtract from mob's defence range.
                self.player_ui.speed_handler(-1) #initiative modifier
                if crit == 1 or crit == 2 and go_string == 'first':
                    print(go + term.move_down(1) + term.clear_eol + "{} takes {} damage. It's a {}".format(mob.name, term.red(str(dmg)), term.orange + term.bold('Crit!')))
                else:    
                    print(go + term.move_down(1) + term.clear_eol + "{} takes {} damage".format(mob.name, term.red(str(dmg))))

                time.sleep(.3) # print the damage inflictedd to mob, then puse for dramatic effect.

            # --- PLAYER DEFEND ---
            elif self.player_action == 'Defend':  # if player selects defend print 'player defends with shield' message.
                #if go_string == 'first':   
                print(go + term.clear_eol + '{} {}s with {}'.format(self.player_ui.name, self.player_action, str(self.player_ui.shield.name)))
                time.sleep(.3) # pause for a bit
                print(go + term.move_down(1) + term.clear_eol + 'Defending halves damage from enemy attacks') # there is no output on the effect of this action unless the mob attacks.
                # else:
                #     print(go + term.clear_eol + '{} tried to defend, but was too slow'.format(self.player_ui.name))
                self.player_ui.speed_handler(1) #initiative modifier
                time.sleep(.3)

            # --- PLAYER ITEM 1 ---
            # elif self.player_action == 'Item 1':     
            #     print(term.home + term.move_down(11) + term.clear_eol +'{} uses {}'.format(self.player_ui.name, str(self.player_ui.item_1.name)))
            #     # if 'damage' in vars(local_player_ui.item_1):
                #     dmg = random.randint(self.player_ui.item_1.damage[0], self.player_ui.item_1.damage[1]) - random.randrange(mob.shield.defence[0], mob.shield.defence[1])
                #     mob_local.hp = mob_local.hp[:-dmg]
                #     self.player_ui.speed_handler(-2) #initiative modifier
                #     print(term.home + term.move_down(12) + term.clear_eol + "{} takes {} damage".format(mob.name, term.red(str(dmg))))
                #     time.sleep(.3)    

                # elif 'defence' in vars(local_player_ui.item_1):
                #     player_defence_local2 = self.stat_buffer('defence', self.player_items)
                    

                # elif effect
                    
                # --- PLAYER ITEM 2
               
                    
            update_hud() # update battle HUD again to draw any changes to the screen

        def mob_acts(go, go_string):

            if mob_local.speed < self.player_ui.speed//2:
                print(go +'{} is so slow they appear to be standing still!'.format(mob_local.name))
                time.sleep(.3)
                print(go + term.move_down(1) + term.clear_eol + "{} moves again".format(self.player_ui.name))
                mob_local.speed = mob_local.speed +1
                return

            if mob_action =='Attack': # mob attacks, print the attack message.
                print(go + term.clear_eol + '{} {}s with {}'.format(mob.name, mob_action, str(mob_local.weapon.name)))  
                time.sleep(.3)
                dmg = random.randint(mob_local.weapon.damage[0], mob_local.weapon.damage[1]) - random.randint(self.player_ui.shield.defence[0], self.player_ui.shield.defence[1])
                crit = random.randint(1,10)
                if crit == 1 or crit == 2 and go_string == 'first':
                    dmg *= 10
                if self.player_action == 'Defend':# and go_string == 'second':
                    dmg = dmg//2
                if dmg < 0:
                    dmg = 0
                self.player_ui.hp_handler(-dmg)
                if crit == 1 or crit == 2 and go_string == 'first':
                    print(go + term.move_down(1)  + "{} takes {} damage. It's a {}".format(self.player_ui.name, term.red(str(dmg)), term.orange + term.bold('Crit!')))
                else:
                    print(go + term.move_down(1)  + "{} takes {} damage".format(self.player_ui.name, term.red(str(dmg))))
                mob_local.speed = mob_local.speed -1
                time.sleep(.3)

            elif mob_action == 'Defend':
               # if  go_string == 'first':
                print(go + term.clear_eol + '{} {}s with {}'.format(mob.name, mob_action, str(mob_local.shield.name)))  
                time.sleep(.3)
                print(go + term.move_down(1) + term.clear_eol + 'Defending halves damage from {}\'s attacks'.format(self.player_ui.name)) # there is no output on the effect of this action unless the mob attacks.
                # else:
                #     print(go + term.clear_eol + '{} tried to defend, but was too slow'.format(mob_local.name))
                mob_local.speed = mob_local.speed +1 #initiative modifier
                time.sleep(.3)

            elif mob_action == 'Item 1':
                print(go + term.clear_eol + 'goblin does {}'.format(mob_action))
                print(go + term.move_down(1) + term.clear_eol + 'a thing happens')

            elif mob_action == 'Item 2':
                print(go + term.clear_eol + 'goblin does {}'.format(mob_action))
                print(go + term.move_down(1) + term.clear_eol + 'a thing happens')

            elif mob_action == 'Fumble':
                print(go + term.clear_eol + 'goblin does {}'.format(mob_action))
                print(go + term.move_down(1) + term.clear_eol + 'a thing happens')
            # else:
            #     mobs_special_moves(mob_action):
                
            self.player_ui.ui_update()
            

        print(term.home + term.move_down(9) + term.clear_eos) # clear the area below player UI
        mob_local = mob # bind the passed in mob object to a local object so the original object wont be modified. we'll want to reuse that.

        ###local_player_ui = self.player_ui
        # populate the players item list from what they have equipped at the start of the battle.
        self.player_items = [self.player_ui.weapon, self.player_ui.shield, self.player_ui.item_1, self.player_ui.item_2]
       
        # set local variables for the player's stats, this way we can manipulate them in battle and they will go back to normal after.
        player_attack_local = self.player_local_stat_setter('damage')
        player_defence_local = self.player_local_stat_setter('defence')
        #player_speed_local = ????? but how would that work

                #   ---Attack---
        if self.player_ui.weapon.name == '(Empty)':
            pass
        elif player_attack_local == (0,0):
            self.move_list.append("Attack with {}".format(self.player_ui.weapon.name) + term.orange(" ({}-{} damage)".format(self.player_ui.weapon.damage[0], self.player_ui.weapon.damage[1])))
            self.player_action_list.append('Attack')
        else:# if passive attack bonus add that to weapon stat and print the total in blue.
            self.move_list.append("Attack with {}".format(self.player_ui.weapon.name) + term.cyan3(" ({}-{} damage)".format(self.player_ui.weapon.damage[0] + player_attack_local[0], self.player_ui.weapon.damage[1] + player_attack_local[1])))
            self.player_action_list.append('Attack')
        
        #   ---Defend---
        if self.player_ui.shield.name == '(Empty)':
            pass
        elif player_defence_local == (0,0): # no passive defence
            self.move_list.append("Defend with {}".format(self.player_ui.shield.name) + term.orange(" ({}-{} defence)".format(self.player_ui.shield.defence[0], self.player_ui.shield.defence[1])))
            self.player_action_list.append('Defend')
        else: # with passive defence
            self.move_list.append("Defend with {}".format(self.player_ui.shield.name) + term.cyan3(" ({}-{} defence)".format(self.player_ui.shield.defence[0] + player_defence_local[0], self.player_ui.shield.defence[1] + player_defence_local[1])))
            self.player_action_list.append('Defend')

        #   ---Item 1---
        if self.player_ui.item_1.name == '(Empty)':
            pass
        elif vars(self.player_ui.item_1)['passive']== 'Yes':
            pass
        else:
            self.move_list.append("Use {}".format(self.player_ui.item_1.name) + term.orange2(" ({})".format(self.player_ui.item_1.battle_descrip)))    
            self.player_action_list.append('Item 1')

        #   ---Item 2---
        if self.player_ui.item_2.name == '(Empty)':
            pass
        elif vars(self.player_ui.item_2)['passive']== "Yes":
            pass
        else:
            self.move_list.append("Use {}".format(self.player_ui.item_2.name) + term.orange2(" ({})".format(self.player_ui.item_2.battle_descrip)))
            self.player_action_list.append('Item 2')


        while mob_local.hp != 0 and self.player_ui.hp != 0: # do this untill mob or player runs out of HP. 
            print(term.home + term.move_down(9) + term.clear_eos) # clear the area below player UI

            self.player_action = '' # initialise player and mob action, this is the action they choose each turn. 
            
            # use mob.action_weight to determine the mobs move! (selected from mob.action_list)
            num = random.randint(1,100)
            for i, (j,k) in enumerate(mob_local.action_weight):
                if num in range(j,k):
                    action_choice = i
            try:
                mob_action = mob_local.action_list[action_choice]
            except:
                file = open('dump.txt', 'a')
                file.write('action choice referenced before assignment {}  {}  {}'.format(str(mob_local.action_weight), str(i), str(mob_local.action_list)))
                file.close()
                return

            update_hud() # print the battle HUD for the first time

            # --- TURN LOOP ---   
            while 1: # begin the turn loop, allows the player to select action/note inputs, change their mind, and eventually confirm with ENTER.
                key = term.inkey() # reads key input from the player.                
                if key == 'n': # pressing 'n' shows some notes about the mob.
                    print(term.home + term.move_down(term.height-5) + term.move_right(1) + term.clear_eos + "Notes: {}".format(textwrap.fill(mob.notes, term.width-7, break_long_words=False)))
                    term.inkey() # pressing any key while note are showing hides them and brings back the battle HUD
                    update_hud() 
    
                for i in range(len(self.player_action_list)): # check each index of the players 'action_list' (0-3).
                    if key == str(i+1): # if key matches 'action_list' index (0-3), but plus 1 so (1-4) because we are using keys 1-4. print a prompt shoing the player what they are choosing. 
                        print(term.home + term.move_down(11) + '{}?'.format(term.bold(self.player_action_list[i])) + ' Press enter to confirm.')
                        self.player_action = self.player_action_list[i] # set 'self.player_action' to whatever the player has selected.

                if key.is_sequence and key.name =='KEY_ENTER' and self.player_action != '': # if player presses enter their currently selected action is chosen.
                    break # we break out of the turn loop.


            # ---  END TURN LOOP --- time to do the end-of-turn combobulations!!
            #these are the locations the first goer and the second goer.
            first = term.home + term.move_down(11)
            second = term.home + term.move_down(14)

            # determine who goes first by calculating initiative
            if self.player_ui.speed > mob_local.speed:
                            
                player_acts(first, 'first')
                
                if mob_local.hp == 0: # check if goblin died as a result of player's turn, if so break from loop
                    break

                time.sleep(.3)
                print(term.home + term.move_down(13) + '. ')
                time.sleep(.3)
                print(term.home + term.move_down(13) + term.move_right(1) + '. ')
                time.sleep(.3)
                print(term.home + term.move_down(13) + term.move_right(2) + '. ')
                time.sleep(.3)

                mob_acts(second, 'second')
                if self.player_ui.hp == 0: # check if player died as a result of mob's turn, if so break from loop
                    break

            else: # if mob has initiative do these things
                mob_acts(first, 'first')
                
                if self.player_ui.hp == 0: # check if player died as a result of mob's turn, if so break from loop
                    break

                time.sleep(.3)
                print(term.home + term.move_down(13) + '. ')
                time.sleep(.3)
                print(term.home + term.move_down(13) + term.move_right(1) + '. ')
                time.sleep(.3)
                print(term.home + term.move_down(13) + term.move_right(2) + '. ')
                time.sleep(.3)

                player_acts(second, 'second')
                if mob_local.hp == 0: # check if goblin died as a result of player's turn, if so break from loop
                    break

            time.sleep(.3)
            print(term.home + term.move_down(17) + 'Press enter to start next turn.')

            if key.is_sequence:
                key = ''
            while 1:
                key = term.inkey()
                if key.is_sequence and key.name == "KEY_ENTER":
                    break      

        if mob_local.hp == 0:
            return term.home + term.move_down(17) + term.clear_eol + '{} slays {}'.format(self.player_ui.name, mob.name)      
        elif self.player_ui.hp == 0:
            return term.home + term.move_down(17) + term.clear_eol + 'You were slain by {}'.format(mob.name)