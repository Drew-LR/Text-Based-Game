# # import random
# # import math
# # import blessed
# import constants

# # term = blessed.Terminal()

# # # def func():
# # #     w = 100
# # #     mylist = []



# # #     for i in range (0,4):
# # #         try:
# # #             num = random.randrange(1, w+1)
# # #             w -= num
# # #             mylist.append(num)
# # #         except:
# # #             adjustment = max(mylist) //3
# # #             mylist.append(adjustment)
# # #             mylist[mylist.index(max(mylist))] = mylist[mylist.index(max(mylist))] - adjustment
        

# # # #     if sum(mylist) != 100:
# # # #         addition = 100 - sum(mylist)
# # # #         mylist[mylist.index(min(mylist))] = mylist[mylist.index(min(mylist))] + addition


# # # #     return mylist
    

# # # # print(func())

# # # # weapon_list = ['wooden_sword', 'stone_club', 'tree_branch']
# # # # hield_list = ['leather_buckler', 'pot_lid', 'uber_aegis']
# # # # item_list = ['magic_beans, fur_ball, ork_teeth']

# # # # mega_list = []
# # # # mega_list.append((', '.join(weapon_list),', '.join(hield_list),', '.join(item_list)))

# # # # print(mega_list)

# # # #mydick = {'0':'drew', '1':('lucas', '1.1'), '1.1':'ransley', '2': 'angie'}

# # # # for i in range(len(mydick)):
# # # #     for k,v in (mydick.items()):
# # # #         if str(i) == k:
# # # #             # if v[1] == str(1.1):
# # # #             #     i = float(v[1])
# # # #             print(k,v)


# # # # for k,v in mydick.items():
# # # #     if type(v) == tuple:
# # # #         print(v)


# # # branch = (12,13,14)
# # # file =open('branch.txt', 'r')
# # # data = file.read()
# # # file.close()
# # # para = data.split("\n\n")
# # # new_list = []
# # # for i in range(len(para)):
# # #     if i in branch:
# # #         new_list.append(para[i])

# # # num_list = ['1', '2', '3', '4', '5']
# # # mydickt= {}

# # # for i, v in enumerate(new_list):
# # #     choice_number = 0
# # #     for j in v:
# # #         if j in num_list:
# # #             choice_number +=1
# # #         mydickt[i] = choice_number


# # # --- this os how you would add the constraint of not having all the same rooms ---
# # # # but how useful is that if there are 10 rooms and 9 are the same?
# # # l = {'1':('method', 2), '2':('method', 2), '3':('method', 2)}

# # # for i in range(1,5):
# # #     p =2
# # #     for v in l.values():
# # #         if p != v[1]:
# # #             print('value not p, ok to add p')
# # #             break
# # #         else:
# # #             print('value same as p, back to top')
# # #             i-=1
# # #             continue
        
# # #     print('broke out of loop')




# # rooms = [(0,2)]
# # x = 0
# # y = 0

# # length = range(4)
# # i=0
# # row_count =0

# # while row_count < length[-1]:
# #     roll = []
# #     if rooms[i][1] != length[0]: # can go left
# #         roll.append('left')#so add left
# #         #roll.append('left')
# #     if rooms[i][1] != length[-1]:#can go right
# #         roll.append('right') # so add right
# #         #roll.append('right')
# #     roll.append('down') # always add one more for the down position

# #     next_room = random.choice(roll)
# #     if next_room == 'left':
# #         x += 0
# #         y = rooms[i][1]-1
    
# #     elif next_room == 'right':
# #         x += 0
# #         y = rooms[i][1]+1

# #     else:
# #         x += 1
# #         y = rooms[i][1]
# #         row_count += 1

# #     rooms.append((x,y))
# #     i+=1

# # rows = []
# # for i in length:
# #     column =[]
# #     for j in length:
# #         column.append('O')
# #     rows.append(column)


# # for i in range(len(rooms)):
# #     for row, column in rooms:
   
# #         if row == i:
# #             rows[i][column] = 'X'

# # # for i in rows:
# # #     print(' '.join(i))

# # # for i in rows: #populate random battles
# # #     for j in range(len(i)):
# # #         if i[j] == 'X':
# # #             battle = random.randint(1,4) # from a pre determined stat, can be higher for harder dungeons
# # #             if battle == 1:
# # #                 i[j] = 'B'

# # print('')
# # for i in rows:
# #     print(' '.join(i))

# # rooms = list(dict.fromkeys(rooms)) # remove duplicates


# # # for i in rooms:
# # #     top_func = ('a.room,')
# # #     go_to_func = ('a.go_to,')

