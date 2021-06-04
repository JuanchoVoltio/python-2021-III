print('='*31)
print('*EXERCISE PISTAS, PILOTOS Y BONUS*')
print('='*31)

import random

min_time  =  67
max_time  =  70

driver_names  = [ 'G. Chávez ' , ' C. Muñoz ' , ' D. Ricciardo ' , ' kobayashi ' , ' P. Wherlein' ]
driver_bonus  = [ 'a' , 'c' , 'c' , 'e' , 'e' ]

track_names  = ( 'Silverstone' , 'Suzuka' , 'Long Beach' , 'Interlagos' )
track_bonuses  = ( 'e, a' , 'a, c' , 'c, a' , 'e, c')

driver_description_template  =  'El piloto {0} tiene bono de {1}'
track_description_template  =  'El GP de {0} tiene bonos de {1}'
lap_time_template  =  'El piloto {0} hizo un tiempo de {1} seg. en el GP de {2} '

i_driver  =  int ( input ( 'Ingrese un índice para el piloto:' ))

i_track  =  int ( input ( 'Ingrese un índice para la pista:' ))


#TODO: Generar el tiempo aleatorio base para un piloto
base_time  =  random.randint ( min_time , max_time )
print(base_time,driver_names)

#TODO: Verificar que el piloto tenga un bono que coincida con el de la pista
#Si coincide aplico el bono, en caso contrario el tiempo base queda igual
if driver_bonus[i_driver] in track_bonuses[i_track]:
    if driver_bonus[i_driver] == 'a':
        base_time = base_time - 0.5
        
    elif driver_bonus[i_driver] == 'e':    
        base_time = base_time - 0.4

    elif driver_bonus[i_driver] == 'c':    
        base_time = base_time - 0.6

#TODO: Imprimir el mensaje con el tiempo de vuelta para la pista
print (lap_time_template.format( driver_names[i_driver], base_time , track_names [i_track]))
