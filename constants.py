from blessed import Terminal

term = Terminal()

game_over = False
current_branch = 0
absolute = 0
maze = False
maze_exit = False
maze_start = 0
maze_end = 0
maze_name = ''
maze_reverse = False
rows = []

def dump_print(string, *argv):
    file = open('dump.txt', 'a')
    file.write(string, argv)
    file.close()