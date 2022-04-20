def twenty_twenty():
    """Напишите выражение, результат которого будет 2020,
    используя только числа и операторы +, *, и -.

    >>> twenty_twenty()
    2020
    """
    print("Программа должна ввести 2020")
    s_1 = int(input("Введите число 1: "))
    s_2 = int(input("Введите число 2: "))
    op = input("Введите оператор: ")
    if op == "+":
        s = s_1 + s_2
    elif op == "*":
        s = s_1 * s_2
    elif op == "-":
        s = s_1 - s_2


    if s == 2020:
        print(s)
    else:
        print("Число не подходит")
    return

twenty_twenty()