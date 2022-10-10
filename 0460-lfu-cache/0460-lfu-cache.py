class Node:
    def __init__(self, key, val):
        self.key , self.val = key, val
        self.next = None
        self.prev = None
        self.ctr = 1
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {} # This is a cache with capacity cap
        self.freq = collections.defaultdict(OrderedDict) 
        self.minFreq = None
        
    def remove(self,node):
        nex , pre = node.next, node.prev
        pre.next = nex
        nex.prev = pre
        del node
        
    def insert(self, node):
        node.prev = self.left
        node.next = self.left.next
        self.next = node
        node.next.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        #Value to return 
        value = self.cache[key].val
        #updating the counter
        node = self.cache[key]
        c = self.cache[key].ctr
        del self.freq[c][key]
        if not self.freq[c] : del self.freq[c]
        c+=1
        node.ctr = c
        self.freq[c][key] = node
        if not self.freq[self.minFreq]: self.minFreq+=1
        return value

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return 
        
        if key not in self.cache:
            if len(self.cache) == self.cap:
                nodeRemove = self.freq[self.minFreq].popitem(last = False)[1]
                self.remove(nodeRemove)
                del self.cache[nodeRemove.key]
                if not self.freq[self.minFreq]: del self.freq[self.minFreq]
                
                
            node = Node(key,value)
            self.minFreq = 1
            self.insert(node) # added to the dll
            self.freq[self.minFreq][key] = node
            self.cache[key] = node
            
            
        else:
            self.cache[key].val = value
            _ = self.get(key)
            return 
            
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)