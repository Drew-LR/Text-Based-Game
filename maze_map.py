from constants import term
import constants

class Map():
    def open(self):
        print(term.home + term.move_down(5) + term.clear_eos)
        for i in range(0,18):
            print(term.home + term.move_down(5 + i) + term.move_right(14) + '|' + (' ' * 50) + '|')
        for i in range(0, 50):
             print(term.home + term.move_down(22) + term.move_right(15+i) + '_')

        for i in range(0,16):
            print(term.home + term.move_down(6 + i) + term.move_right(16) + '|' + (' ' * 46) + '|')
        for i in range(0, 46):
            print(term.home + term.move_down(5) + term.move_right(17+i) + '_')
            print(term.home + term.move_down(21) + term.move_right(17+i) + '_')

        map_name = ' Old Town '
        print(term.home + term.move_down(8) + term.move_right(term.width//2 - len(map_name)//2 -1) + term.underline(map_name))

        length = len(constants.rows[0])

        print(term.home + term.move_down(term.height//2 - len(constants.rows)//2 + 1))
        for j in constants.rows:
            print(term.move_right(term.width//2 - length-1) + ' '.join(j))
            
        while 1:
            key = term.inkey()
            if key == 'm':
                print(term.home + term.move_down(5) + term.clear_eos)
                break

        #      print(term.home + term.move_down(term.height//2 - len(constants.rows)//2))
        # for i, v in enumerate(constants.rows):
        #     for j in v:
        #         if j == 'O':
        #             print(term.move_right(term.width//2 - length + i) + term.blue('O'))
        #         elif j == 'X':
        #             print(term.move_right(term.width//2 - length + i) + term.orange('X'))