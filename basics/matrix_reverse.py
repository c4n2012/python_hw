def matrix2array(matrix):
    matrix_size = len(matrix.split())
    matrix_temp = matrix.split()
    splitted_matrix = []
    for i in range(0,matrix_size):
        splitted_row =[]
        for j in range (0,matrix_size):
            splitted_row += matrix_temp[i][j]
        splitted_matrix += [splitted_row]
    #print(splitted_matrix)
    return splitted_matrix

def matrix_reverse(matrix):
    matrix_size = len(matrix)
    matrix_reversed =[]
    for i in range(0,matrix_size):
        for j in range (0,matrix_size):
            if i == j:
                pass
            elif i <= j:
                pass
            else:
                a = matrix[i][j]
                matrix[i][j] = matrix[j][i] 
                matrix[j][i] = a
               # print(matrix[i][j]+" "+matrix[j][i])
    matrix_print(matrix)

def matrix_print(matrix):
    for line in matrix:
        print(*line)

matrix = """
123
456
789"""
matrix_array = matrix2array(matrix)
matrix_reverse(matrix_array)
print()
matrix = """
1111
2222
3333
4444"""
matrix_array = matrix2array(matrix)
matrix_reverse(matrix_array)