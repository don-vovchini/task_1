print('\033[37m' + "Для завершения работы отправьте пустую строку")
text = input('\033[37m' + "Введите текст:\n")
while len(text) != 0:
    print("В данном тексте содержится следующее количество гласных букв латинского алфавита:")
    print("a = {0}; e = {1}; i = {2}; o = {3}; u = {4}; y = {5}".format(str(text.count('a')), str(text.count('e')), str(text.count('i')), str(text.count('o')),
                                                                        str(text.count('u')), str(text.count('y'))))
    print('\033[37m' + "Для завершения работы отправьте пустую строку")
    text = input('\033[37m' + "Введите текст:\n")
