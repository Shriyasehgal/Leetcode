class Node:
    def __init__(self, val):
        self.val = val
        self.children =[None]*26
        self.wordend = 0
class WordDictionary:
    
    def __init__(self):
        self.root = Node(None)
        

    def addWord(self, word: str) -> None:
        currRoot = self.root
        for letter in word:
            if currRoot.children[ord(letter)-ord('a')] == None:
                currRoot.children[ord(letter)-ord('a')] = Node(letter)
            currRoot = currRoot.children[ord(letter)-ord('a')]
        currRoot.wordend = 1

    def search(self, word: str) -> bool:
        currRoot = self.root
        def helper(word,currRoot):
            for i, letter in enumerate(word):
                if letter == '.':
                    for j in range(26):
                        if currRoot.children[j] != None:
                            if helper(word[i+1:],currRoot.children[j]):
                                return True
                    return False

                elif letter != '.' and currRoot.children[ord(letter)-ord('a')] == None:
                    return False
                else:
                    currRoot = currRoot.children[ord(letter)-ord('a')]
            return currRoot.wordend
        return helper(word,currRoot)
            
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)