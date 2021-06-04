print('==========================')
print('*EXERCISE NÚMERO FACTORIAL*')
print('==========================')

number = int(input("Ingrese un número entero positivo diferente de 0: "))

factorial = 1

for i in range (int(number)):
    factorial *= number
    number -= 1

print (factorial)

'''if number !=0 and number <= 30:
        for i in range (1, number + 1):
            factorial *= i
else:
     print("La condición NO se ha cumplido.\n")
                
print("factorial:",factorial)'''