# # #    for i in rooms:
# # #        key = (str(i),) #make a '(0,2)' type object to use as key. romms is just a list of corordinates.

# #     #check number of doors [(3, 1), (2, 1), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2)]
# # choice_list = []
# # for i, (x,y)in enumerate(rooms):
# #     choices = []
# #     #has east
# #     if y == length[-1]: #if current room is far east.
# #         pass # no east, go straight to check west
# #     else:
# #         for j, (inner_x, inner_y) in enumerate(rooms):
# #             if inner_x == x and inner_y == y: # looking at current room. dont compare it to itself!
# #                 continue
# #             if inner_x == x: # check all rooms in the same row as the current room
# #                 if inner_y == y+1: # if we find one of those rooms to be east of current room 
# #                     choices.append('East') # can go east!
# #                     break
    
# #     # has west
# #     if y == length[0]: #if current room is far west.
# #         pass # no west, go straight to check north
# #     else:
# #         for j, (inner_x, inner_y) in enumerate(rooms):
# #             if inner_x == x and inner_y == y: # looking at current room. dont compare it to itself!
# #                 continue
# #             if inner_x == x: # check all rooms in the same row as the current room
# #                 if inner_y == y-1: # if we find one of those rooms to be east of current room 
# #                     choices.append('West') # can go west!
# #                     break

# #     # has north
# #     if x == range(len(rows))[0]: #if current room is far north.
# #         if i == 0:
# #             choices.append('End')
# #         pass # no north, go straight to check south --- actually is north and end of maze but anyway
# #     else:
# #         for j, (inner_x, inner_y) in enumerate(rooms):# check all other rooms
# #             if inner_x == x and inner_y == y: # looking at current room. dont compare it to itself!
# #                 continue
# #             if inner_x == x-1 and inner_y == y: # check the room in the same column, but row above, the current room
# #                 choices.append('North') # can go North!
# #                 break

# #     # has south
# #     if x == range(len(rows))[-1]: #if current room is far south.
# #         if i == range(len(rooms))[-1]:
# #             choices.append('Beginning')
# #         pass # no south, go straight to check next iteration --- actually is south and beggining of maze but anyway
# #     else:
# #         for j, (inner_x, inner_y) in enumerate(rooms):# check all other rooms
# #             if inner_x == x and inner_y == y: # looking at current room. dont compare it to itself!
# #                 continue
# #             if inner_x == x+1 and inner_y == y: # check the room in the same column, but row below, the current room
# #                 choices.append('South') # can go south!
# #                 break
# #     choice_list.append(choices)
# # # print(rooms) 
# # # print(choice_list)



# # # co_list = []

# # # for i, (x,y) in enumerate(rooms):
# # #     temp_list =[]
# # #     for j in choice_list:
# # #         for v in j:
# # #             if 'East' == v:
# # #                 print('east door{}'.format((x,y-1)))
# # #             if 'West' == v:
# # #                 print('wesr door{}'.format((x,y+1)))
# # #             if 'South' == v:
# # #                 print('south door{}'.format((x+1,y)))
# # #             if 'North' == v:
# # #                 print('north door{}'.format((x-1,y)))
# # #             if 'End' == v:
# # #                 print('end door{}'.format(('End')))
# # #             if 'Beginning' == v:
# # #                 print('Beggining door{}'.format(('Beginning')))


# # # 

# # # for i, j in enumerate(choice_list):
# # #     temp_list = []          
# # #     for v in j:
# # #         if 'East' == v:
# # #             temp_list.append(rooms[i][0][1])
# # #             print('at ({}, {}), to go {} take {}'.format(x, y, v, temp_list[i]))
# # #         elif 'West' == v:
# # #             temp_list.append([x,y-1])
# # #             print('at ({}, {}), to go {} take {}'.format(x, y, v, temp_list[i]))
# # #         elif 'South' == v:
# # #             temp_list.append([x+1,y])
# # #             print('at ({}, {}), to go {} take {}'.format(x, y, v, temp_list[i]))
# # #         elif 'North' == v:
# # #             temp_list.append([x-1,y])
# # #             print('at ({}, {}), to go {} take {}'.format(x, y, v, temp_list[i]))
# # #         elif 'End' == v:
# # #             temp_list.append('End')
# # #             print('at ({}, {}), to go {} take {}'.format(x, y, v, temp_list[i]))
# # #         elif 'Beginning' == v:
# # #             temp_list.append('Begining')
# # #             print('at ({}, {}), to go {} take {}'.format(x, y, v, temp_list[i]))
# # #         continue
# # #     co_list.append(temp_list)
# # # print(co_list)

