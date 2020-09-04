from constants import term
import blessed
import text_handler
import ui
import battle
import mobs_lib

# def diverge_return():

#     local_dict = {
#         '7.1' :  (shop_ob.shop, 0, '1', ui_ob.empty,'empty'),
#         '7.2' :  (shop_ob.shop, 1, '1', ui_ob.empty,'empty'),
#         '7.3' :  (shop_ob.shop, 2, '1', ui_ob.empty,'empty'),
#         '7.4' :  (shop_ob.shop, 3, '1', ui_ob.empty,'empty'),
#         '7.5' :  (shop_ob.shop, 4, '1', ui_ob.empty,'empty'),
#     }
#     for i in local

yn_ob = text_handler.Text_handler('ynq.txt')
open_ob = text_handler.Text_handler('open_question.txt')
story_ob = text_handler.Text_handler('story_text.txt')
ui_ob = ui.Ui()
battle_text_ob = text_handler.Text_handler('battle_init.txt')
shop_ob = text_handler.Text_handler('shop.txt')

battle_ob = battle.Battle(ui_ob)

game_over_ob = text_handler.Text_handler('game_over.txt')

# The event dictionary stores all game events in chronological order. k,v pairs are processed by the 'game_events' function in 'event_handler.py'
# 'Keys' in this dict are always numbers, in chronoligical order.
# Each key's 'value', is a tuple of 'values', in the format; function - parameters for that function, function - parameters for that function, and so on.
# The first 'value' in the tuple is a function call to whichever event type we currently want, i.e story text, 
# a battle, a choice to be made by the player etc. Lets call that the 'top level function'.
# 'Values' following the 'top level function' are fed to that function by the 'game_events' function in 'event_handler.py'.
# 'Values' following any other 'lower level function' in the tuple are fed to that function by the 'top level function'.
# As at 1/8/20 only the 'top level function' takes other function calls as arguments. 'lower level functions' only take parameter values. 

main_dict = {
    '0' : (story_ob.story_txt, 0), # story paragrahp 1
    '1' : (story_ob.story_txt, 1), # story paragraph 2
    '2' : (yn_ob.yn_txt, 1, ui_ob.empty, 'empty', game_over_ob.game_over, 1), # accept quest option
    '3' : (yn_ob.yn_txt, 0, ui_ob.gold_handler, 200, ui_ob.empty, 'empty'), #take the money question
    '4' : (story_ob.story_txt, 3), # reading the note
    '5' : (open_ob.open_q, 2, '1', ui_ob.empty, 'empty'), # remember to prepare for your quest
    '6' : (open_ob.open_q, 0, '1',ui_ob.empty, 'empty', '2', ui_ob.hp_handler, -2), # open the door question
    '7' : (story_ob.story_txt, 4), # the librarian speaks
    '8' : (open_ob.open_q, 1, '1', ui_ob.hp_handler, 10, '2', ui_ob.hp_handler, -10, '3', ui_ob.gold_handler, 100, '4', ui_ob.gold_handler, -100), # do all the things question
    '9' : (story_ob.story_txt, 9), # librarian celebrates, goblin appears
    '10' : (battle_text_ob.battle_text, 0, battle_ob.init_battle_hud, mobs_lib.goblin), # fight the goblin
    '11': (game_over_ob.game_over, 2) # the goblin slain!
    }

new_dict = {
        '3.1' :  (story_ob.story_txt, 2), #his eyes light up
        '6.1' :  (shop_ob.shop, 0, '1', ui_ob.empty,'empty', '2', ui_ob.empty, 'empty', '3', ui_ob.empty, 'empty', '4', ui_ob.empty, 'empty', '5', ui_ob.empty, 'empty'), # int he RAA, where to visit?
        '6.2' :  (shop_ob.shop, 1, '1', ui_ob.hp_handler, 10,'2', ui_ob.empty,'empty', '3', ui_ob.empty,'empty'), #rooms
        '6.3' :  (shop_ob.shop, 2, '1', ui_ob.empty,'empty', '2', ui_ob.empty,'empty', '3', ui_ob.empty,'empty'), #bar
        '6.4' :  (shop_ob.shop, 3, '1', ui_ob.empty,'empty', '2', ui_ob.empty,'empty', '3', ui_ob.empty,'empty'), # potion
        '6.5' :  (shop_ob.shop, 4, '1', ui_ob.empty,'empty', '2', ui_ob.empty,'empty', '3', ui_ob.empty,'empty'), #smith
        '9.1' : (story_ob.story_txt, 5), # add hp
        '9.2' : (story_ob.story_txt, 6), # sub hp
        '9.3' : (story_ob.story_txt, 7), # add coin
        '9.4' : (story_ob.story_txt, 8), # sub coin


        '99'  : (game_over_ob.game_over, 0), # game over screen for hp < 0.
        '100' : () # game over condition for game events.
}