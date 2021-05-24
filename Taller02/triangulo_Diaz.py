
crew_member_template_massage = "El triangulo con {0} es un triángulo {0}"

print("*"*75)
print("* Programa para determinar ¿Qué tipo de triángulo és? *")
print("*************************************************************************** \n")

angulo_1 = int(input("Introduce el ángulo uno de 0° a 360° grados:"))
angulo_2 = int(input("Introduce el ángulo dos de 0° a 360° grados:"))
angulo_3 = int(input("Introduce el ángulo tres de 0° a 360° grados:"))

if angulo_1 < 90 and angulo_2 < 90 and angulo_3 < 90:
    print("El triángulo con ángulo uno de", angulo_1, "ángulo dos de", angulo_2, "Y ángulo tres de", angulo_3, "es un Triángulo Acutángulo ")

elif angulo_1 == 90 and angulo_2 < 90 and angulo_3 < 90 or angulo_2 ==90 and angulo_1 < 90 and angulo_3 < 90 or angulo_3 == 90 and angulo_2 < 90 and angulo_1 < 90:
    print("El triángulo con ángulo uno de", angulo_1, "ángulo dos de", angulo_2, "Y ángulo tres de", angulo_3,"es un Triángulo Rectángulo ")

elif angulo_1 > 90 and angulo_2 < 90 and angulo_3 < 90 or angulo_2 > 90 and angulo_1 < 90 and angulo_3 < 90 or angulo_3 > 90 and angulo_1 < 90 and angulo_2 < 90:
    print("El triángulo con ángulo uno de", angulo_1, "ángulo dos de", angulo_2, "Y ángulo tres de", angulo_3,"es un Triángulo Obtusángulo ")

else:
    print("La condición NO se ha cumplido")

print("Fin.")
