matrix = [10, 3, 4, 1, 8, 11, 5, 2, 7]
print(matrix)
    
#TODO: Ordenar los valores

print("="*29)
    
for recorrido in range(1,len(matrix)):
    for posicion in range(len(matrix)- recorrido):
        if matrix[posicion] > matrix[posicion + 1]:
            temporal = matrix[posicion]
            matrix[posicion] = matrix[posicion + 1]
            matrix[posicion + 1] = temporal
            print (matrix)
print()

#TODO: Invertir la matrix

print("="*29)

matrix.reverse()
print(matrix)

    
