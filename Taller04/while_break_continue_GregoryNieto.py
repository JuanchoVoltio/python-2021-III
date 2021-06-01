print('*******************************************')
print('*EXERCISE while, break and continue *')
print('*******************************************\n')

pregunta1  =  '¿Qué edad tiene? '
pregunta2  =  '¿En qué ciudad vive? '

age  =  0
city  =  ''

while not ( age  >  50  and  city  ==  'Facatativá' ):
    age  =  int ( input ( pregunta1 ))
    if( age  <  50 ):
        continue
    city  =  input ( pregunta2 )
    #pregunta 3
    #pregunta 4
else :
    print ( '¡Se puede vacunar contra el COVID!' )
