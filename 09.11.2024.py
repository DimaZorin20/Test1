# def rules():
#     print(f"Привет!")
#     print("Прежде чем начать играть изучи правила:")
#     print("\n 1. Надо вести себя нормально.\n 2. Не мешать другим игрокам. \n 3. Поддерживать атмосферу в игре")
#
#
# rules()


# def name():
#     name = input("Введите свое имя: ")
#     surname = input("Введите свою фамилию: ")
#     print(f"Здравствуйте, {surname} {name}")
# name()


# def print_numbers():
#     number1 = int(input("Введите число: "))
#     for num in range(number1):
#         print(num)
#
# print_numbers()

def nums():
    number = int(input("Введите число: "))
    for n in range(0,2,2):
        number += n
    print(number)

nums()