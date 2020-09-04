def print_func(func, param): # this is for passing secondary functions which print to the screen hp_handler, gold_handler ect
    print (func(param))

def return_func(func, param): # this is for passing secondary functions which dont print, like adding to the inventory
    return func(param)