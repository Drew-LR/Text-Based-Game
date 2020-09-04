my_dict = {
    '1' : ('Oneth',  '4'), 
    '2' : ('twoth',  '5'),
    '3' : ('threeth','1'),
    '4' : ('fourth', '2'),
    '5' : ('fiveth', '3'),
}

'''
1 = 4
2 = 5
3 = 1
4 = 2
5 = 3
'''
index = 1

for i in range(10):
    for k,v in my_dict.items():
        if str(index) == k:
            index = v[1]
            print(k,v)


'''  # a bit of scrap I worked on last night.
  if constants.diverge == True: ### heres the new bit
                                    while constants.diverge == True:
                                        for k,v in event_list.main_dict.items():
                                            if str(constants.skip) == k:
                                                func = v[0] # the first variable for this key is a function to be called, the 'top level function'
                                                print(func(*key_elem[1:])) # feed all other variables to the 'top level function', some may also be functions (see event_list.py) 

                                                while 1: # wait until the player presses 'KEY_ENTER', then continue with the iteration of 'main_dict'. 
                                                    key = term.inkey()
                                                    if key.is_sequence and key.name == 'KEY_ENTER':     
                                                        #constants.skip = 0 # 'reset constants.skip' for the next iteration
                                                        break
                                            constants.skip = 0 # before we pass on an empty (a key with no variables), we have to reset constants.skip for the next iteration.
                                            pass ### new bit ends here

                                constants.skip = 0 # 'reset cons'''
