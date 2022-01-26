class Node:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.last = False
class WordDictionary:

    def __init__(self):
        self.node = Node(None)
        

    def addWord(self, word: str) -> None:
        root = self.node
        for letter in word:
            if letter not in root.children.keys():
                root.children[letter] = Node(letter)
            root = root.children[letter]
        root.last = True


    def search(self, word: str) -> bool:
        root = self.node
        
        def helper(root, word):
            for i,letter in enumerate(word):
                
                if letter == '.':
                    if len(root.children.keys())==0:
                        return False
                    for child in root.children.keys():
                        if helper(root.children[child],word[i+1:]):
                            return True
                    return False

                elif letter != '.' and letter not in root.children.keys():
                    return False
                else:
                    root = root.children[letter]
            return root.last
        return helper(root,word)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
