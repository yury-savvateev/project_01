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

    def add_empty_rows(self, quantity_empty_rows): # добавим заданное количество пустых строк к матрице
        pass

    def add_empty_cols(self, quantity_empty_cols): # добавим заданное количество пустых колонок к матрице
        pass

    def add_value_with_creation_of_new_area(self, row, col, value): # увеличим матрицу до заданной области и добавим заданное значение
        pass

    

