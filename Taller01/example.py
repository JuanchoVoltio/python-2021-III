edades_salon_1 = [10, 5, 8]
edades_salon_2 = (8, 7, 11, 5, 6, 7)

print("Salon 1: ", edades_salon_1)
print("Salon 2: ", edades_salon_2)

#edades_salon_1.insert(int(input("Index: ")), input("Add new age: "))

print(edades_salon_1)

edades_salon_1.extend(edades_salon_2)

print(edades_salon_2)

print(edades_salon_2.count(4))