# # master = {}
# # for i in range(len(rooms)):
# #     master[rooms[i]] = choice_list[i]
 
# # print(master)
# # co_list = []
# # for k,v in master.items():
# #     temp_list = []
# #     for i in v:
# #         if 'East' == i:
# #             temp_list.append((k[0], k[1]+1))
# #         elif 'West' == i:
# #             temp_list.append((k[0], k[1]-1))
# #         elif 'South' == i:
# #             temp_list.append((k[0]+1, k[1]))
# #         elif 'North' == i:
# #             temp_list.append((k[0]-1, k[1]))
# #         elif 'End' == i:
# #             temp_list.append('End')
# #         elif 'Beginning' == i:
# #             temp_list.append('Begining')
# #     co_list.append(temp_list)

# # print(co_list)




# # # rooms a list of tuple coordinates
# # # choices list. tells us how many doors are in the rooms from room list. and which way they point.

      
                
# #             # if v == 'West':
# #             #     print('west {}, {}'.format(rooms[i], rooms[i+1]))
# #             #     ##temp_list.append(rooms[i-1])
# #             # if v == 'South':
# #             #     print('south {}, {}'.format(rooms[i], rooms[i+1]))
# #             # if v == 'North':
# #             #     print('north {}, {}'.format(rooms[i], rooms[i+1]))
# #             # if v == 'End':
# #             #     print('end {}, {}'.format(rooms[i], rooms[i+1]))
# #             # if v == 'Beginning':
# #             #     print('beginning {}, {}'.format(rooms[i], rooms[i+1]))
        
# # # for i, j in enumerate(choice_list):
# # #     temp_list = []
# # #     for k, v in enumerate(j):
# # #         if v == 'East':
# # #             print('east {}, {}'.format(rooms[i], rooms[i+1]))
# # #             temp_list.append(rooms[i+1])
# # #         if v == 'West':
# # #             print('west {}, {}'.format(rooms[i], rooms[i+1]))
# # #             ##temp_list.append(rooms[i-1])
# # #         if v == 'South':
# # #             print('south {}, {}'.format(rooms[i], rooms[i+1]))
# # #         if v == 'North':
# # #             print('north {}, {}'.format(rooms[i], rooms[i+1]))
# # #         if v == 'End':
# # #             print('end {}, {}'.format(rooms[i], rooms[i+1]))
# # #         if v == 'Beginning':
# # #             print('beginning {}, {}'.format(rooms[i], rooms[i+1]))
        
# #     #temp_list.append(str(i), rooms[i], )



# #     #print("{} : ({}, {}) : {}".format(str(i), str(x), str(y), str(choices)))

# # #door_num = 4# must know how many doors a room has. the same value as there are option strings to add
    
# #  #{'(0,2)' : (a.room, 3, ('North', 'South', 'West'), '1', a.go_to, 5.2, '2', a.go_to, 5.2, '3', a.go_to, 5),
# # #  key       top_func door_num  choices            choice_num goto  co  choice_num got co choice_num goto co   


            
   

# # # for j in choice_list:
# # #     temp_list = []          
# # #     for v in j:
# # #         if 'East' == v:
# # #             temp_list.append([x,y+1])
# # #             print('at ({}, {}), to go {} take {}'.format(x, y, v, temp_list[i]))
# # #         elif 'West' == v:
# # #             temp_list.append([x,y-1])
# # #             print('at ({}, {}), to go {} take {}'.format(x, y, v, temp_list[i]))
# # #         elif 'South' == v:
# # #             temp_list.append([x+1,y])
# # #             print('at ({}, {}), to go {} take {}'.format(x, y, v, temp_list[i]))
# # #         elif 'North' == v:
# # #             temp_list.append([x-1,y])
# # #             print('at ({}, {}), to go {} take {}'.format(x, y, v, temp_list[i]))
# # #         elif 'End' == v:
# # #             temp_list.append('End')
# # #             print('at ({}, {}), to go {} take {}'.format(x, y, v, temp_list[i]))
# # #         elif 'Beginning' == v:
# # #             temp_list.append('Begining')
# # #             print('at ({}, {}), to go {} take {}'.format(x, y, v, temp_list[i]))
# # #         continue
# # #     co_list.append(temp_list)
# # # print(co_list)


# print(constants.rows)

dic = {'1': 'one', '2': 'two', '3': 'three'}

print(dic)
print(dic(reversed))

#print(list(dic.keys())[-1])
