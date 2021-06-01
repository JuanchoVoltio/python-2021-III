'''print("="*45)
print("Ejercicio clase, funciones, objetos --Driver--")
print("="*45)'''

class F1_Driver:
    name = "Undefinied"
    bonus = "N/A"

    def get_time_bonus(self, time):
        if(time == "67.4" or time == "67.6" or time == "67.5" or time == "67.6" or time == "67.4"):
            return self.time_bonus
        else:
            return "Sorry, the bonus time does not match"


driver_1 = F1_Driver()
driver_1.name = "tiempo"
driver_1.time_bonus = "Si aplica para ti"

tiempo = input ("what time do you have ?\n")
answer = driver_1.get_time_bonus(tiempo)
print(answer)
