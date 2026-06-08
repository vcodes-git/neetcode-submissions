class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # tree = {i: [] for i in range(numCourses)}

        # for crs, pre in prerequisites:
        #     tree[crs].append(pre)

        # state = [0] * (numCourses)

        # def dfs(c):
        #     if state[c] == 1:
        #         return False
        #     if state[c] == 2:
        #         return True
            
        #     state[c] = 1
        #     for dep in tree[c]:
        #         if not dfs(dep):
        #             return False
        #     state[c] = 2
        #     return True
        
        # return all(dfs(i) for i in range(numCourses))
        

        # TOPOLOGICAL SORT
        revGraph = {i: [] for i in range(numCourses)}
        degree = [0] * numCourses

        for course, pre in prerequisites:
            revGraph[pre].append(course)
            degree[course] += 1
        
        q = deque([i for i in range(numCourses) if degree[i] == 0])
        processed = 0

        while q: 
            course = q.popleft()
            processed += 1
            for child in revGraph[course]:
                degree[child] -= 1
                if degree[child] == 0: 
                    q.append(child)
        
        return processed == numCourses

