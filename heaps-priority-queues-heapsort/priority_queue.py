import heap

class priority_queue(object):
    def __init__(self, a):
        self.a = a
        heap.build_max_heap(a)
    
    def size(self):
        return heap.heap_size(self.a)

    def maximum(self):
        assert self.size() > 0
        return self.a[1]
    
    def extract_max(self):
        assert self.size() > 0
        result = self.a[1]
        self.a[1] = self.a[self.size()]
        self.a.pop()
        if self.size() > 0:
            heap.max_heapify(self.a, 1, self.size())
        return result

    def decrease_key(self, index, key):
        assert key <= self.a[index]
        self.a[index] = key
        heap.max_heapify(self.a, index, self.size())

    def increase_key(self, index, key):
        assert key >= self.a[index]
        heap.increase_key(self.a, index, key)

    def insert_key(self, key):
        heap.insert(self.a, key)
    
##############################################################################
# test:

def print_pq(pq):
    print(pq.a[1:])
    heap.print_tree(pq.a)
    
def test_priority_queue():
    # Example from slides. But I keep changing the same pq,
    # So the content of the pq change away from the slides.
    
    # If you want the data as well, you can use a dictionary
    # and put the "key: data" pairs in there.
    # Then for efficiency, run the priority queue algorithm only 
    # on the keys in the heap, and access the data through the dict.

    a = [None, 4,1,7,9,3,10,14,8,2,16]
    pq = priority_queue(a)
    print_pq(pq)
    m = pq.extract_max()
    print('Extract max', m)
    print_pq(pq)
    pq.increase_key(4, 17) # 4 is the index, not the old key
    print('increase_key(4, 17)')
    print_pq(pq)
    pq.insert_key(15)
    print('insert_key(15)')
    print_pq(pq)
    pq.decrease_key(2, 5) # 2 is the index, not the old key
    print('decrease_key(2, 5)')
    print_pq(pq)

if __name__ == '__main__':
    test_priority_queue()