import racing_base_module as rbm

class F1Track(rbm.RacingElement):
    place = "N/A"
    bonus = {}

    def set_bonus(self, bonus_type):
        if(bonus_type == "chasis" or bonus_type == "motor" or tipo == "aero"):
            self.bonus.add(bonus_type)
        else:
            return "Sorry, the bonus does not apply"


class F1Driver(rbm.RacingElement):
    bonus = "N/A"
    team = "N/A"

    def __init__(self, name, team):
        super().__init__(name)
        self.team = team

    def set_bonus(self, bonus_type):
        if(bonus_type == "chasis" or bonus_type == "motor" or tipo == "aero"):
            self.bonus = bonus_type
        else:
            return "Sorry, the bonus does not apply"
