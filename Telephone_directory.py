def user_imprt():
    with open ("telephone_directory.txt", "a", encoding="utf-8") as file:
        file.write(input("Введите Фамилию: ") + " ")
        file.write(input("Введите Имя: ") + " ")
        file.write(input("Введите Отчество: ") + " ")
        file.write(str(int(input("Введите телефон: "))) + "\n")
#
#
user_imprt()

# with open('telephone_directory.txt', 'r', encoding="utf-8") as file:
#     words = input()
#     line = file.readline().split()
#     # some_line = file.readline()
#     while line:
#         for el in line:
#             if el == words:
#                 print(*line)
#                 break
#         line = file.readline().split()
#         # some_line = file.readline()

