from constants import term
import constants
import text_handler
import time

consequence_ob = text_handler.Text_handler('consequences.txt')
class Ui():
    def __init__(self):
        self.gold = 200
        self.hp = ['#','#','#','#','#']
        self.player_stance_changes = 3

    def gold_handler(self, gold_change):
        gold = self.gold

        if gold_change >= 0:
            gold += gold_change
            return(term.home + term.move_down(2) + term.clear_eol + "Gold {}".format(gold) + "   " + term.green("+{} Gold").format(gold_change))
        else:
            if abs(gold_change) > gold:
                self.gold = 0
                return consequence_ob.consequence_returner(1)
            gold += gold_change
            return(term.home + term.move_down(2) + term.clear_eol + "Gold {}".format(gold) + "   " + term.red("{} Gold").format(gold_change))
 
        self.gold = gold

    def hp_handler(self, hp_change):
        hp = self.hp

        if hp_change >= 0:
            for i in range(hp_change):
                hp.append('#')
            return(term.home + term.move_down(1) + term.clear_eol + "HP {}".format(''.join(hp)) + "   " + term.green("+{} HP").format(hp_change))
        else:
            for i in range(hp_change, 0, 1):
                hp = hp[:-1]
            return(term.home + term.move_down(1) + term.clear_eol + "HP {}".format(''.join(hp)) + "   " + term.red("{} HP").format(hp_change) + term.clear_eol)
    
        self.hp = hp
        if hp == []:
            return consequence_ob.consequence_returner(0)
        

    def ui_update(self):
        for i in range(0,9):
            print(term.move_xy(0,0+i) + term.clear_eol()) # Clear the top 9 rows
        
        print(term.home + "Name {}".format(constants.name))
        print("HP {}".format(''.join(self.hp)))
        print("Gold {}".format(self.gold))

    def empty(self, empty=''):
        if empty == 'empty':
            return ''

    


