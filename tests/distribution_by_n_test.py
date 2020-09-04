import random

def func():
    w = 100
    mylist = []
    pre =1
    length = [1,2]


    for i in range(len(length)):
        try:
            if i == len(length) -1:
                mylist.append((pre, 100))
                break
            num = random.randrange(pre, w+1)
            mylist.append((pre,num))
            pre = num +1
        except:
            adjustment = max(mylist) //3
            mylist.append(adjustment)
            mylist[mylist.index(max(mylist))] = mylist[mylist.index(max(mylist))] - adjustment
        

    # if sum(mylist) != 100:
    #     addition = 100 - sum(mylist)
    #     mylist[mylist.index(min(mylist))] = mylist[mylist.index(min(mylist))] + addition


    return mylist
    

mylist =func()
print(mylist)
# def sprinkle(mylist):
#     while sum(mylist) >1:
#         x= random.choice(mylist)
#         if x <= 0:
#             continue
#         #print(x, mylist.index(x))
#         mylist[mylist.index(x)] = x-1

#     print(mylist)
# sprinkle(mylist)
