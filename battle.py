from constants import term
import random

class Mob():
    def __init__(self, name, hp, stance_change):
        self.name = name
        self.hp = hp
        self.mob_stance_changes = stance_change
        

class Battle():
    def __init__(self, player_ui):
        self.player_stance_change = 3
        self.player_ui = player_ui
        self.display_timer = ['#', '#', '#', '#', '#', '#','#', '#', '#', '#']
        self.turn_number = 1
        self.stance_list = ['attack', 'defend', 'special']
        self.player_current_stance = 'defend'
        self.mob_current_stance = 'defend'


    def init_battle_hud(self, mob):
        mob_hp = mob.hp

        while mob_hp != [] and self.player_ui.hp != []:

            self.player_current_stance = 'defend'
            mob_current_stance = 'defend'

            print(term.home + term.move_down(9) + term.clear_eos)
            print(term.home + term.move_down(10) + term.clear_eos + " " + mob.name)
            print("HP {}".format(''.join(mob_hp)))
            print("Stance changes {}".format(mob.mob_stance_changes))
            print("Current stance {}".format(mob_current_stance))
            
            print(term.home + term.move_down(10) + term.move_right(term.width//2) + "Player")
            print(term.move_right(term.width//2) + "HP {}".format(''.join(self.player_ui.hp)))
            print(term.move_right(term.width//2) + "Stance changes {}".format(self.player_ui.player_stance_changes))
            print(term.move_right(term.width//2) + "Current stance {}".format(self.player_current_stance))

            print(term.home + term.move_down(18) + "Press enter to engage the enemy...")

            current_key =''
            while self.player_ui.player_stance_changes > 0:
                key = term.inkey()
                for i in range(len(self.stance_list)):
                    if key == str(i+1) and key != current_key:

                        # Player changes stance
                        current_key = str(i+1)
                        self.player_ui.player_stance_changes -= 1
                        self.player_current_stance = self.stance_list[i]

                        # mob randomly changes stance
                        mob_key = random.randint(0,2)
                        if mob_key != i:
                            mob_current_stance = self.stance_list[mob_key]
                        
                        # Update mob's selected stance
                        print(term.home + term.move_down(13) + term.clear_eol + "Current stance {}".format(mob_current_stance))

                        # Update player's selected stance
                        print(term.home + term.move_down(17) + term.clear_eol + "Stance changed to {}".format(self.player_current_stance))
                        print(term.home + term.move_down(12) + term.move_right(term.width//2) + term.clear_eol + "Stance changes {}".format(self.player_ui.player_stance_changes))
                        print(term.move_right(term.width//2) + term.clear_eol + "Current stance {}".format(self.player_current_stance))

                    elif key.is_sequence and key.name == "KEY_ENTER":
                        self.player_ui.player_stance_changes = 0  

            self.player_ui.player_stance_changes = 3
            
            
        
            print(term.home + term.move_down(15) + term.clear_eos + "{} ".format(mob.name) + "{}".format(mob_current_stance) + "s")
            print(term.home + term.move_down(15) + term.move_right(term.width//2) + "Player {}".format(self.player_current_stance) + "s")
            print(term.home + term.move_down(18) + 'Press enter to start next turn...')
            
            if self.player_current_stance == mob_current_stance:
                print(term.home + term.move_down(17) + term.clear_eol + 'And nothing was achieved')

            elif self.player_current_stance == 'attack' and mob_current_stance == 'special':
                print(term.home + term.move_down(17) + term.clear_eol + 'player lands an attack')
                mob_hp = mob_hp[:-1]
                print(term.home + term.move_down(11) + term.clear_eol + "HP {}".format(''.join(mob_hp)) + "  " + term.red("-1"))
                print(term.home + term.move_down(11) + term.move_right(term.width//2) + term.clear_eol + "HP {}".format(''.join(self.player_ui.hp)))

            elif self.player_current_stance == 'defend' and mob_current_stance == 'attack': 
                print(term.home + term.move_down(17) + term.clear_eol + 'player fends off an attack')

            elif self.player_current_stance == 'special' and mob_current_stance == 'defend': 
                print(term.home + term.move_down(17) + term.clear_eol + 'player lands a special!')
                mob_hp = mob_hp[:-2]
                print(term.home + term.move_down(11) + term.clear_eol + "HP {}".format(''.join(mob_hp)) + "  " + term.red("-2"))
                print(term.home + term.move_down(11) + term.move_right(term.width//2) + term.clear_eol + "HP {}".format(''.join(self.player_ui.hp)))


            elif self.player_current_stance == 'special' and mob_current_stance == 'attack':
                print(term.home + term.move_down(17) + term.clear_eol + 'player is hit by an attack')
                self.player_ui.hp = self.player_ui.hp[:-1]
                print(term.home + term.move_down(11) + term.move_right(term.width//2) + term.clear_eol + "HP {}".format(''.join(self.player_ui.hp) + "  " + term.red("-1")))

            elif self.player_current_stance == 'attack' and mob_current_stance == 'defend': 
                print(term.home + term.move_down(17) + term.clear_eol + 'player\'s attack has no effect')

            elif self.player_current_stance == 'defend' and mob_current_stance == 'special': 
                print(term.home + term.move_down(17) + term.clear_eol + 'player is hit by a special!')
                self.player_ui.hp = self.player_ui.hp[:-2]
                print(term.home + term.move_down(11) + term.move_right(term.width//2) + term.clear_eol + "HP {}".format(''.join(self.player_ui.hp) + "  " + term.red("-2")))

            self.player_ui.ui_update()
            while 1:
                key = term.inkey()
                if key.is_sequence and key.name == "KEY_ENTER":
                    break

        if mob_hp == []:
            return term.home + term.move_down(10) + term.clear_eos + 'Player slays {}'.format(mob.name)       
        elif self.player_ui.hp == []:
            return term.home + term.move_down(10) + term.clear_eos + 'You were slain by {}'.format(mob.name)