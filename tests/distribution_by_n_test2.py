import random

def func():
    w = 100
    mylist = []
    pre =1
    length = [1,2,3,4]


    for i in range(len(length)):
        try:
            if i == len(length) -1:
                mylist.append((pre, 100))
                break
            num = random.randrange(pre, w)
            mylist.append((pre,num))
            pre = num +1
        except:           
            #print('that error where we go over 100 occured')

            mylist = func()
            return mylist
            
            # adjustment = max(mylist) //3
            # mylist.append(adjustment)
            # mylist[mylist.index(max(mylist))] = mylist[mylist.index(max(mylist))] - adjustment


    return mylist
    
mylist = func()
# print(mylist)


for i in range(1001):

#     num = random.randint(1,101)
#     for i, (j,k) in enumerate(mylist):
#         if num in range(j,k):
#             print(num, 'in', mylist[i])

    num = random.randint(1,100)
    if num == 101:
        print(num)