from blessed import Terminal
term = Terminal()

while term.cbreak():

    def func_to_execute1(a,b):
        return (a+b)

    def func_to_execute2(c,d):
        return (c*d)

    def func_to_execute3(start):
        print(start)
        while 1:
            key = term.inkey()
            if key == 'y':
                return func_to_execute1
            elif key == 'n':
                return func_to_execute2

    new_dict = {'1' : (func_to_execute3, 'y or n'), '2' : (func_to_execute2, 1, 2), '3' : (func_to_execute1, 1, 2)}

    def execute_function(new_dict):
        for k,v in new_dict.items():
            func = v[0]
            print(func(*v[1:]))
            while 1:
                key = term.inkey()
                if key.is_sequence and key.name == 'KEY_ENTER':
                    break

    execute_function(new_dict)
    #func_to_execute1(new_list)