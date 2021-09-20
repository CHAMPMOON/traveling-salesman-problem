from workwithmatrix import WorkWithMatrix
from node import Node

class TaskSalesman:
    def __init__(self, matrix):
        self.task = matrix
        self.way = list()
        self.active_node = list()
        self.num_vert = len(matrix)
    

    def solve_salesman(self):
        way = list()
        matr = WorkWithMatrix(self.task)
        R = matr.bring_matrix()
        work_node = Node(way, self.task, R)
        try:
            while True:
                work_node = min(Node.nodes)
                # self.print_node(work_node)
                self.create_lf_node(work_node)
                self.create_rg_node(work_node)
                Node.nodes.remove(work_node)
        except:
            print("weight -", work_node.rating)
            return self.print_way(work_node.way)


    def create_rg_node(self, node):
        matr = WorkWithMatrix(node.matrix)
        R = matr.bring_matrix()
        i, j, D = matr.find_fines()
        matr.delete_i_j(i, j)
        matr.inf_edges(i, j, node.way)
        H, rg_matr = matr.bring_matrix(True)
        way = node.way.copy()
        way.append([i, j])
        rg_node = Node(way, rg_matr, node.rating + H)
        

    def create_lf_node(self, node):
        matr = WorkWithMatrix(node.matrix)
        R = matr.bring_matrix()
        i, j, D = matr.find_fines()
        matr = WorkWithMatrix(node.matrix)
        lf_matr = matr.get_lf_matrix(i, j)
        way = node.way.copy()
        lf_node = Node(way, lf_matr, node.rating + D)
    
    
    def print_node(self, node):
        print(node.matrix, sep="\n")
        print(f"way - {node.way}")
        print(f"R - {node.rating}")
    
    def print_way(self, way):
        end = way[0]
        while len(way) != 1:
            for elem in way:
                if elem[0] == end[-1]:
                    edge = end + [elem[1]]
                    way.remove(end)
                    way.remove(elem)
                    way.append(edge)
                    end = edge
        way = way[0]
        if len(way) == self.num_vert:
            way.append(way[0])
        print(way[0] + 1, end="")
        for el in way[1:]:
            print(f" --> {el + 1}", end="")
