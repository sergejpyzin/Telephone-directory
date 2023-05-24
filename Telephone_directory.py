# def user_imprt():
#     with open ("telephone_directory.txt", "a", encoding="utf-8") as file:
#         file.write(input("Введите Фамилию: ") + " ")
#         file.write(input("Введите Имя: ") + " ")
#         file.write(input("Введите Отчество: ") + " ")
#         file.write(str(int(input("Введите телефон: "))) + "\n")
# #
# #
# user_imprt()

def user_search():
    with open('telephone_directory.txt', 'r', encoding="utf-8") as file:
        search_word = input()
        line = file.readline().split()
        while line:
            for el in line:
                if el == search_word:
                    print(*line)
            line = file.readline().split()

