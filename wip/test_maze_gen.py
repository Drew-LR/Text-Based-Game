import random

maze_dict = {}
def enter(length):
    def choices_gen():
        choice_list = []
        for i, (x,y)in enumerate(rooms):
            choices = []
            #has east
            if y == length[-1]: #if current room is far east.
                pass # no east, go straight to check west
            else:
                for j, (inner_x, inner_y) in enumerate(rooms):
                    if inner_x == x and inner_y == y: # looking at current room. dont compare it to itself!
                        continue
                    if inner_x == x: # check all rooms in the same row as the current room
                        if inner_y == y+1: # if we find one of those rooms to be east of current room 
                            choices.append('East') # can go east!
                            break
            
            # has west
            if y == length[0]: #if current room is far west.
                pass # no west, go straight to check north
            else:
                for j, (inner_x, inner_y) in enumerate(rooms):
                    if inner_x == x and inner_y == y: # looking at current room. dont compare it to itself!
                        continue
                    if inner_x == x: # check all rooms in the same row as the current room
                        if inner_y == y-1: # if we find one of those rooms to be east of current room 
                            choices.append('West') # can go west!
                            break

            # has north
            if x == range(len(rows))[0]: #if current room is far north.
                if i == 0:
                    choices.append('End')
                pass # no north, go straight to check south --- actually is north and end of maze but anyway
            else:
                for j, (inner_x, inner_y) in enumerate(rooms):# check all other rooms
                    if inner_x == x and inner_y == y: # looking at current room. dont compare it to itself!
                        continue
                    if inner_x == x-1 and inner_y == y: # check the room in the same column, but row above, the current room
                        choices.append('North') # can go North!
                        break

            # has south
            if x == range(len(rows))[-1]: #if current room is far south.
                if i == range(len(rooms))[-1]:
                    choices.append('Beginning')
                pass # no south, go straight to check next iteration --- actually is south and beggining of maze but anyway
            else:
                for j, (inner_x, inner_y) in enumerate(rooms):# check all other rooms
                    if inner_x == x and inner_y == y: # looking at current room. dont compare it to itself!
                        continue
                    if inner_x == x+1 and inner_y == y: # check the room in the same column, but row below, the current room
                        choices.append('South') # can go south!
                        break
            choice_list.append(tuple(choices))
        return choice_list  

    def door_num_gen():
        door_num_list = []
        for i in choice_list:
            door_num_list.append(str(len(i)))
        return door_num_list
                
    def co_list_gen():
        master = {}
        for i in range(len(rooms)):
            master[rooms[i]] = choice_list[i]
        
        #print(master)
        co_list = []
        for k,v in master.items():
            temp_list = []
            for i in v:
                if 'East' == i:
                    temp_list.append([k[0], k[1]+1])
                elif 'West' == i:
                    temp_list.append([k[0], k[1]-1])
                elif 'South' == i:
                    temp_list.append([k[0]+1, k[1]])
                elif 'North' == i:
                    temp_list.append([k[0]-1, k[1]])
                elif 'End' == i:
                    temp_list.append('End')
                elif 'Beginning' == i:
                    temp_list.append('Beginning')
            co_list.append(temp_list) 

        long_co = []
        for item in co_list:
            long_co += item
        #print(long_co)

        long_choice = []
        for item in choice_list:
            long_choice += item
        #print(long_choice)

        # choice_co_list = []
        # for i in range(len(long_co)):
        #     choice_co_list.append((long_choice[i], long_co[i]))
            
        return co_list, long_choice, long_co



    #constants.maze = True
    length_dict = {'short' : random.randint(3, 6), 'medium' : random.randint(7,10), 'longest' : random.randint(11, 15)}

    for k,v in length_dict.items():
        if k == length:
            length = range(v)

    # Generate maze
    start_point = random.randint(0,length[-1])
    rooms = [(0,start_point)]
    x = 0
    y = 0

    i=0
    row_count =0

    while row_count < length[-1]:
        roll = []
        if rooms[i][1] != length[0]: # can go left
            roll.append('left')#so add left
            #roll.append('left')
        if rooms[i][1] != length[-1]:#can go right
            roll.append('right') # so add right
            #roll.append('right')
        roll.append('down') # always add one more for the down position

        next_room = random.choice(roll)
        if next_room == 'left':
            x += 0
            y = rooms[i][1]-1
        
        elif next_room == 'right':
            x += 0
            y = rooms[i][1]+1

        else:
            x += 1
            y = rooms[i][1]
            row_count += 1

        rooms.append((x,y))
        i+=1

    rows = []
    for i in length:
        column =[]
        for j in length:
            column.append('O')
        rows.append(column)


    for i in range(len(rooms)):
        for row, column in rooms:

            if row == i:
                rows[i][column] = 'X'

    rooms = list(dict.fromkeys(rooms)) # remove duplicates
    rooms_dict = {}
    for i, v in enumerate(rooms):
        rooms_dict[i] = v
    rooms_dict['End'] = 'End'
    rooms_dict['Beginning'] = 'Beginning'

    # key_list = key_gen()
    choice_list = choices_gen()
    door_num_list = door_num_gen()
    co_list, long_choice, long_co = co_list_gen()
    top_func = ('a.room',)
    go_to_func = ('a.go_to',)

    # generate room number of strings

    
    for i, v in enumerate(choice_list): # outer loop generates the main stem. {key, top_func, door_num, choices}
        key = (list(rooms_dict)[i],)
        stem = key + top_func + (door_num_list[i],) + (choice_list[i],)
       
        for j, k in enumerate(v): # inner loop manages the temp_stem. {string_index, go_to, coordinate}
        
            temp_stem = (str(j+1),) + go_to_func
            if k == 'East':
                for rooms_dict_key, rooms_dict_value in rooms_dict.items():
                    if rooms_dict_value == tuple(co_list[i][j]):
                        temp_stem = temp_stem + (rooms_dict_key,)
                
            elif k == 'West':
                for rooms_dict_key, rooms_dict_value in rooms_dict.items():
                    if rooms_dict_value == tuple(co_list[i][j]):
                        temp_stem = temp_stem + (rooms_dict_key,)
                
            elif k == 'South':
                for rooms_dict_key, rooms_dict_value in rooms_dict.items():
                    if rooms_dict_value == tuple(co_list[i][j]):
                        temp_stem = temp_stem + (rooms_dict_key,)
                
            elif k == 'North':
                for rooms_dict_key, rooms_dict_value in rooms_dict.items():
                    if rooms_dict_value == tuple(co_list[i][j]):
                        temp_stem = temp_stem + (rooms_dict_key,)
                
            elif k == 'End':
                for rooms_dict_key, rooms_dict_value in rooms_dict.items():
                    if rooms_dict_value == co_list[i][j]:
                        temp_stem = temp_stem + (rooms_dict_key,)
                
            elif k == 'Beginning':
                for rooms_dict_key, rooms_dict_value in rooms_dict.items():
                    if rooms_dict_value == co_list[i][j]:
                        temp_stem = temp_stem + (rooms_dict_key,)
                
            stem = stem + temp_stem
            

        
        maze_dict[stem[0]] = stem[1:]



    # for i in rows:   # for printing the map
    #     print(' '.join(i))
    print(rooms_dict)
    file = open('dump.txt', 'a')
    file.write('\n maze =')
    for i in rows:
        file.write('\n{}'.format(' '.join(i)))
    for k, v in maze_dict.items():
        file.write('\n {} : {}'.format(str(k), str(v)))
    file.close()
enter('short')


