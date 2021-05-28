
numero=int(input("Digíte un número menor o igual a 30: "))

factorial = 1
if numero !=0 and numero <= 30:
        for i in range (1, numero + 1):
            factorial *= i
else:
     print("La condición NO se ha cumplido.\n")
                
print("factorial:",factorial)

