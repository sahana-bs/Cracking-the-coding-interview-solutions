def dfs(parent):
    self.visited.add(parent)
    if self.adj_list[parent]:
        for n in self.adj_list[parent]:
            if n in self.visited:
                return False
            self.visited.add(parent)
            self.adj_list[n].remove(parent)
            dfs(n)

for s,d in edges:
    self.adj_list[s].append(d)
    self.adj_list[d].append(s)

if dfs(0) == False:
    return False
return len(self.visited)==n
