from constants import term

class Items():
    def __init__(self, name, descrip, passive='No', battle_descrip=None, damage=(0,0), defence=(0,0), effect='No', chance=None):

        self.name = name
        self.descrip = descrip
        self.battle_descrip = battle_descrip
        self.damage = damage
        self.defence = defence
        self.chance = chance
        self.passive = passive
    
no_item = Items('(Empty)', 'Nothing equipped', '')

# weapons
wooden_sword = Items('Wooden Sword', 'A memento of youthful days spent fighting Lv.1 slimes', damage=(4,6), chance=95)
tree_branch = Items('Tree Branch', 'The least weapony weapon.', damage=(1,1), chance=90)
stone_club = Items('Stone Club', 'A naturally occuring lump of stone, only a weapon if you swing it', damage=(3,8), chance=85)
non_wooden_sword = Items('Non-Wooden Sword', 'A memento of youthful days spent fighting Lv.1 slimes', damage=(4,6), chance=95)

# shields
leather_buckler = Items('Leather Buckler', 'Very much a beginners shield', defence=(1,3))
pot_lid = Items('Pot Lid', 'Perhaps better cooked with, it is as advertised', defence=(1,1))
uber_aegis = Items('Uber Aegis', 'A shield to test all the other punny shields', defence=(50,99))

# items
magic_beans = Items('Magic Beans', 'Deadly poisonous beans, not exactly a weapon unless they get in your opponent\'s mouth', battle_descrip='Poisonous beans! Aim for your opponents mouth', defence=(999999999,999999999), chance=10)
ork_teeth = Items('Ork Teeth', 'The gnarly, disembodied teeth of an ork. Scatter like caltrops to lower an opponents movement and morale.', effect=(1,2), chance=95)

# passive items
fur_ball = Items('Fur Ball', 'Could be construed as cute, one wonders about it\'s applications for battle', passive='Yes', damage=(10,20))


weapon_list = [wooden_sword, stone_club, tree_branch]
hield_list = [leather_buckler, pot_lid, uber_aegis]
item_list = [magic_beans, fur_ball, ork_teeth]