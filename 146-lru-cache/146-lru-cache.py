class Node: 
    def __init__(self,key,value):
        self.key,self.value = key, value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # dictionary with a capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    #Remove from the list
    def remove(self,node):
        pre, nex = node.prev, node.next
        pre.next = nex
        nex.prev = pre
    
    #insert at the right
    def insert(self,node):
        pre, nex = self.right.prev, self.right
        pre.next = node
        nex.prev = node
        node.next = nex
        node.prev = pre
        
    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return val
        else: return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            
            del self.cache[lru.key]
        
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)