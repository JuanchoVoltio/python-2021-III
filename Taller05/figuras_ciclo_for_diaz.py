'''# figura a 

b = int(input("número de filas: "))
h = int(input("número de columnas: "))
print()
for i in range (0,b):# ciclo for de las filas
    for j in range(0,h):# ciclo for de las columnas
        print("*", end="")
    print()'''

'''# figura b

h = int(input("Introduce el número de renglones del triángulo: "))
for i in range(h+1):
    print('*'*i)

for i in range(h+1):
    espacios=h-i
    print(' '*espacios+'*'*i)'''

# figura c

b = int(input("número de columnas: "))
h = int(input("número de filas: "))  

for i in range(h):
    print(" "*i, end="")
    print("*"*b, end="")
    print(" "*i)
    b=b-2
