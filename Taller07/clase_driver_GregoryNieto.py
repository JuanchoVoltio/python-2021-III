'''print('************************************************')
print('*EXERCISE CLASE Y FUNCIONES (driver)*')
print('************************************************\n')'''


class F1Driver:
    name = ''
    bonus = ''
    motor = 0.4
    chasis = 0.6
    aerodin = 0.5

    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus

    def get_time_bonus (self, time):
        if (time == ''):
            return 'aplicas'

    def validacion(self, x):
        descuento = x
        return descuento

    for i in range(0, 3):
        try:
            entrada = int (input('¿Qué bono tiene?: '))
            break
        except ValueError:
            print('No existe ese bono')

    print(validacion(entrada))

    
        

