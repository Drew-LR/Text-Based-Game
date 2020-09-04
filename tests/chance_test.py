import random



def flip(n):

    heads = 0
    tails = 0

    for i in range(n):
        chance = random.randint(0,5)
        if chance == 1:
            heads += 1
        else:
            tails += 1
    print('heads = ', heads, '%')
    print('tails = ', tails, '%')

flip(100)



