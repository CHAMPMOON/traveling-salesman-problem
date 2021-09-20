class Node:
    nodes = list()

    def __init__(self, way, matrix, R):
        self.way = way
        self.matrix = matrix
        self.rating = R
        Node.nodes.append(self)
    
    def __lt__(self, other):
        return self.rating <= other.rating

    
