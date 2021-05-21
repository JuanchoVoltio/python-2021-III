import random

print("========================")
print("taller01, parada de pits")
print("========================\n")

vehiculoInactivo = "llega el vehículo a pits, sincrónicamente dos mecánicos por rueda cambian: \n"

mecanicos_1_2 = "cambian llanta 1, 'Si', duración cambio de llanta en segundos: \n"

random_variable_1_2 = random.randint(1,3)
mecanicos_3_4 = "cambian llanta 2, 'Si', duración cambio de llanta en segundos: \n"

random_variable_3_4 = random.randint(1,3)
mecanicos_5_6 = "cambian llanta 3, 'Si', duración cambio de llanta en segundos: \n"

random_variable_5_6 = random.randint(1,3)
mecanicos_7_8 = "cambian llanta 4, 'Si', duración cambio de llanta en segundos: \n"

random_variable_7_8 = random.randint(1,3)
tanquear = "repostaje de combustible,'Sin Tanqueo' \n"
vehiculoActivo = "Sincronización completa, estado OK, salida según tiempo promedio gastado por cambio de llanta en segundos \n"

promedio_en_segundos = (random_variable_1_2 + random_variable_3_4 + random_variable_5_6 + random_variable_7_8 ) / 4

print(vehiculoInactivo)
print(mecanicos_1_2)
print(random_variable_1_2)
print(mecanicos_3_4)
print(random_variable_3_4)
print(mecanicos_5_6)
print(random_variable_5_6)
print(mecanicos_7_8)
print(random_variable_7_8)
print(tanquear)
print(vehiculoActivo)
print("El intervalo de tiempo que gastó en cambio de llantas fue de: " ,promedio_en_segundos,'Sg')
print("Fin.")

