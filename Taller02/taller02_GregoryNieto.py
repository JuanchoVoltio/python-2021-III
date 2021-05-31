print("*****************************************")
print("* EXERCISE CLASE DE ÁNGULOS *")
print("*****************************************\n")

template1 = 'introduce el ángulo del triángulo:  '
template2 = 'No aplica "La sumatoria de los ángulos de un triángulo es igual a 180'
template3 = 'Es un ángulo Rectángulo'
template4 = 'Es un ángulo Acutángulo'
template5 = 'Es un ángulo Obtusángulo'

angleA = float(input (template1))
angleB = float(input (template1))
angleC = float(input (template1))

grado = angleA + angleB + angleC

print(grado)

if grado > 180 or grado < 180 :
    print (template2)
elif angleA == 90 or angleB == 90 or angleC == 90 :
    print(template3)
elif angleA < 90 and angleB < 90 and angleC < 90 :
    print(template4)
elif angleA > 90 or angleB > 90 or angleC > 90 :
    print(template5)

else :
    pass
    
