class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        if beginWord not in wordList: wordList.append(beginWord)
        mapp = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[0:i] + '*' + word[i+1:]
                mapp[pattern].append(word)
        
        oldQueue = deque([beginWord])
        newQueue = deque([])
        path = 1
        visited = set()
        while oldQueue:
            curr = oldQueue.popleft()
            visited.add(curr)
            for i in range(len(curr)):
                pattern = curr[0:i] + '*' + curr[i+1:]
                for word in mapp[pattern]:
                    if word != curr and word not in visited:
                        newQueue.append(word)
                        if word == endWord: return path+1
            if not oldQueue:
                newQueue,oldQueue = oldQueue, newQueue
                path+=1
        return 0
        
        '''def bfs(curr, path, visited):
            nonlocal final_path
            if curr in visited: return            
            if curr == endWord:
                final_path = min(final_path,path)
                return
            visited.add(curr)
            for i in range(len(curr)):
                pattern = curr[0:i] + '*' + curr[i+1:]
                for word in mapp[pattern]:
                    if word not in visited:
                         bfs(word,path+1,visited)
            visited.remove(curr)
            
        bfs(beginWord, 1, set())
        return final_path if final_path!= float('inf') else 0'''
                        
            
            
            
            
        
        