import f1_module as f1m
import racing_base_module as rbm

track1 = f1m.F1Track("LeMans")
print(track1.name)

driver1 = f1m.F1Driver("C. Sainz", "Ferrari")
print(driver1.name, " - ", driver1.team)

print(track1.get_time_bonus(rbm.bonus_engine))
print(rbm.bonus_aero)
rbm.say_hello()

