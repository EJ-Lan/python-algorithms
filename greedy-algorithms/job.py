class Job:
    def __init__(self, start, end, name):
        assert start > 0
        assert end > start
        self.start = start
        self.end = end
        self.name = name

    def __str__(self):
        return f'(Job {self.name} start = {self.start}, end = {self.end})'

    # the >= operator for Job. Sorts by start time. 
    # Operator is needed for key comparison in the 
    # quicksort partition function
    def __ge__(self, other): 
            return self.start >= other.start