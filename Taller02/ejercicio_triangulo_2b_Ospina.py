#ENTRADAS
#Se espera que el usuario ingrese por consola el valor de cada uno de los tres angulos, asignando cada valor a una variable"""
angulo1 = float(input("Digite el valor del primer angulo:   "))
angulo2 = float(input("Digite el valor del segundo angulo:   "))
angulo3 = float(input("Digite el valor del tercer angulo:   "))

#PROCESO Y SALIDAS
if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print ("De acuerdo a los datos ingresados, el poligono es un triángulo rectángulo")
else:
    if (angulo1 != 90 and angulo2 != 90 and angulo3 != 90) and (angulo1 > 90 or angulo2 > 90 or angulo3 > 90):
        print ("De acuerdo a los datos ingresados, el poligono es un triángulo oblicuángulo de tipo obtusángulo")
    else:
        print ("De acuerdo a los datos ingresados, el poligono es un triángulo oblicuángulo de tipo acutángulo")

