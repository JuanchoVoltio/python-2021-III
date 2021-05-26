
min_base_time = 67
max_base_time = 71

driver_names = ['G. Chavez', 'C. Muñoz', 'D. Ricciardo']
driver_bonus = ['a', 'c', 'c']

track_names = ('Silverstone', 'Suzuka')
track_bonuses = ('e, a', 'a, c')

driver_description_template = 'El piloto {0} tiene bono de {1}'
track_description_template = 'El GP de {0} tiene bonos de {1}'
lap_time_template = 'El piloto {0} hizo un tiempo de {1} seg. en el GP de {2}'

i_driver = int(input('Ingrese un índice para el piloto: '))

i_track = int(input('Ingrese un índice para la pista: '))


#TODO: Generar el tiempo aleatorio base para un piloto
base_time = random(min_base_time, max_base_time)

#TODO: Verificar que el piloto tenga un bono que coincida con el de la pista
#Si coincide aplico el bono, en caso contrario el tiempo base queda igual

#TODO: Imprimir el mensaje con el tiempo de vuelta para la pista
print(lap_time_template.format(driver_names[i_driver], base_time, track_names[i_track]))
