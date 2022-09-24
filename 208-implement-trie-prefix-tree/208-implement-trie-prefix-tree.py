class Node:
    def __init__(self,val):
        self.val = val
        self.children = [None]*26
        self.wordend = 0
        
class Trie:
    def __init__(self):
        self.root = Node(None)
        

    def insert(self, word: str) -> None:
        currRoot = self.root
        for letter in word:
            if currRoot.children[ord(letter) - ord('a')] == None:
                currRoot.children[ord(letter) - ord('a')] = Node(letter)
            currRoot = currRoot.children[ord(letter) - ord('a')]
        currRoot.wordend = 1
        

    def search(self, word: str) -> bool:
        currRoot = self.root
        for letter in word:
            if currRoot.children[ord(letter)-ord('a')] == None:
                return False
            currRoot = currRoot.children[ord(letter)-ord('a')]
        return currRoot.wordend
        

    def startsWith(self, prefix: str) -> bool:
        currRoot = self.root
        for letter in prefix:
            if currRoot.children[ord(letter)-ord('a')] == None:
                return False
            currRoot = currRoot.children[ord(letter)-ord('a')]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)