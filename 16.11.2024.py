# def calc(n1, n2):
#     def sum():
#         print(n1 + n2)
#     def mult():
#         print(n1 * n2)
#
#     sum()
#     mult()
#
# calc(int(input("Введите первое число: ")), int(input("Введите второе число: ")))


def calculate_speed(distance, time):
    return distance / time

print(
    calculate_speed(distance=10, time=5)
)