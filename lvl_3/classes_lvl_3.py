class My_matrix:
    def __init__(self):
        self.data = []

    # Спросим у пользователя что он хочет сделать
    def ask_what_to_do(self):
        #print(len(self.data))
        choice = input('Ваш выбор: ')
        if choice == "m": # Ввод исходных данных для создания или пересоздания матрицы
            print('Введите через запятую количество строк и колонок новой матрицы: '
                '\nФормат ввода, пример: 4,4'
                '\nЭто означает, что вы хотите создать или пересоздать матрицу в 4 строки и 4 колонки.')
            input_of_user = input('Введите данные: ')        
            result = (input_of_user, choice)
        elif choice == "r" and len(self.data) != 0: # Ввод исходных данных для увеличения размера матрицы с добавлением значений None
            print('Введите через запятую количество строк и колонок, которые вы хотите добавить к матрице.'
                '\nФормат ввода, пример: 5,3'
                '\nЭто означает, что вы хотите добавить 5 строк и 3 колонки.')
            input_of_user = input('Введите данные: ')
            result = (input_of_user, choice)
            
        elif choice == "a" and len(self.data) != 0: # Ввод исходных данных добавления значения в матрицу в определенную ячейку
            
            print('Введите через запятую адрес ячейки матрицы и значение, которое вы хотите вставить в матрицу.'
                '\nФормат ввода, пример: 5,3,856'
                '\nЭто означает, что вы хотите добавить значение 856 по адресу ячейки [строка: 5, колонка: 3].')
            input_of_user = input('Введите данные: ')
            result = (input_of_user, choice)
            
        elif choice == "i" and len(self.data) != 0: # Ввод исходных данных для изменения значений в матрице
            
            print('Введите через запятую и разделитель ">" значения, которые нужно найти в матрице и заменить на указанные вами значения.'
                '\nФормат ввода, пример: 33,56,23>12,22,11'
                '\nЭто означает, что вы хотите во всех ячейках со значением 33 установить значение 12, значение 56 на значение 22 и т.д ')
            input_of_user = input('Введите данные: ')
            result = (input_of_user, choice)

        elif choice == "n" and len(self.data) != 0: # Вывод количества строк и колонок в матрице
            result = (None, choice)

        elif choice == "s" and len(self.data) != 0: # Вывод значений матрицы
            result = (None, choice)

        elif choice == "q": # Завершим программу
            result = (None, choice)
            
        else:
            # Пользователь ввел какую-то ерунду, попросим повторить ввод.
            result = (None, None)  

        return result         

                   
    # Проверим корректность ввода пользователем исходных значений 
    # и преобразуем строковый ввод пользователя в целочисленные значения
    def input_validation(self, input_of_user, choice):
        # self.input_of_user1 = input_of_user
        #print(input_of_user)
        input_of_user_list = input_of_user.split(",") # выдерним из строки с разделителем "," список значений
        len_input_of_user_list = len(input_of_user_list)
        if len_input_of_user_list == 2 and (choice == "m" or choice == "r"): # Если в списке два значения, то пользователь правильно ввел данные
            try: #Если получится перевести исходные данные пользователя в int, то продолжим
                input_tuple = () # создадим пустой кортеж
                for i in input_of_user_list:
                    input_tuple = input_tuple + (int(i),) # формируем целочисленные исходные данные в виде кортежа
                result = (input_tuple, choice) # возвратим целочисленные исходные данные и признак
            except: # Если возникнет исключительная ситуация (ошибка), то пользователь ввел неправильные данные
                result = False
        elif len_input_of_user_list == 3 and choice == "a":
            try: #Если получится перевести исходные данные пользователя в int, то продолжим
                input_tuple = () # объявим пустой кортеж
                counter = 0
                for i in input_of_user_list:
                    counter = counter + 1
                    if counter == 3:
                        input_tuple = input_tuple + (int(i),) # формируем целочисленное новое значение ячейки матрицы
                    else:
                        input_tuple = input_tuple + (int(i) - 1,) # формируем целочисленный адрес ячейки матрицы в виде кортежа
                result = (input_tuple, choice) # возвратим целочисленные исходные данные и признак действий пользователя
            except: # Если возникнет исключительная ситуация (ошибка), то пользователь ввел неправильные данные
                result = False
        elif choice == "i": # проверим правильно ли ввели значения на замену "value1,value2..>new_value1,new_value2.."
            input_of_user_list = input_of_user.split(">") # выдерним из строки с разделителем ">" список значений
            values_old_list = input_of_user_list[0].split(",") # старые значения преобразуем в список
            values_new_list = input_of_user_list[1].split(",") # новые значения преобразуем в список
            if len(input_of_user_list) == 2 and (len(values_old_list) == len(values_new_list)): # Если в списке два значения, то пользователь действительно ввел два набора данных
                try: #Если получится перевести исходные данные пользователя в int, то продолжим
                    values_old_tuple = () # создадим пустой кортеж для старых значений
                    values_new_tuple = () # создадим пустой кортеж для новых значений
                    for i in values_old_list:
                        values_old_tuple = values_old_tuple + (int(i),) # формируем целочисленные исходные данные в виде кортежа
                    for i in values_new_list:
                        values_new_tuple = values_new_tuple + (int(i),) # формируем целочисленные исходные данные в виде кортежа
                    result = ((values_old_tuple,values_new_tuple), choice) # возвратим целочисленные исходные данные и признак
                except: # Если возникнет исключительная ситуация (ошибка), то пользователь ввел неправильные данные
                    result = False
            else:
                result = False # пользователь ввел не верные данные
        else:
            result = False # пользователь ввел не верные данные
        return result

    # Создадим таблицу значениями NULL
    def create_table(self, row_col):
        if len(self.data) != 0:
            self.data.clear()
        try:
            self.num_rows = row_col[0]
            self.num_cols = row_col[1]
            for i in range(row_col[0]):
                row = [None] * row_col[1]
                self.data.append(row)
            result = True
        except:
            result = False
        return result
            


    # Поместим значение в таблице по адресу в колонке col строке row на значение new_value
    def set_value(self, row_col_value):
        self.data[row_col_value[0]][row_col_value[1]] = row_col_value[2]

    def get_num_rows(self): # возвратим число строк
        return self.num_rows

    def get_num_cols(self): # возвратим число колонок
        return self.num_cols

    def add_empty_rows_cols(self, rows_cols): # добавим заданное количество пустых строк и колонок к матрице
        self.num_rows = self.num_rows + rows_cols[0] # установим новое количество строк
        row = [None] * self.num_cols       
        for i in range(rows_cols[0]): # увеличим количество строк
            self.data.append(row)
        self.num_cols = self.num_cols + rows_cols[1] # установим новое количество колонок
        col = [None] * rows_cols[1]
        for i in range(self.num_rows): # Добьем количество колонок
            self.data[i] = self.data[i] + col
        return True

    # Заменим старые значения в матрице на новые значения
    def replace_value(self, old_new_value):
        for row in range(self.num_rows):
            for col in self.data[row]:
                try:
                    index_in_new_value = old_new_value[0].index(col)
                    index_in_matrix = row.index(col)
                    self.data[row][index_in_matrix] = old_new_value[1][index_in_new_value]
                except:
                    pass
        return True
 




    

