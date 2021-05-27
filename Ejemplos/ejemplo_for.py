
my_list = [10, 30, "11", 50, True]
message_template = "The number is: {0}"

for item in my_list:
    print(message_template.format(item))

#for( i = 0; i < 10; i++)
for number in range(0, 10, 2): # Range retorna una colección de 10 numeros
    print("Conteo: ", number)
