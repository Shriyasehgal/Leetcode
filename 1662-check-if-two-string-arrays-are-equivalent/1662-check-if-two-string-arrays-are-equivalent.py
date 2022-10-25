class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        queue = deque([])
        for word in word1:
            for char in word:
                queue.append(char)
        for word in word2:
            for char in word:
                if not queue: return False
                if char != queue.popleft(): return False
        return not queue
                