class F1Driver:
    name = "Undefinied" #debe ser inicializado
    phone_number = "N/A"
    bonus = ''

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = self.set_phone_number(phone_number)
    
    def radio_chat(self):
        print("Leave me alone, I know what I'm doing")

    def give_phone_number(self, who):
        if(who == "mom" or who == "friend"):
            return self.phone_number
        else:
            return "Sorry, I don't know you. I can't."

    def set_phone_number(self, number):
        self.phone_number = int(number)
        

#End of class F1Driver



driver_1 = F1Driver("Montoya", "455345") #001
print(driver_1.name, " creado.")

driver_2 = F1Driver("Raikkonen", "asda345") #020
print(driver_2.name, " creado.")
'''driver_2.radio_chat()

who = input("Who are you? ")

answer = driver_1.give_phone_number(who)
print(answer)



print(driver_1.name)'''

