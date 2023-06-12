class My_matrix:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.data = []
        for i in range(num_rows):
            row = [None] * num_cols
            self.data.append(row)


    def set_value(self, row, col, value):
        self.data[row][col] = value

    def replace_value(self, row, col, new_value):
        if self.data[row][col] is not None:
            self.data[row][col] = new_value

    def get_num_rows(self):
        return self.num_rows

    def get_num_cols(self):
        return self.num_cols