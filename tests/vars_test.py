

# class Thing():
#     def __init__(self, a=None, b=None, c=None):
#         self.a =a
#         self.c=c
#         self.b=b


# thing_ob1 = Thing(a=1,c=2,b=3)
# thing_ob2 = Thing(a=3,b=4)
# thing_ob3 = Thing(b=5,c=6)



# def look(key):
#     thing_list =[thing_ob1, thing_ob2, thing_ob3]

#     for i in thing_list:
#         if key in vars(i) and 'a' in vars(i):
#             print(vars(i)[key])

# look('a')

# # thing_list =[thing_ob1, thing_ob2, thing_ob3]

# # print(      vars(thing_list[1])['a']      )


# file=open('room.txt', 'r')
# data=file.read()
# paragraph = data.split("\n\n")
# file.close()
# three_door =[] 
# for i in paragraph[1:]:
#     if i.endswith('#3door'):
#         print(i)
#         three_door.append(i[:-6])
#         print(three_door)

l = range(4)

print(l[-1])
 
