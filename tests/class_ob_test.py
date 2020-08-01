

class Mob():
    def __init__(self, hp):
        self.hp = hp


mob_ob = Mob(100)

def change_hp(object):
    new_hp_object = object.hp
    print("object hp", object.hp)
    new_hp_object -= 50
    print(new_hp_object)
    print("object hp mod", object.hp)

print("mob hp", mob_ob.hp)

change_hp(mob_ob)

print('mob hp after', mob_ob.hp)
print(new_hp_object)
