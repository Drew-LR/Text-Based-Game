from blessed import Terminal

term = Terminal()

def move_to_bottom():
    print(term.move_down(10))
    print("no")


def move_to_top():
    term.move_up(term.height)

print(term.clear())    

move_to_bottom()
term.inkey()    
