class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start not in bank: bank.append(start)
        bankDict = defaultdict(list)
        for i in range(len(bank)):
            for j in range(i+1,len(bank)):
                l,r = 0,0
                count = 0
                while l < 8:
                    if bank[i][l]!= bank[j][r]:
                        count+=1
                    l+=1
                    r+=1
                if count == 1:
                    bankDict[bank[i]].append(bank[j])
                    bankDict[bank[j]].append(bank[i])
        q1 = deque([start])
        q2 = deque()
        visited = set()
        visited.add(start)
        count = 0
        while q1:
            gene = q1.popleft()
            if gene == end: return count
            for n in bankDict[gene]:
                if n not in visited:
                    q2.append(n)
                    visited.add(n)
            if not q1:
                q1,q2 = q2,q1
                count+=1
        return -1
                
            
        
            