import sys

sys.setrecursionlimit(10000)
class Graph:
    def __init__(self, params):
        self.edges = params[0]
        self.leftVertex = params[1]
        self.rightVertex = params[2]

    def kuhn(self, v, used, matching):
        if used[v]:
            return False
        used[v] = True
        for i in range (len(self.edges[v])):
            to = self.edges[v][i]
            if matching[to] == -1 or self.kuhn(matching[to], used, matching):
                matching[to] = v
                return True
        return False

    def maxMatching(self):
        matching = [-1]*self.rightVertex
        for v in range (self.leftVertex):
            used = [False]*self.leftVertex
            self.kuhn(v, used, matching)
        return matching

