students = [
    ["Давид", [4, 4, 4]],
    ["Дима", [5, 5, 5]],
    ["Света", [3, 4, 4]],
    ["Сергей", [5, 5, 4]],
    ["Таня", [5, 4, 5]],
    ["Савелий", [5, 5, 4]],
    ["Руслан", [5, 4, 4]],
    ["Артур", [4, 4, 4]],
    ["Данила", [4, 3, 3]]
]

sum_grade = 0

def calculate_average(grades):
    return sum(grades) / 3

for student in students:
    name, grades = student
    average = calculate_average(grades)
    print(f"{name}  |  {average:.2f}")
    print("-------------------")



def find_best_and_worst_students(students):
    best_student = None
    worst_student = None
    best_average = 0
    worst_average = float('inf')

    for student in students:
        name, grades = student
        average = calculate_average(grades)

        if average > best_average:
            best_average = average
            best_student = name

        if average < worst_average:
            worst_average = average
            worst_student = name

    print(f"\nЛучший студент: {best_student} с средней оценкой {best_average:.2f}")
    print(f"Худший студент: {worst_student} с средней оценкой {worst_average:.2f}")

find_best_and_worst_students(students)