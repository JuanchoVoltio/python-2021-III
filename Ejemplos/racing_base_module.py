bonus_chassis = "chassis"
bonus_aero = "aero"
bonus_engine = "motor"

def say_hello():
    print("Aloha")

class RacingElement:
    name = "Undefinied"

    def __init__(self, name):
        self.name = name
    
    def get_time_bonus(self, bonus_type):
        result = -1

        if bonus_type == bonus_chassis:
            result = 0.6
        elif bonus_type == bonus_aero:
            result = 0.5
        elif bonus_type == bonus_engine:
            result = 0.4

        return result



