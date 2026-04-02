#  1. Создаём список студентов по примеру из задания
students = [
{"name": "Harry", "grades": [82, 90, 78]},
{"name": "Hermione", "grades": [97, 90, 97]},
{"name": "Ron", "grades": [62, 70, 64]},
{"name": "Draco", "grades":[62, 75, 70]}
]


#  2. Создаём функцию, которая принимает список оценок и возвращает среднее значение.
def calculate_average(grades):
    average_grade = sum(grades) / len(grades)
    return average_grade


#  3. Логическое выражение-функция:
#  - проверяет средний балл, если он выше или равен 75, то студент "Успешен",
#  - выводит соответствующее сообщение.
def successful_student(average_grade):
    if average_grade < 75:
        print("Статус: Неуспешен")
    else:
        print("Статус: Успешен")


#  2. Напишем цикл, который пройдётся по каждому студенту и рассчитает его средний балл.
for student in students:
    grades = student["grades"]
    average_grade = calculate_average(grades)
#  4. Выведем для каждого студента сообщение формата, требуемого в задании
    print("\nСтудент: ", student["name"])
    print(f"Средний бал: {average_grade:.2f}")
    successful_student(average_grade)  #  Вывод сообщения об успешности


#  6. Рассчитаем общий средний балл по всем студентам и выведем его
def average_for_all(students):
    total_sum = 0
    total_count = 0
    average_grade_for_all = 0
    for student in students:
        grades = student["grades"]
        total_sum += sum(grades)  #  Добавляем сумму оценок студента к общей сумме оценок
        total_count += len(grades)  #  Добавляем количество оценок студента к общему количеству оценок
        average_grade_for_all = total_sum / total_count
    print(f"\nОбщий средний балл по всем студентам: {average_grade_for_all:.2f}")


average_for_all(students)  #  Выводим Средний балл по всем студентам


#  6.1. Добавим нового студента в список, используя метод append
def student_adding(new_studing):
    students.append(new_student)
    print("\nДобавлен студент: ", new_student["name"])
    average_for_all(students)  #  7. Пересчитываем и выводим Средний балл по всем студентам, т.к. обновился список студентов


new_student = {"name": "Dobby", "grades": [99, 99, 99, 90]}
student_adding(new_student)


#  6.2. Удалим студента с самым низким средним баллом из списка
def student_expulsion():
    student_to_remove = None  #  Инициализируем переменную (на всякий случай)
    min_avg = float('inf')  #  Число, большее, чем любой средний балл (для поиска минимума)
    for student in students:
        grades = student["grades"]
        average_grade = calculate_average(grades)
        if average_grade < min_avg:
            min_avg = average_grade
            student_to_remove = student
    print("\nОтчислен студент с минимальным средним баллом:", student_to_remove["name"])
    students.remove(student_to_remove)
    average_for_all(students)  #  7. Пересчитываем и выводим Средний балл по всем студентам, т.к. обновился список студентов