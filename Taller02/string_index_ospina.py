texto=("La {} p se encuentra en el indice:  ")
cadena = "programoenpythonymediviertoalaprenderperosinpausaysinprisa"
letra = "p"
print ( "Se extrajo la palabra: ", "*"*10 , cadena[19:27].upper() ,"*"*10, " de la cadena", cadena)
print ("")
print ("")
print ("La cantidad de palabras que inician con la letra P es: ",cadena.count(letra))
primer_indice = cadena.index(letra)
print (texto.format("primera"), primer_indice)
segundo_indice = cadena.index(letra, primer_indice + 1)
print (texto.format("segunda"),segundo_indice)
tercer_indice = cadena.index(letra, segundo_indice + 1)
print (texto.format("tercera"), tercer_indice)
cuarto_indice = cadena.index(letra, tercer_indice + 1)
print (texto.format("cuarta"), cuarto_indice)
quinto_indice = cadena.index(letra, cuarto_indice + 1)
print (texto.format("quinta"), quinto_indice)
sexto_indice = cadena.index(letra, quinto_indice + 1)
print (texto.format("sexta"), sexto_indice)




