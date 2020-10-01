class Maze():

    def gen(self, length):
        rooms = [(0, length[-1])]
        x = 0
        y = 0

        i=0
        row_count =0

        while row_count < length[-1]:
            roll = []
            if rooms[i][1] != length[0]: # can go left
                roll.append('left')#so add left
            if rooms[i][1] != length[-1]:#can go right
                roll.append('right') # so add right
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
                column.append('o')
            rows.append(column)


        for i in range(len(rooms)):
            for row, column in rooms:
        
                if row == i:
                    rows[i][column] = 'x'

        for i in rows:
            print(' '.join(i))



    def exit(self, para=0):
        
        constants.maze_exit = True
        return ''

    def enter(self, length):
        constants.maze = True

        length_dict = {'short' : random.randint(2, 5), 'medium' : random.randint(6,9), 'longest' : random.randint(10, 15)}

        length = length

        branch = []
        for i in range(len(branch_tup)):
            branch.append(branch_tup[i])

        file =open('branch.txt', 'r')
        data = file.read()
        file.close()
        para = data.split("\n\n") # open branch.txt and read it in.

        branch_options = []
        for i in range(len(para)):
            if i in branch:
                branch_options.append(para[i]) # make a list of the branching options specified in 'branch'.
                
        num_list = ['1', '2', '3', '4', '5'] # list of possible answers.
        branch_dict = {}
        
        for i, v in enumerate(branch_options): # iterate through the branchings option.
            choice_number = 0
            for j in v:                  # iterate through every character.
                if j in num_list:        # if the character is a number it is a choice the player can make.
                    choice_number += 1   # then add 1 to choice number.
                branch_dict[branch_tup[i]] = choice_number # now this dict contains, key = index of branch_option, value = number of choies in that branch option 

        for k, v in length_dict.items(): # check length dict to get the length of the maze
            if k == length: 
                maze_length = range(0, v+1) 
                coordinate_range = range(0, v)

        for i in maze_length:       # v is the randomised length, one for every maze event we are about to generate.
            #coordinate = ()
            top_func = (a.branch,)
            go_to_func = (a.go_to,)
            key = (str(i),)

            if i == 0:
                p = (branch[0],)
                branch.remove(branch[0])
            else:
                 p = random.choice(branch)
                 p = (p,)

            for k, v in branch_dict.items():
                if p[0] == k:
                    choices = range(1, v+1)

            coordinate_list = []
            for i in coordinate_range:
                coordinate_list.append(i+1)
            for i in choices:
                if len(coordinate_list) < len(choices):
                    coordinate_list.append(random.choice(coordinate_list))

            stem = key + top_func + p
            
            for i in choices:
                choice_num = (str(i),)
                coordinate = (random.choice(coordinate_list),)
                for co in coordinate_list:
                    if co == coordinate[0]:
                        coordinate_list.remove(co)

                stem = stem + choice_num + go_to_func + coordinate

            maze_dict[stem[0]] = stem[1:]
        maze_dict['99'] = (a.story, 5)

        file = open('dump.txt', 'a')
        file.write('\n maze =')
        for k, v in maze_dict.items():
            file.write('\n {} : {}'.format(str(k), str(v)))
        file.close()
