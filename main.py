class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, department, name, age):
        self.department = department
        super().__init__(name, age)

class Sports:
    def conduct_sports(self, sportsname):
        self.sportsname = sportsname
        print(f"Conducting {sportsname} sports.")

class SportsTeacher(Teacher, Sports):
    def __init__(self, department, name, age, sport):
        self.sport = sport
        super().__init__(department, name, age)

    def display_sport(self):
        print(f"Sport: {self.sport}")

class Principal(Teacher):
    def displayinfo(self):
        print(f"Principal Info - Name: {self.name}, Age: {self.age}, Department: {self.department}")
        
    def manage_school(self):
        print("Managing School")

person1 = Person("John", 30)
teacher1 = Teacher("Mathematics", "Alice", 40)
sports_teacher1 = SportsTeacher("Physical Education", "Bob", 35, "Football")
principal1 = Principal("Science", "Dr. Smith", 50)
print(f"Person - Name: {person1.name}, Age: {person1.age}")
print(f"Teacher - Name: {teacher1.name}, Age: {teacher1.age}, Department: {teacher1.department}")
sports_teacher1.conduct_sports("Football")
sports_teacher1.display_sport()
principal1.displayinfo()
principal1.manage_school()