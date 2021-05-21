#ENTRADAS
import random

pits = int(input("El vehículo necesita parar en boxes para cambio de neumáticos: 1. Si o 2. No"))
#PROOCESO
if pits == 1:
    print("*******PITS*********")
    print("")
    print("La próxima vuelta se debe ingresar a la zona de pits")
    print("")
    print("¡¡¡¡¡¡¡ALERTA DE APROXIMACIÓN A ZONA DE PITS!!!!!!!")
    print("Recuerde que la velocidad máxima en pitsline es 80km/h")
    print("****************************************************")
    print("")
    print("")
    print("¡¡¡¡¡¡¡¡¡¡¡ALERTA EQUIPO DE MECÁNICOS!!!!!!!!!!!!")
    print("............Vehículo aproximandose................")
    print("")
    print("*********VEHÍCULO DETENIDO***********")
    print("02 Mecánicos deben alzar el vehículo en la parte delantera y trasera")
    print("")
    print("*********CAMBIO DE NEUMÁTICOS*********")
    print ("El cambio se realiza con grupos compuetos por 03 mecánicos; 01 grupo por cada rueda")
    print ("Equipo 1 cambia la rueda derecha trasera")
    tiempo_1=(random.uniform(1,1.81))
    print ("Equipo 2 cambia la rueda  izquierda trasera")
    tiempo_2=(random.uniform(1,1.81))
    print ("Equipo 3 cambia la rueda  derecha delantera")
    tiempo_3=(random.uniform(1,1.81))
    print ("Equipo 4 cambia la rueda  izquierda delantera")
    tiempo_4=(random.uniform(1,1.81))
    print("")
    print("")
    record = 1.82 #El record de pistop en la Formula 1 lo tiene la escuderia Red Bull , en el año 2013 lo estableció en 1.82 segundos
    if tiempo_1 < record or tiempo_2 < record or tiempo_3 < record or tiempo_4 < record:
        print ("Se ha establecido un nuevo record de scuderia en los pitstop")
        print ("¡¡¡¡¡¡FELICIDADES!!!!!! Acaban de superar a la Scudería Red Bull")
        print ("y su record del añoo 2013 en la F1, establecido en 1.82segundos")
        print("")
        print("")
else:
    if pits == 2:
        print("Verifique los indicadores del vehículo")
    else:
        print("Digíte uno de los valores válidos: 1. Para ingreso a pits - 2. Para continuar")
#SALIDAS
print("El tiempo en el pitstop del equipo 1 fué: ", tiempo_1)
print("El tiempo en el pitstop del equipo 2 fué: ", tiempo_2)
print("El tiempo en el pitstop del equipo 3 fué: ", tiempo_3)
print("El tiempo en el pitstop del equipo 4 fué: ", tiempo_4)


