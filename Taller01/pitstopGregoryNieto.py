print("*******************")
print("*EXERCISE PIT STOP*")
print("*******************\n")

car_stop="Se detiene el vehículo y de manera simultánea realizan el trabajo:\n"
hombre_1="Asistente 1 cambia llanta 1"
import random
tiempo_hombre_1= random.randint(6,8)
hombre_2="Asistente 2 cambia llanta 2"
import random
tiempo_hombre_2= random.randint(6,8)
hombre_3="Asistente 3 cambia llanta 3"
import random
tiempo_hombre_3= random.randint(6,8)
hombre_4="Asistente 4 cambia llanta 4"
import random
tiempo_hombre_4= random.randint(6,8)
hombre_5="Asistente 5 tanquea el vehículo"
import random
tiempo_hombre_5= random.randint(6,8)
tiempo_total=(tiempo_hombre_1+tiempo_hombre_2+tiempo_hombre_3+tiempo_hombre_4+tiempo_hombre_5)/5
car_run='Todo listo en' ,tiempo_total,  'sg y arranca el vehículo'

print(car_stop)
print(hombre_1)
print("y el tiempo que demora en el cambio es de " ,tiempo_hombre_1, "sg\n")
print(hombre_2)
print("y el tiempo que demora en el cambio es de " ,tiempo_hombre_2, "sg\n")
print(hombre_3)
print("y el tiempo que demora en el cambio es de " ,tiempo_hombre_3, "sg\n")
print(hombre_4)
print("y el tiempo que demora en el cambio es de " ,tiempo_hombre_4, "sg\n")
print(hombre_5)
print("y el tiempo que demora en el tanqueo es de " ,tiempo_hombre_5, "sg\n")
print(car_run)

