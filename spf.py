class Graph(): 
        def __init__(self, nodes):
        self.distArray = [0 for i in range(nodes)]
        self.vistSet = [0 for i in range(nodes)]
        self.V = nodes
        self.INF = 1000000
        self.graph = [[0 for column in range(nodes)]  
                    for row in range(nodes)]
   
    def dijkstra(self, srcNode):
        for i in range(self.V):      
          self.distArray[i] = self.INF
          self.vistSet[i] = False
        self.distArray[srcNode] = 0
        for i in range(self.V): 
  
            u = self.minDistance(self.distArray, self.vistSet) 
  
            self.vistSet[u] = True
  
            for v in range(self.V): 
                if self.graph[u][v] > 0 and self.vistSet[v] == False and self.distArray[v] > self.distArray[u] + self.graph[u][v]: 
                        self.distArray[v] = self.distArray[u] + self.graph[u][v] 
  
        self.printSolution(self.distArray)

    
    def minDistance(self, distArray, vistSet): 
  
        
        min = self.INF 
        
        for v in range(self.V): 
            if distArray[v] < min and vistSet[v] == False: 
                min = distArray[v] 
                min_index = v 
  
        return min_index

    def printSolution(self, distArray): 
        print ("Node \tDistance from 0")
        for i in range(self.V): 
            print (i, "\t", distArray[i])

ourGraph = Graph(7) 
ourGraph.graph = [[0, 2, 6, 0, 0, 0, 0], 
        [2, 0, 0, 5, 0, 0, 0], 
        [6, 6, 0, 8, 0, 0, 0], 
        [0, 0, 8, 0, 10, 15, 0], 
        [0, 0, 0, 10, 0, 6, 2], 
        [0, 0, 0, 15, 6, 0, 6], 
        [0, 0, 0, 0, 2, 6, 0],
        ]; 
  
ourGraph.dijkstra(0)
