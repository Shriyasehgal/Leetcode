class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        graph = {}
        for i in range(len(recipes)):
            graph[recipes[i]] = ingredients[i]
        res = []
        prepared = set()
        visited = set()
        def dfs(item):
            if item in visited: return False
            if item in prepared: return True
            if item not in supplies and item not in graph: return False
            visited.add(item)
            for i in graph[item]:
                if i not in supplies:
                    if not dfs(i): return False
            graph[item] = []
            res.append(item)
            supplies.add(item)
            prepared.add(item)
            visited.remove(item)
            return True
        for item in recipes:
            dfs(item)
        return res
                
            