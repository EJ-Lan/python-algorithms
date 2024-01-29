import random

def random_list(num_elements, num_range = 1000):
    return [random.randint(0, num_range) for _ in range(num_elements)]