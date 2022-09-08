#Pick the Equation
what_equation_to_pick = int(
    input(
        f'What equation do you want to solve for: 1 = Newton second law, 2 = Pythagorean theorem :'
    ))

#Newtons Second Law
if what_equation_to_pick == 1:
    test_variable = True
    while test_variable == True:
        possible_variable_solving_for = input(
            f' What would you like to solve for?, f, m, or a : ')
        if possible_variable_solving_for == "f":
            m = int(input('What is m equal to:'))
            a = int(input('What is a equal to:'))
            f = m * a
            print(f'f = {f}')
            test_variable = False
        elif possible_variable_solving_for == "a":
            m = int(input('What is m equal to:'))
            f = int(input('What is f equal to:'))
            a = f / m
            print(f'a = {a}')
            test_variable = False
        elif possible_variable_solving_for == "m":
            f = int(input('What is f equal to:'))
            a = int(input('What is a equal to:'))
            m = f / a
            print(f'm = {m}')
            test_variable = False

#Pythagorean Therum
elif what_equation_to_pick == 2:
    test_variable = True
    while test_variable == True:
        possible_variable_solving_for = input(
            f' What would you like to solve for?, a, b, or c : ')
        if possible_variable_solving_for == "a":
            b = int(input('What is a equal to:'))
            c = int(input('What is c equal to:'))
            a = ((c * c) / (b * b)) / 2
            print(f'f = {b}')
            test_variable = False
        elif possible_variable_solving_for == "b":
            a = int(input('What is a equal to:'))
            c = int(input('What is c equal to:'))
            b = ((c * c) / (a * a)) / 2
            print(f'a = {a}')
            test_variable = False
        elif possible_variable_solving_for == "c":
            a = int(input('What is a equal to:'))
            b = int(input('What is b equal to:'))
            c = ((a * a) * (b * b)) / 2
            print(f'm = {c}')
            test_variable = False
