# # def sum_numbers(x, y, z):
# #     total = list(x, y, z)
# #
# # sum_numbers(x=5,y=2,z=10)
#
#
#
#
#
# def sum_numbers(*args):
#     total = sum(args)
#     return total
#
# print(sum_numbers(5, 3, 10, 25, 22))



#
# def sum_numbers(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
#
# print(sum_numbers(5, 3, 10, 25, 22))




# def hello_user():
#     name = "Дима"
#     print(f"Привет, {name}!")
#
# hello_user()



# name = 3
# def hello_user():
#     global name
#     name = name * 10
#     print(name)
#
# hello_user()
# print(name)





#
# def outher():
#     count = 0
#     def inner():
#         nonlocal count
#         count = count + 10
#         print(count)
#
#     inner()
#
# outher()





# def calc(x):
#     count = 0
#     total = 0
#
#     for i in str(x):
#         if int(i) % 2 == 0:
#             count += 1
#             total += int(i)
#     return count, total
#
# print(calc(678))





# def calc(*args):
#     count = 0
#     total = 0
#     for i in args:
#         count += 1
#         total += i
#     return total / count
#
# print(calc(42, 52, 32))

# def calc(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total / len(args)
#
# print(calc(42, 52, 32))




# a = "У лукоморья дуб зеленый."
# print(len(a))




things = ["Телефон", "Планшет", "Ручка", "Клавиатура"]
print(len(things))