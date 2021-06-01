import random

pitstop_template = 'Se detiene el vehículo y de manera simultánea realizan el trabajo:\n'
pitstop_template1 = 'Mecánico {0} quita llanta usada y pone llanta {0} nueva.'
pitstop_template2 = 'Mecánico {0} tanquea el vehículo.'
pitstop_template3 = 'y el tiempo que demora en el cambio es de'
pitstop_template4 = ' seg\n'
pitstop_template5 = 'y el tiempo que demora en el tanqueo es de '
pitstop_template6 = 'Sale de pits el vehiculo en aproximadamente '

print("***************************")
print("* EXERCISE PITSTOP *")
print("***************************\n")

car_stop = pitstop_template

mecánico_1 = pitstop_template1.format(1)
tiempo_mecánico_1= random.randint(6,8)

mecánico_2 = pitstop_template1.format(2)
tiempo_mecánico_2= random.randint(6,8)

mecánico_3 = pitstop_template1.format(3)
tiempo_mecánico_3= random.randint(6,8)

mecánico_4 = pitstop_template1.format(4)
tiempo_mecánico_4= random.randint(6,8)

mecánico_5 = pitstop_template2.format(5)
tiempo_mecánico_5= random.randint(6,8)

tiempo_total=(tiempo_mecánico_1 + tiempo_mecánico_2 + tiempo_mecánico_3 + tiempo_mecánico_4 + tiempo_mecánico_5)/5
car_run = pitstop_template6 + str(tiempo_total)+  pitstop_template4

print(car_stop)
print(mecánico_1)
print(pitstop_template3 ,tiempo_mecánico_1, pitstop_template4)
print(mecánico_2)
print(pitstop_template3 ,tiempo_mecánico_2, pitstop_template4)
print(mecánico_3)
print(pitstop_template3 ,tiempo_mecánico_3, pitstop_template4)
print(mecánico_4)
print(pitstop_template3 ,tiempo_mecánico_4, pitstop_template4)
print(mecánico_5)
print(pitstop_template5 ,tiempo_mecánico_5, pitstop_template4)
print(car_run)

