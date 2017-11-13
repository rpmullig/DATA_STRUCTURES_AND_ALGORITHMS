from swap import swap
#from aifc import data

def less(x, y):
    return x < y

def less_key(x, y):
    return x.key < y.key

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * (i + 1)

def parent(i):
    return (i-1) / 2

# Student code -- fill in all the methods that have pass as the only statement
class Heap:
    def __init__(self, data, 
                 less = less):
        self.data = data
        self.less = less
        self.build_min_heap()

    def __repr__(self):
        return repr(self.data)
    
    
    def minimum(self):
        # first check if 0 or none
        if len(self.data) == 0 or self.data == None:
            return None
        else:
        # return the first node, the smallest one
            return self.data[0]

    def insert(self, obj):
       # Simply add the object to the list
       self.data.append(obj)
       # then run min_heapify to re-organize the heap
       self.min_heapify

    def extract_min(self):
        # for testing
        assert len(self.data) != 0
        # take first node, delete it, then return it
        min_value = self.data[0]
        del self.data[0]
        return min_value
        
    def min_heapify(self, i):
        #variables for use in the function
        n = len(self.data)
        H = self.data
        l = left(i)
        r = right(i)
        # compare keys and values,
        if less(l, n) and H[i] > H[l]:
            least = l
        # assign the value to i just as a place holder till
        # one cane compare the otherss
        else:
            least = i
        # compare for the right node
        if less(r, n) and H[least] > H[r]:
            least = r
        # if the least is not i, then swap and recure
        if least != i:
            swap(H, i, least)
            min_heapify(H, least)
    
    def build_min_heap(self):
        # go through the min_heap using the parents only
        n = len(self.data)
        last_parent = n / 2 - 1
        for i in range(last_parent, -1, -1):
            self.min_heapify(i)
   
class PriorityQueue:
    def __init__(self, less=less_key):
        self.heap = Heap([], less)

    def __repr__(self):
        return repr(self.heap)

    def push(self, obj):
        self.heap.insert(obj)

    def pop(self):
        return self.heap.extract_min()

if __name__ == "__main__":
    # unit tests here

    # I'm not even sure how to do this
    pass
