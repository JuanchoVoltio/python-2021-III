
first_question  =  '¿Qué edad tiene? '
second_question  =  '¿En qué ciudad vive? '

age  =  0
city  =  ''

while not ( age  >  18  and  city  ==  'Medellín' ):
    age  =  int ( input ( first_question ))
    if( age  <  18 ):
        continue
    city  =  input ( second_question )
    #pregunta 3
    #pregunta 4
else :
    print ( '¡Encontré a la persona!' )
