'''
Graph structure: 
A -->  ['B', 'C', 'D']
C -->  ['A', 'G']
B -->  ['A', 'G']
E -->  ['D', 'F']
D -->  ['A', 'E', 'F']
G -->  ['B', 'C']
F -->  ['D', 'E']

BFS(A):
A,B,C,D,G,E,F

BFS(B):
B,A,C,G,D,E,F

DFS(A):
A,B,G,C,D,E,F

DFS(B):
B,A,C,G,D,E,F

'''
class queue:
    def __init__(self):
        self.item = []

    def isempty(self):
        return self.item == []

    def enqueue(self,a):
        self.item.insert(0,a)

    def dequeue(self):
        return self.item.pop()

class stack:
    def __init__(self):
        self.items = []

    def s_push(self,a):
        self.items.append(a)

    def s_pop(self):
        return self.items.pop()

    def isempty(self):
        return self.items==[]

    def top(self):
        return self.items[len(self.items)-1]
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,Node):
        self.vertices[Node]=[]

    def add_edge(self,f,t):
        if f not in self.vertices:
            self.add_vertex(f)
        if t not in self.vertices:
            self.add_vertex(t)
        self.vertices[f].append(t)
        self.vertices[t].append(f)

    def print_graph(self):
        for key in self.vertices.keys():
            print key,self.vertices[key]

    def BF_print(self,node):
        q = queue()
        visited = []
        if node in self.vertices:
            print node,
        else:
            print 'no such node'
            return
        q.enqueue(node)
        visited.append(node)
        while(q.isempty()==False):
            node = q.dequeue()
            for nbors in self.vertices[node]:
                if nbors not in visited:
                    q.enqueue(nbors)
                    visited.append(nbors)
                    print nbors,
        print
        return

    def DF_print(self,node):
        if node not in self.vertices:
            print 'node not in graph'
            return
        s = stack()
        visited = [node]
        print node,
        s.s_push(node)
        while(s.isempty()==False):
            node = s.top()
            nf = 0
            for nbors in self.vertices[node]:
                if nbors not in visited:
                    visited.append(nbors)
                    s.s_push(nbors)
                    print nbors,
                    nf = 1
                    break
            if(nf==1):
                continue
            else:
                s.s_pop()
        print
        return


if __name__ == '__main__':
    g = Graph()
    g.add_edge('A','B')
    g.add_edge('A','C')
    g.add_edge('A','D')
    g.add_edge('B','G')
    g.add_edge('C','G')
    g.add_edge('D','E')
    g.add_edge('D','F')
    g.add_edge('E','F')
    g.print_graph()
    g.BF_print('A')
    g.BF_print('B')
    g.DF_print('A')
    g.DF_print('B')
    
