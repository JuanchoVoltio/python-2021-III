texto=("La {} p se encuentra en el indice:  ")
una="primera"
dos="segunda"
tres="tercera"
cuatro="cuarta"
cinco="quinta"
seis="sexta"
cadena = "programoenpythonymediviertoalaprenderperosinpausaysinprisa"
print ( "Se extrajo la palabra: ", "*"*10 , cadena[19:27].upper() ,"*"*10, " de la cadena", cadena)
print ("")
print ("")
letra = "p"
print ("La cantidad de palabras que inician con la letra P es: ",cadena.count(letra))
primer_indice = (cadena.index(letra))
#print ("La primera P se encuentra en el indice: ",primer_indice)
print (texto.format(una), primer_indice)
segundo_indice = cadena.index(letra, primer_indice + 1)
#print ("La segunda P se encuentra en el indice: ",segundo_indice)
print (texto.format(dos), segundo_indice)
tercer_indice = cadena.index(letra, segundo_indice + 1)
#print ("La tercera P se encuentra en el indice: ",tercer_indice)
print (texto.format(tres), tercer_indice)
cuarto_indice = cadena.index(letra, tercer_indice + 1)
#print ("La cuartaP se encuentra en el indice: ",cuarto_indice)
print (texto.format(cuatro), cuarto_indice)
quinto_indice = cadena.index(letra, cuarto_indice + 1)
#print ("La quinta P se encuentra en el indice: ",quinto_indice)
print (texto.format(cinco), quinto_indice)
sexto_indice = cadena.index(letra, quinto_indice + 1)
#print ("La sexta P se encuentra en el indice: ",sexto_indice)
print (texto.format(seis), sexto_indice)




