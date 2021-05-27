
my_dict = {
    'a' : 10,
    'b' : 30,
    'c' : 50,
    3 : 40,
    -2 : 20
    }

for current_key in my_dict: #Iterar sobre las llaves
    print(current_key)

for current_value in my_dict.values(): #Iterar sobre los valores
    print(current_value)

for curr_key, curr_value in my_dict.items(): #Iterar sobre las llaves y valores
    print("key: ", curr_key, " | value: ", curr_value)

my_dict.pop('c')

print(my_dict)
