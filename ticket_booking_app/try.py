# Define a class representing a Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Define a subclass Student inheriting from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        return f"{self.name} is studying {subject}."

# Define another subclass Teacher inheriting from Person
class Teacher(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def teach(self, subject):
        return f"{self.name} is teaching {subject}."

# Create instances of Person, Student, and Teacher classes
person1 = Person("Alice", 30)
student1 = Student("Bob", 20, "S1234")
teacher1 = Teacher("Carol", 40, "Mathematics")

# Demonstrate encapsulation
print(person1.name)  # Accessing public attribute directly
# print(person1.__age)  # This would raise an AttributeError because __age is a private attribute

# Demonstrate polymorphism
print(person1.greet())
print(student1.greet())  # Inherited method overridden in Student class

# Demonstrate inheritance
print(student1.study("Python"))  # Method from Student class
print(teacher1.teach("Algebra"))  # Method from Teacher class
