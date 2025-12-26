class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        return f"Name is {self.name} and age {self.age}"
    
    @classmethod
    def from_string(cls, data_string):
        name, age = data_string.split(' ')
        return cls(name.strip(), int(age.strip()))
    
    
class Student(Person):
    school_name = "Koblenz International School"
    
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.__grade = grade
        
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, grade):
        if grade >= 0:
            self.__grade = grade
        else:
            print("Invalid grade")
                
    def info(self):
        return f"The name of the student is {self.name} and the age is {self.age}"
    
    def show_details(self):
        return self.info()


class Teacher(Person):
    school_name = "Koblenz International School"
    
    def info(self):
        return f"The name of the teacher is {self.name} and the age is {self.age}"
    
    def show_details(self):
        return self.info()
    
    @staticmethod
    def is_eligible(age):
        return age >= 25


class Course:
    def __init__(self, title):
        self.__title = title
        
    @property
    def course_title(self):
        return self.__title
    
    @course_title.setter
    def course_title(self, title):
        if isinstance(title, str) and title.strip():
            self.__title = title
        else:
            print("The title should be correct and not empty")


class Teacher_assistant(Student, Teacher):
    def role(self):
        return "I am a teaching assistant"


def check_role(obj):
    if isinstance(obj, Student):
        return "This is a student"
    elif isinstance(obj, Teacher):
        return "This is a teacher"


s1 = Student("waqar", 23, 67)
s2 = Student("khan", 25, 99)
teach = Teacher("latif", 29)
teach_assis = Teacher_assistant("talha", 30, 97)

s1.grade = 89
s2.grade = 99

print(s1.show_details())
print(teach.show_details())
print(isinstance(teach_assis, Student))
print(Teacher_assistant.mro())