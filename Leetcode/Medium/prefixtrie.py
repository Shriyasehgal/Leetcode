class Node:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.last = False
class Trie:

    def __init__(self):
        self.node = Node(None)

    def insert(self, word: str) -> None:
        root = self.node
        for letter in word:
            if letter not in root.children.keys():
                root.children[letter]=Node(letter)
            root = root.children[letter] 
        root.last = True
        return None
            
    def search(self, word: str) -> bool:
        root = self.node
        for letter in word:
            if letter not in root.children.keys():
                return False
            root = root.children[letter] 
        return root.last               
        

    def startsWith(self, prefix: str) -> bool:
        root = self.node
        for letter in prefix:
            if letter not in root.children.keys():
                return False
            root = root.children[letter] 
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
