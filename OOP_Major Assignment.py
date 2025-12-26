class Person:  # base class representing a person
    def __init__(self, name, age):  # constructor stores name and age
        self.name = name  # instance attribute: name
        self.age = age  # instance attribute: age
        
    def info(self):  # returns a human-readable info string
        return f"Name is {self.name} and age {self.age}"  # formatted return
    
    @classmethod  # class method decorator for alternative constructors
    def from_string(cls, data_string):  # construct Person from "name age" string
        name, age = data_string.split(' ')  # split input into name and age parts
        return cls(name.strip(), int(age.strip()))  # return new Person instance
    
    
class Student(Person):  # Student inherits from Person
    school_name = "Koblenz International School"  # class variable for school name
    
    def __init__(self, name, age, grade):  # constructor adds a private grade
        super().__init__(name, age)  # initialize Person part
        self.__grade = grade  # private attribute for grade
        
    @property  # getter for grade
    def grade(self):
        return self.__grade  # return private grade value
    
    @grade.setter  # setter with simple validation
    def grade(self, grade):
        if grade >= 0:  # allow non-negative grades
            self.__grade = grade  # update private grade
        else:
            print("Invalid grade")  # print error for invalid values
                
    def info(self):  # override info to be student-specific
        return f"The name of the student is {self.name} and the age is {self.age}"  # formatted info
    
    def show_details(self):  # helper to return detailed info
        return self.info()  # reuse info()


class Teacher(Person):  # Teacher inherits from Person
    school_name = "Koblenz International School"  # class variable for school name
    
    def info(self):  # teacher-specific info string
        return f"The name of the teacher is {self.name} and the age is {self.age}"  # formatted info
    
    def show_details(self):  # helper returning teacher info
        return self.info()  # reuse info()
    
    @staticmethod  # static method does not use self or cls
    def is_eligible(age):  # eligibility check for teachers
        return age >= 25  # True if age is at least 25


class Course:  # Course class demonstrating property decorators
    def __init__(self, title):  # constructor storing a private title
        self.__title = title  # private attribute for course title
        
    @property  # getter for course_title
    def course_title(self):
        return self.__title  # return the private title
    
    @course_title.setter  # setter with validation
    def course_title(self, title):
        if isinstance(title, str) and title.strip():  # ensure non-empty string
            self.__title = title  # set new title
        else:
            print("The title should be correct and not empty")  # validation message


class Teacher_assistant(Student, Teacher):  # example of multiple inheritance
    def role(self):  # method describing role
        return "I am a teaching assistant"  # role string


def check_role(obj):  # helper function (module-level) to identify role
    if isinstance(obj, Student):  # check if object is Student or subclass
        return "This is a student"  # return identification
    elif isinstance(obj, Teacher):  # check if object is Teacher or subclass
        return "This is a teacher"  # return identification


s1 = Student("waqar", 23, 67)  # example Student instance
s2 = Student("khan", 25, 99)  # another Student instance
teach = Teacher("latif", 29)  # example Teacher instance
teach_assis = Teacher_assistant("talha", 30, 97)  # teaching assistant instance

s1.grade = 89  # update s1's grade using setter
s2.grade = 99  # update s2's grade using setter

print(s1.show_details())  # print student details to stdout
print(teach.show_details())  # print teacher details to stdout
print(isinstance(teach_assis, Student))  # demonstrate isinstance with TA
print(Teacher_assistant.mro())  # print method resolution order for the TA class