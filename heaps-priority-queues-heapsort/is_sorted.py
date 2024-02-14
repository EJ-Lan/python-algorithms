def compare_less_equal(item1, item2):
    return item1 <= item2
    
def compare_greater_equal(item1, item2):
    return item1 >= item2
    
def is_sorted(sequence, compare = compare_less_equal):
    return all(compare(sequence[i], sequence[i+1]) for i in range(len(sequence) - 1))