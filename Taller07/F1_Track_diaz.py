'''print("="*45)
print("Ejercicio clase, funciones, objetos --Track--")
print("="*45)'''

class F1_Track:
    name = "Undefinied"
    place = "N/A"
    bonus = ""

    def get_bonus(self, tipo):
        if(tipo == "chasis, aero" or tipo == "motor, chasis" or tipo == "aero, chasis" or tipo == "motor, aero"):
            return self.bonus
        else:
            return "Sorry, the bonus does not apply"

track_1 = F1_Track()
track_1.name = "tipo"
track_1.bonus = "Si aplica para ti"

tipo = input ("what bonus do you have ?\n")
answer = track_1.get_bonus(tipo)
print(answer)
            

