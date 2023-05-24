def user_imprt():
    with open ("telephone_directory.txt", "a", encoding="utf-8") as file:
        file.write(input("Введите Фамилию: ") + " ")
        file.write(input("Введите Имя: ") + " ")
        file.write(input("Введите Отчество: ") + " ")
        file.write(str(int(input("Введите телефон: "))) + "\n")


def user_search():
    with open('telephone_directory.txt', 'r', encoding="utf-8") as file:
        search_word = input()
        line = file.readline().split()
        while line:
            for el in line:
                if el == search_word:
                    return print(*line)
            line = file.readline().split()

def user_interaction (choice):
    if choice == 1:
        return user_imprt()
    elif choice == 2:
        return user_search()
    else:
        return print("Извините. Введенный номер операции некоректен")



user_interaction(int(input("Выберете метод взаимодействия с телефонным справочником. Введите номер операции  "
                                 "(1 - заполнение справочника; 2 - поиск абонента):\n")))