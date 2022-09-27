class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        q = deque()
        for i,d in enumerate(dominoes):
            if d != '.': q.append((i,d))
        while q:
            i,d = q.popleft()
            if d == 'L':
                if i > 0 and dominoes[i-1] == '.':
                    dominoes[i-1] = 'L'
                    q.append((i-1,'L'))
            elif d == 'R':
                if i < len(dominoes)-1 and dominoes[i+1] =='.':
                    if i < len(dominoes)-2 and dominoes[i+2] == 'L':
                        q.popleft() #Removing the next L as well so that it doesnot knock over the standing dominoe
                    else:
                        dominoes[i+1] = 'R'
                        q.append((i+1,'R'))
        return ''.join(dominoes)
        