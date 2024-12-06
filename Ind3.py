# Функция принимает два параметра из чисел и возвращает все нечетные числа между ними

# def calc(number1, number2):
#     even = []
#     for i in range(number1, number2):
#         if i % 2 == 1:
#             even.append(i)
#     return even
#
# print(calc(1, 6))


# Нужно написать функцию которая в качестве параметра принимает список из целых чисел
# некоторые числа должны повторяться
# функция возвращает другой список но с уникальными значениями

# numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# def unical_numbers(list):
#     unical_numbers_list = []
#     for i in numbers:
#         if i not in unical_numbers_list:
#             unical_numbers_list.append(i)
#     return unical_numbers_list
#
# print(unical_numbers(numbers))


# text = "У лукоморья дуб зеленый"
#
# print("нет" not in text)




# Кортеж - tuple()

# i = ("Матвей", "Илья", "Саня", "Даниил")
# print(i[3])
# for g in i:
#     print(g.lower())
# print(i)

# g1 = (5, 2, 10, 30, 52, 60, 10, 5, 2, 10, 30, 52, 60, 10, 5, 2, 10, 30, 52, 60, 10, 5, 2, 10, 30, 52, 60, 10)
# g2 = [5, 2, 10, 30, 52, 60, 10, 5, 2, 10, 30, 52, 60, 10, 5, 2, 10, 30, 52, 60, 10, 5, 2, 10, 30, 52, 60, 10]

# print(g1.__sizeof__())
# print(g2.__sizeof__())
# print(g.count(10))



# Словарь(хэш-таблица, объект)

# employer = {
#     "name":"Дима",
#     # "name":"Илья",
#     "age":13,
#     "town":"Uren"
# }

# employer["age"] = 14
# print(employer["town"])
# print(employer["age"])
# print(len(employer))


# Словарь юзера

my_dict = {
    "Дима":{
        "Phone":"7940020011",
        "Telegram":"@dima4449",
        "VK":"id123471"
    },
    "Илья": {
        "Phone": "7940020012",
        "Telegram": "@ilya1234",
        "VK": "id333472"
    },
    "Саша": {
        "Phone": "7940020013",
        "Telegram": "@sanya2324",
        "VK": "id223473"
    }
}

# for i in my_dict:
#     print(i)

get_user = my_dict[input("Введите имя: ")][input("Введите данные контакта: ")]
print(get_user)
print(my_dict.__sizeof__())