def filling_directory():
    with open("telephone_directory.txt", "a", encoding="utf-8") as file:
        file.write(input("Введите Фамилию: ") + " ")
        file.write(input("Введите Имя: ") + " ")
        file.write(input("Введите Отчество: ") + " ")
        file.write(str(int(input("Введите телефон: "))) + "\n")


def user_imprt():
    filling_directory()
    while True:
        answer = int(input("Вы хотите продолжить, введите ответ (1 - да, продолжить; 2 - нет, выйти в главное меню; ) "
                           "нажмите любую клавишу для завершения работы программы.\n"))
        if answer == 1:
            filling_directory()
        elif answer == 2:
            user_interaction()
        else:
            break


def user_search():
    with open('telephone_directory.txt', 'r', encoding="utf-8") as file:
        search_el = input()
        line = file.readline().split()
        while line:
            for el in line:
                if el == search_el:
                    return print(*line)
            line = file.readline().split()


def user_interaction():
    choice = int(input("Выберете метод взаимодействия с телефонным справочником. Введите номер операции  "
                       "(1 - заполнение справочника; 2 - поиск абонента):\n"))
    if choice == 1:
        return user_imprt()
    elif choice == 2:
        return user_search()
    else:
        print("Извините. Введенный номер операции некоректен")
        return user_interaction()


user_interaction()
