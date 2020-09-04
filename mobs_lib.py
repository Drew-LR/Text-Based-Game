import battle
import items_lib
import random

# template  _dict = {'name':[], 'hp': [],'speed':[], 'weapon':[], 'shield':[], 'item_1':[], 'item_2':[], 'notes': [], 'unique_action_list' :''}

# hereforth be the mob dictionaries
goblin_dict = {'name':['Goblin'], 'hp':[100,80,60],'speed':[3, 5, 7], 'weapon':[items_lib.wooden_sword, items_lib.stone_club, items_lib.tree_branch], 'shield':[items_lib.leather_buckler,items_lib.no_item, items_lib.pot_lid], 'item_1':[items_lib.ork_teeth,items_lib.magic_beans,items_lib.fur_ball, items_lib.no_item], 'item_2':[items_lib.no_item], 'notes':['Goblins are hostile and mischievous. They will attempt to ambush opponents for valuable loot. Luckily they are also notably clumsy, rendering them mostly harmless.'], 'unique_action_list':'Fumble'}

mungo_dict = {'name':['Mungo'], 'hp': [10],'speed':[10], 'weapon':[items_lib.stone_club], 'shield':[items_lib.uber_aegis], 'item_1':[items_lib.no_item], 'item_2':[items_lib.no_item], 'notes': ['Mungo is the latest mob, good for him.'], 'unique_action_list':'Mung'}

def mob_spawner(mob_dict):

    def weighter(action_list):# assign a weight (probability of mob choosing) to each action
        weight_list = []
        w =100
        pre = 1
        for i in range(len(action_list)):
            try:
                if i == len(action_list) -1:
                    weight_list.append((pre, 100))
                    break
                num = random.randrange(pre, w)
                weight_list.append((pre,num))
                pre = num +1
            except:
                weight_list = weighter(action_list)
                return weight_list
        return weight_list

    mob_list = []
    action_list = []

    for k, v in mob_dict.items(): # take one option for each key to populate mob stats and equips
        if k == 'unique_action_list': # but ignore unique_action_list until later
            continue
        attribute = random.choice(v)
        mob_list.append(attribute)

    for k, v in mob_dict.items(): # populate an action_list with unique actions 
        if k == 'unique_action_list':
            action_list.append(v)

    # add actions based on available equips to action_list
    if mob_list[3] != items_lib.no_item:
        action_list.append('Attack')
    if mob_list[4] != items_lib.no_item:
        action_list.append('Defend')
    if mob_list[5] != items_lib.no_item:
        action_list.append('Item 1')
    if mob_list[6] != items_lib.no_item:
        action_list.append('Item 2')

    weight_list = weighter(action_list)

    mob_list.append(action_list)
    mob_list.append(weight_list)
    return mob_list

class Mob():
    def __init__(self, name, hp, speed, weapon, shield, item_1, item_2, notes, action_list, action_weight):
        self.name = name
        self.hp = hp 
        self.speed = speed 

        self.weapon = weapon
        self.shield = shield
        self.item_1 = item_1
        self.item_2 = item_2
        self.action_list = action_list
        self.action_weight = action_weight 

        self.notes = notes



# Objects for mob types
goblin = Mob(*mob_spawner(goblin_dict))
mungo = Mob(*mob_spawner(mungo_dict))
print(vars(goblin))