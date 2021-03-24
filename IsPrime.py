print('\033[37m' + "Для завершения работы отправьте пустую строку")
a = input('\033[37m' + "Введите число больше 1: ")
while len(a) != 0:
    while ' ' in a:
        a = a.replace(" ", "")
    try:
        a = int(a)
    except ValueError:
        print('\033[31m' + "Ошибка: " + '\033[37m' + "Введеное значение не является числом!")
        print('\033[37m' + "Для завершения работы отправьте пустую строку")
        a = input("Введите число больше 1: ")
        continue
    else:
        if a < 2:
            print('\033[31m' + "Ошибка: " + '\033[37m' + "Число должно быть больше 1!")
            print('\033[37m' + "Для завершения работы отправьте пустую строку")
            a = input("Введите число больше 1: ")
            continue
        if a == 2:
            print("Число " + '\033[31m' + "2" + '\033[37m' + " простое")
            print("Множитель " + '\033[31m' + "2" + '\033[37m')
            print('\033[37m' + "Для завершения работы отправьте пустую строку")
            a = input("Введите число больше 1: ")
            continue
        if a % 2 == 0:
            print("Число " + '\033[31m' + str(a) + '\033[37m' + " не простое")
            print("Множитель " + '\033[31m' + "2" + '\033[37m')
            print('\033[37m' + "Для завершения работы отправьте пустую строку")
            a = input("Введите число больше 1: ")
            continue
        b = 3
        while b * b <= a and a % b != 0:
            b += 2
        if a % b == 0 and a != b:
            print("Число " + '\033[31m' + str(a) + '\033[37m' + " не простое")
            print("Множитель " + '\033[31m' + str(b) + '\033[37m')
        else:
            print("Число " + '\033[31m' + str(a) + '\033[37m' + " простое")
        print('\033[37m' + "Для завершения работы отправьте пустую строку")
        a = input("Введите число больше 1: ")
        continue