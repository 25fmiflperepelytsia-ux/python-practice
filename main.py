try:
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    operation = input("Введіть знак операції (+, -, *, /): ")

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        result = a / b
    else:
        raise ValueError("Некоректна операція")

    print("Результат:", result)

except ValueError:
    print("Помилка: введено нечислове значення або некоректну операцію!")

except ZeroDivisionError:
    print("Помилка: ділення на нуль неможливе!")
