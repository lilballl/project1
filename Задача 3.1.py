class Matrix:
    def __init__(self, n):
        self.matrix = [[None for i in range(n)] for j in range(n)]
    
    def set_value(self, row, col, value):
        self.matrix[row][col] = value
    
    def replace_value(self, row, col, value):
        if self.matrix[row][col] is not None:
            self.matrix[row][col] = value
    
    def get_num_rows(self):
        return len(self.matrix)
    
    def get_num_cols(self):
        return len(self.matrix[0])
