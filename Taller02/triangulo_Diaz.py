
output_message_template = "El triángulo con ángulo uno de {0}°, ángulo dos {1}°, y ángulo tres {2}°, es un Triángulo {3}"
input_message = "Introduce el ángulo {0}° de {1}° a {2}° grados:"


print("*"*75)
print("* Programa para determinar ¿Qué tipo de triángulo és? *")
print("*************************************************************************** \n")

angulo_1 = int(input(input_message.format("uno", 1, 178)))
angulo_2 = int(input(input_message.format("dos", 1, 178)))
angulo_3 = int(input(input_message.format("tres", 1, 178)))

if angulo_1 < 90 and angulo_2 < 90 and angulo_3 < 90:
    print("El triángulo con ángulo uno de", angulo_1, "ángulo dos de", angulo_2, "y ángulo tres de", angulo_3, "es un Triángulo Acutángulo ")
    print(output_message_template.format(angulo_1, angulo_2, angulo_3, "Acutángulo"))
    
elif angulo_1 == 90 and angulo_2 < 90 and angulo_3 < 90 or angulo_2 ==90 and angulo_1 < 90 and angulo_3 < 90 or angulo_3 == 90 and angulo_2 < 90 and angulo_1 < 90:
    print("El triángulo con ángulo uno de", angulo_1, "ángulo dos de", angulo_2, "y ángulo tres de", angulo_3,"es un Triángulo Rectángulo ")
    print(output_message_template.format(angulo_1, angulo_2, angulo_3, "Rectángulo"))

elif angulo_1 > 90 and angulo_2 < 90 and angulo_3 < 90 or angulo_2 > 90 and angulo_1 < 90 and angulo_3 < 90 or angulo_3 > 90 and angulo_1 < 90 and angulo_2 < 90:
    print("El triángulo con ángulo uno de", angulo_1, "ángulo dos de", angulo_2, "y ángulo tres de", angulo_3,"es un Triángulo Obtusángulo ")
    print(output_message_template.format(angulo_1, angulo_2, angulo_3, "Obtusángulo"))
    

else:
    print("La condición NO se ha cumplido")

print("Fin.")
