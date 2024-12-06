# cars = ["Mersedes", "BMW", "АвтоВАЗ", "Tesla", "Porshe"]
#
# for i in cars:
#     print(i.lower())

# def asd(name):
#     print(f"Привет, {name}!")
#
# a = input("Введите имя: ")
# asd(a)

# def das(number):
#     print(number ** 2)
#
# num = int(input("Введите число: "))
# das(num)

# def asd(n1, n2):
#     return n1 + n2
#
# print(asd(2, 3))

# def ds(text):
#     print(f"Номер вашей машины: {text}")
#
# a = input("Введите номер вашей машины: ")
# b = ds(a)
# print(b)

# def ds(text):
#     return text
#
# a = input("Введите номер вашей машины: ")
# b = ds(a)
# print(b[len(b)-2:len(b)])

# a = "Hello, World!"

# print(a[1:10])
# print(a[:7])
# print(a[0:13:1])
# print(a[::-1])
# print(len(a))
# print(a[5:len(a)])

# a = ["Banana", "Apple", "Meet", "Milk", "Bread"]
#
# # print(a[1:len(a)])
# a.append("Pineapple")
# a.remove("Apple")
#
# print(a)

# numbers = [5, 2, 10, 23, 42]
#
# print(sum(numbers))
#
# b = 0
# def calc():
#     global b
#     for i in numbers:
#         b += i
#     print(b)
#
# calc()


# def asd(n1, n2):
#     print(min(n1, n2))
#
# asd(6, 10)


def pl(width=0, length=0):
    return width * length

print(pl())