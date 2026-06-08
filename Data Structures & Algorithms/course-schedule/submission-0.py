class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        tree = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            tree[crs].append(pre)

        state = [0] * (numCourses)

        def dfs(c):
            if state[c] == 1:
                return False
            if state[c] == 2:
                return True
            
            state[c] = 1
            for dep in tree[c]:
                if not dfs(dep):
                    return False
            state[c] = 2
            return True
        
        return all(dfs(i) for i in range(numCourses))
            

