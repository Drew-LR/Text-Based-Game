from constants import term
import constants
import event_handler
import ui
import text_handler
from enter_name import enter_name

menu = ["new game", "continue", "quit"]

def print_menu(selected_row_idx):
    print(term.clear)
    for idx, row in enumerate(menu):
        x = term.width//2 - len(row)//2
        y = term.height//2 - len(menu)//2 + idx
        if idx == selected_row_idx: 
            print(term.move_xy(x ,y) + term.on_white + term.black + term.bold(row))
        else:
            print(term.move_xy(x, y) + row)    

def main():
    print(term.clear())
    current_row = 0
    print_menu(current_row)

    with term.hidden_cursor(), term.cbreak():
        while 1:

            key = term.inkey()
            if key.is_sequence:

                if key.name == 'KEY_UP' and current_row > 0:
                    current_row -= 1
                elif key.name == 'KEY_DOWN' and current_row < len(menu) -1:
                    current_row += 1
                elif key.name == 'KEY_ENTER':
                    if current_row == 0:
                        event_handler.game_events()
                    elif current_row == 1:
                        print(term.clear + term.home + "ahh, save data")
                        term.inkey()
                    elif current_row == len(menu) -1:
                        break

                print_menu(current_row)
    print(term.clear)

#constants.name = enter_name()
main()
