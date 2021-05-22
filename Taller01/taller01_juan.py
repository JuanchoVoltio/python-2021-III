import random

crew_member_template_massage = "pareja {0} cambia llanta {0}"

print("="*24)
print("taller01, parada de pits")
print("========================\n")

vehiculoInactivo = "llega el vehículo a pits, sincrónicamente dos mecánicos por rueda cambian: \n"

pareja_1 = crew_member_template_massage.format(1)
tiempo_pareja_mecanicos_1 = random.randint(1,3)

pareja_2 = crew_member_template_massage.format(2)
tiempo_pareja_mecanicos_2 = random.randint(1,3)

pareja_3 = crew_member_template_massage.format(3)
tiempo_pareja_mecanicos_3 = random.randint(1,3)

pareja_4 = crew_member_template_massage.format(4)
tiempo_pareja_mecanicos_4 =  random.randint(1,3)


tanquear = "\nrepostaje de combustible,'Sin Tanqueo' \n"
vehiculoActivo = "Sincronización completa, estado OK, salida según tiempo promedio gastado por cambio de llanta en segundos \n"

promedio_en_segundos = (tiempo_pareja_mecanicos_1 + tiempo_pareja_mecanicos_2 + tiempo_pareja_mecanicos_3 + tiempo_pareja_mecanicos_4 ) / 4

print(vehiculoInactivo)
print(pareja_1)
print("Tiempo de demora en el cambio " ,tiempo_pareja_mecanicos_1,"sg \n")
print(pareja_2 )
print("Tiempo de demora en el cambio " ,tiempo_pareja_mecanicos_2,"sg \n")
print(pareja_3)
print("Tiempo de demora en el cambio " ,tiempo_pareja_mecanicos_3,"sg \n")
print(pareja_4)
print("Tiempo de demora en el cambio " ,tiempo_pareja_mecanicos_4,"sg \n" )
print(tanquear,"\n")
print(vehiculoActivo,"\n")
print("El intervalo de tiempo total que gastó en cambio de las '4' llantas fue de: " ,promedio_en_segundos, "Sg \n")
print("Fin.")

