import random
import math

# def func():
#     w = 100
#     mylist = []



#     for i in range (0,4):
#         try:
#             num = random.randrange(1, w+1)
#             w -= num
#             mylist.append(num)
#         except:
#             adjustment = max(mylist) //3
#             mylist.append(adjustment)
#             mylist[mylist.index(max(mylist))] = mylist[mylist.index(max(mylist))] - adjustment
        

# #     if sum(mylist) != 100:
# #         addition = 100 - sum(mylist)
# #         mylist[mylist.index(min(mylist))] = mylist[mylist.index(min(mylist))] + addition


# #     return mylist
    

# # print(func())

# # weapon_list = ['wooden_sword', 'stone_club', 'tree_branch']
# # hield_list = ['leather_buckler', 'pot_lid', 'uber_aegis']
# # item_list = ['magic_beans, fur_ball, ork_teeth']

# # mega_list = []
# # mega_list.append((', '.join(weapon_list),', '.join(hield_list),', '.join(item_list)))

# # print(mega_list)

# #mydick = {'0':'drew', '1':('lucas', '1.1'), '1.1':'ransley', '2': 'angie'}

# # for i in range(len(mydick)):
# #     for k,v in (mydick.items()):
# #         if str(i) == k:
# #             # if v[1] == str(1.1):
# #             #     i = float(v[1])
# #             print(k,v)


# # for k,v in mydick.items():
# #     if type(v) == tuple:
# #         print(v)


# branch = (12,13,14)
# file =open('branch.txt', 'r')
# data = file.read()
# file.close()
# para = data.split("\n\n")
# new_list = []
# for i in range(len(para)):
#     if i in branch:
#         new_list.append(para[i])

# num_list = ['1', '2', '3', '4', '5']
# mydickt= {}

# for i, v in enumerate(new_list):
#     choice_number = 0
#     for j in v:
#         if j in num_list:
#             choice_number +=1
#         mydickt[i] = choice_number


# --- this os how you would add the constraint of not having all the same rooms ---
# # but how useful is that if there are 10 rooms and 9 are the same?
# l = {'1':('method', 2), '2':('method', 2), '3':('method', 2)}

# for i in range(1,5):
#     p =2
#     for v in l.values():
#         if p != v[1]:
#             print('value not p, ok to add p')
#             break
#         else:
#             print('value same as p, back to top')
#             i-=1
#             continue
        
#     print('broke out of loop')




rooms = [(0,2)]
x = 0
y = 0
roll = []
length = range(4)
i=0

while i < length[-1]+random.randint(0,1):
    if rooms[i][1] != length[0]: # can go left
        roll.append('left')#so add left
    if rooms[i][1] == length[-1]:#can go right
        roll.append('right') # so add right
    roll.append('down') # always add one more for the down position

    next_room = random.choice(roll)
    if next_room == 'left':
        x = 0
        y = rooms[i][1]-1
    
    elif next_room == 'right':
        x = 0
        y = rooms[i][1]-2

    else:
        x = 1
        y = rooms[i][1]

    rooms.append((x,y))

rows = []
for i in range(4):
    column =[]

    for i in range(4):
        column.append('o')
    rows.append(column)





#x[0][end-1] = 'x'


for i in rows:
    print(' '.join(i))

