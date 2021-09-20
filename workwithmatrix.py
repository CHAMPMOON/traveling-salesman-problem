from re import T
import numpy as np

class WorkWithMatrix:
    inf = float("inf")

    def __init__(self, common_matrix):
        self.matrix = np.array(common_matrix)
    

    def bring_matrix(self, bool=False):
        R = 0
        for i in range(len(self.matrix)):
            min_line = min(self.matrix[i])
            if min_line == self.inf:
                continue
            self.matrix[i] -= min_line
            R += min_line
        for i in range(len(self.matrix)):
            min_colm = min(self.matrix[:,i])
            if min_colm == self.inf:
                continue 
            self.matrix[:,i] -= min_colm
            R += min_colm
        if bool:
            return R, self.matrix
        return R


    def find_fines(self):
        D = list()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 0:
                    min_line = min(list(self.matrix[i][:j]) + list(self.matrix[i][j + 1:]))
                    min_colm = min(list(self.matrix[:,j][:i]) + list(self.matrix[:,j][i + 1:]))
                    D.append((i, j, min_line + min_colm))
        return max(D, key=lambda x: x[2])
                    
    
    def delete_i_j(self, i, j):
        self.matrix[i] = [self.inf] * len(self.matrix)
        self.matrix[:,j] = [self.inf] * len(self.matrix)


    def inf_edges(self, i, j, way):
        self.matrix[j][i] = self.inf
        end = i
        while True:
            for elem in way:
                if elem[1] == end:
                    self.matrix[j][elem[0]] = self.inf
                    end = elem[0]
                    break
            else:
                break
    
    def get_lf_matrix(self, i, j):
        self.matrix[i][j] = self.inf
        return self.matrix


    
                



    

    
    






