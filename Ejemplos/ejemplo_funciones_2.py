def function_1(params):
    print(type(params))
    '''for value in params.values():
        print(value)'''

def test_function(name, age, bonus='undefined'):
    #bloque de código
    print(name, " ", bonus, " ", age)

def math_operation(num1, num2, operator):
    local_result = 'NaN'
    
    if operator == '+':
        local_result = num1 + num2
    elif operator == '-':
        local_result = num1 - num2
    elif operator == '*':
        local_result = 0
        for i in range(num2): #range(0, num2, 1)
            local_result = math_operation(local_result, num1, '+')   
    else:
        local_result = "Unknown operation"

    return local_result
#End of function

result = math_operation(6, 9, '*')

print("Result is: ", result)


"""#test_function("Kobayashi", "aero", 35)
#test_function(bonus='aero', name='Kobayashi', age=35)
test_function(name='Kobayashi', age=35, bonus='aero')

test_function(name="S. Montoya", age=17)

#function_1(driver_name = "Ricciardo", driver_bonus = "aero", driver_age = 30)
#function_1("Ricciardo", "aero", 30)
#function_1([40, 50, 30])"""
