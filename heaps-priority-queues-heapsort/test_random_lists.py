import random
import time

def random_list(length, one_based = False):
    L = []
    if one_based:
        L = [None]
    for _ in range(length):
        L.append(random.randrange(1000000))
    return L

# runs function(L) on random lists L and measure the runtime
def test_random_lists(function, one_based = False, num_doublings = 15):
    last_time = 0
    for i in range(1, num_doublings + 1):
        length = 1 << i # double length each round
        L = random_list(length, one_based)
        start_time = time.time()
        result = function(L)
        time_used = time.time() - start_time
        print (f'Length {length} time {time_used:.3f}')
        if last_time > 0:
            print (f'Ratio {(time_used / last_time):.3f}')
        last_time = time_used
        
def test_random_one_based_lists(function, num_doublings = 15):
    one_based = True
    test_random_lists(function, one_based, num_doublings)