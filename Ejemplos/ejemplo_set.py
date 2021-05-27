
my_set = {10, 30, 50, 40, 20}
message_template = "The number is: {0}"

print(my_set)

my_other_set = {30, 40, 80, -20}

print(my_other_set)

print(my_set.symmetric_difference(my_other_set))

'''my_set.update(my_list)

print(my_set)

item_to_search = 30

for item in my_set:
    print(message_template.format(item))
    if item == item_to_search:
        print("Found!")
        break

print(my_set)'''
print("End of program")
