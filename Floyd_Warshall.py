from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices

    def printSolution(self, reach):
        print("Following matrix transitive closure of the given graph ")
        for i in range(self.V):
            for j in range(self.V):
                print("%7d\t" % (reach[i][j])),
            print("")

    def transitiveClosure(self, graph):
        reach = [i[:] for i in graph]
        for k in range(self.V):

            for i in range(self.V):

                for j in range(self.V):
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

        self.printSolution(reach)


g = Graph(4)

graph = [[1, 1, 0, 1],
         [0, 1, 1, 0],
         [0, 0, 1, 1],
         [0, 0, 0, 1]]

g.transitiveClosure(graph)
