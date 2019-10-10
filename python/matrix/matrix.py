class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[*map(int,m.split())] for m in matrix_string.split('\n')]
        return

    def row(self, index):
        # print(self.matrix[index-1])
        return self.matrix[index-1]

    def column(self, index):
        # print([m[index-1] for m in self.matrix])
        return [m[index-1] for m in self.matrix]
