'''
Topological sorting of DAG
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering
of vertices such that for every directed edge u v, vertex u comes before
v in the ordering. Topological Sorting for a graph is not possible if the
graph is not a DAG.
Kahn's algorithm
'''
from collections import defaultdict, deque
class Sorting:
    def findOrder(self, gr):
        q = deque() #to keep a track of all nodes with in-degree 0
        adj_ = defaultdict(list)
        hm = {}
        for s,d in gr:
            #create the adjacency list
            adj_[d].append(s)
            hm[s]=hm.get(s,0)+1   #.get return 0 if the value does not exist in the hashmap

        topological_order = []
        #update the q with in-degree 0
        for i in range(len(gr)):
            if i not in hm:
                q.append(i)

        while q:
            node = q.popleft()
            topological_order.append(node)
            if node in adj_:
                for n in adj_[node]:    #reduce in degree for all the neighbors
                    hm[n]-=1
                    if hm[n]==0:
                        q.append(n)
        return topological_order if len(topological_order)==len(gr) else []
