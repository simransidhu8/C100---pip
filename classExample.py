class Student:
    def __init__(self, name, age, gender, level, grades = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {} 
    
    def setGrade(self, course, grade):
        self.grades[course] = grade
    
    def getGrade(self, course):
        return self.grades[course]

    def getGpa(self) :
        return sum(self.grades.values())/len(self.grades)
    
# define some students
simran = Student("Simran", 13, "female", 8, {"Math": 9, "Science": 7.8})
john = Student("John", 13, "Male", 8, {"Math": 7.5, "Science": 8})

# reading gpa's of students
print(simran.getGpa())
print(john.getGpa())