class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        eqn = {}
        def find(x):
            if x not in eqn:
                eqn[x] = x
            p = eqn[x]
            if p == x:
                return p
            return find(p)
        def union(x,y):
            p1 = find(x)
            p2 = find(y)
            if p1 == p2: return
            else: eqn[p2] = p1 
        for eq in equations:
            if eq[1] == '=':
                union(eq[0],eq[3])
        for eq in equations:
            if eq[1] == '!':
                if find(eq[0]) == find(eq[3]): return False
        return True
        