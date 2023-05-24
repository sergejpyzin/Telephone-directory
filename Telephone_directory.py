# def user_imprt():
#     with open ("telephone_directory.txt", "a", encoding="utf-8") as file:
#         file.write(input("Введите Фамилию: ") + "\t")
#         file.write(input("Введите Имя: ") + "\t")
#         file.write(input("Введите Отчество: ") + "\t")
#         file.write(str(int(input("Введите телефон: "))) + "\n")
#
#
# user_imprt()

with open('telephone_directory.txt', 'r', encoding="utf-8") as file:
    # words = input()
    line = file.readline().split()
    print(line)
    for el in line:
        print(el)
