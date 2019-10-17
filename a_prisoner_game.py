import random
#question: can we import random within the definition??

def play_prisoner_lightswitch_game(number_of_prisoners):
    N = number_of_prisoners
    counting_list = [False]*N
    light = False
    days = 0
    prisoner_count = 0
    while prisoner_count < N-1:
        days = days + 1
        m = random.randint(0,N-1)
        if m > 0 and light == False and counting_list[m] == False:
            light = True
            counting_list[m] = True
        elif m == 0 and light == True:
            light = False
            prisoner_count = prisoner_count + 1
    return "the prisoners were released after %s days" % days
