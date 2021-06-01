matrix = [[10, 3, 4],
          [1, 8, 11],
          [5, 2, 7]]

matrix2 = [[12, 3, 4],
          [1, 8, 11],
          [5, 2, 6]] 

def calculate_average(*ages):
    carry = 0
    for age in ages:
        carry = carry + age
        
    print("Average: ",carry/len(ages))
#End of calculate_average()

def print_matrix(matrix):
    for i in range(0, 3, 1): #Controlar el recorrido de las filas
        for j in range(0, 3, 1): #Controlar el recorrido de las columnas
            print(matrix[i][j], " ", end="")
        print()

    print("=" * 10)    
#End of print_matrix()

calculate_average(2, 3, 4, 5)

#print_matrix(matrix2)

#TODO: Ordenar los valores

#print_matrix(matrix)

#TODO: Invertir la matriz

#print_matrix(matrix2)
