class Student:
    def __init__(self, name, age, grade, ):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grade(self,):
        sum = 0
        for student in self.students:
            sum += student.get_grade()
        return sum/ len(self.students)



s1 = Student("Umesh", 21, 100)
s2 = Student("Akash", 22, 93)
s3 = Student("Jill", 21, 75)

course=Course("DME", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.get_avg_grade())