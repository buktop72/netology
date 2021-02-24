class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lection_grades:
                lecturer.lection_grades[course] += [grade]
            else:
                lecturer.lection_grades[course] = [grade]
        else:
            return 'Ошибка'

    def calc_average(self):
        y = 0
        for i in self.grades:
            y += (sum(self.grades[i]) / len(self.grades[i]))
        return (round(y / len(self.grades), 2))

    def __str__(self):
        self.average_score = self.calc_average()
        return (
            f"Имя: {self.name} \n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.average_score}\n"
            f"Курсы в процессе изучения: {self.courses_in_progress}\n"
            f"Завершенные курсы:{self.finished_courses} \n"

        )

    def __lt__(self, second):
        if not isinstance(second, Student):
            print(second.name, 'Не студент!')
        else:
            return self.calc_average() < second.calc_average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.lection_grades = {}

    def __str__(self):
        y = 0
        for i in self.lection_grades:
            y += (sum(self.lection_grades[i]) / len(self.lection_grades[i]))
        self.average_grades = round(y / len(self.lection_grades), 2)
        return (
            f"Имя: {self.name} \n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.average_grades} \n"
        )

    def calc_average(self):
        y = 0
        for i in self.lection_grades:
            y += (sum(self.lection_grades[i]) / len(self.lection_grades[i]))
        return (round(y / len(self.lection_grades), 2))

    def __lt__(self, second):
        if not isinstance(second, Lecturer):
            print(second.name, 'Не лектор!')
        else:
            return self.calc_average() < second.calc_average()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (
            f"Имя: {self.name} \n"
            f"Фамилия: {self.surname} \n"
        )


def course_average(ls, courses):
    x, y = 0, 0
    for i in ls:
        x += 1
        y += (sum(i.grades[courses]) / len(i.grades[courses]))
    print('Средний балл студентов курса ', courses, '-', round(y/x, 2))


def lecturer_rating(ls, courses):
    x, y = 0, 0
    for i in ls:
        x += 1
        y += (sum(i.lection_grades[courses]) / len(i.lection_grades[courses]))
    print('Средняя оценка студентами лекций курса ', courses, '-', round(y/x, 2))


student_1 = Student('Pavel', 'Popov', 'male')
student_2 = Student('Ira', 'Zotova', 'famale')
reviewer_1 = Reviewer('Ignat', 'Stepanovich')
reviewer_2 = Reviewer('Viktor', 'Viktorovich')
lecturer_1 = Lecturer('Ivan', 'Ivanovitsh')
lecturer_2 = Lecturer('Sergey', 'Petrovich')
lecturer_1.courses_attached = ['Python', 'Git']
lecturer_2.courses_attached = ['Python', 'Git']

student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses = ['Введение в программирование']
student_2.courses_in_progress += ['Python']
student_2.finished_courses = ['Введение в программирование', 'Git']

reviewer_1.courses_attached += ['Git', 'Python']
reviewer_2.courses_attached += ['Python', 'Git']

reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_1, 'Git', 3)
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_1, 'Git', 9)

reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Git', 10)
reviewer_1.rate_hw(student_2, 'Git', 7)
reviewer_1.rate_hw(student_2, 'Git', 9)

student_1.rate_lect(lecturer_1, 'Python', 9)
student_2.rate_lect(lecturer_1, 'Python', 10)
student_1.rate_lect(lecturer_1, 'Git', 8)
student_2.rate_lect(lecturer_1, 'Git', 9)
student_2.rate_lect(lecturer_1, 'Python', 9)
student_2.rate_lect(lecturer_1, 'Python', 9)

student_1.rate_lect(lecturer_1, 'Python', 9)
student_2.rate_lect(lecturer_2, 'Python', 5)
student_1.rate_lect(lecturer_2, 'Git', 8)
student_2.rate_lect(lecturer_2, 'Git', 9)
student_2.rate_lect(lecturer_2, 'Python', 7)
student_2.rate_lect(lecturer_2, 'Python', 6)
students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)
print(student_1 > student_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 > student_2)
course_average(students, 'Python')
lecturer_rating(lecturers, 'Python')
print('средний балл студента ', student_1.name,
      student_1.surname, '-', student_1.calc_average())
print('средний балл студента ', student_2.name,
      student_2.surname, '-', student_2.calc_average())
print('средний балл лектора ', lecturer_1.name,
      lecturer_1.surname, '-', lecturer_1.calc_average())
print('средний балл лектора ', lecturer_2.name,
      lecturer_2.surname, '-', lecturer_2.calc_average())
