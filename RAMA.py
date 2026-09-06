                                            ## METHODS--CLASSES AND OBJECTS ##

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def is_passed(self):
#         return self.marks>40
#         # if self.marks>40:
#         #     return True
#         # else:
#         #     return False
# s1=Student("ram",80)
# s2=Student("Neela",39)
# if s1.is_passed():
#     print(s1.name,"passed")
# else:
#     print(s1.name,"failed")
# if s2.is_passed():
#     print(s2.name,"passed")
# else:
#     print(s2.name,"failed")



# class Employee:
#     company_name="TechCorp"
#     def __init__(self,name):
#         self.name=name
#     @classmethod
#     def change_name(cls,new_name):
#         cls.company_name=new_name
# e1=Employee("ram")
# e2=Employee("sri")
# e3=Employee("jai")
# print(f"1.{e1.name}-",e1.company_name)
# print(f"2.{e2.name}-",e2.company_name)
# Employee.change_name("Deloitte")
# print(e1.company_name)
# print(e2.company_name)



# class MathOps:
#     @staticmethod
#     def is_even(num):
#         if num%2==0:
#             return True
#         else:
#             return False
# print(MathOps.is_even(18))
# obj=MathOps()
# print(obj.is_even(13))

#             print("even")
#         else:
#             print("odd")
# obj=MathOps()
# obj.is_even(13)



# class Car:
#     wheels=4
#     def __init__(self,mileage):
#         self.mileage=mileage
#     def display_specs(self):
#         print("mileage:",self.mileage)
#         print("wheels:", self.wheels)
#     @classmethod
#     def change_wls(cls, new_wls):
#         cls.wheels = new_wls
# c = Car(25)
# c.display_specs()
# Car.change_wls(8)
# c.display_specs()




# class Temperature:
#         def __init__(self, Celsius):
#             self.Celsius = Celsius
#
#         @staticmethod
#         def to_fahrenheit(Celsius):
#             return (Celsius * 9 / 5) + 32
#
#         def show_conversion(self):
#             Fahrenheit = Temperature.to_fahrenheit(self.Celsius)
#             print("Celsius: ", self.Celsius)
#             print("Fahrenheit: ", Fahrenheit)
#
# t = Temperature(43)
# t.show_conversion()



# class Book:
#     total_books = 0
#
#     def __init__(self, title, author, ):
#         self.title = title
#         self.author = author
#         Book.total_books += 1
#
#     @classmethod
#     def from_string(cls, book_str):
#         t, a = book_str.split("-")
#         if cls.is_valid(t):
#             return cls(t, a)
#         else:
#             return "invalid book str"
#
#     @staticmethod
#     def is_valid(t):
#         return len(t) >= 3
#
# bts = "abc-gef"
# # b1=Book.from_string(bts)
# b1 = Book("deg", 'ijk')
# b2 = Book("xyz", 'abc')
# print(b1.title)
# print(b1.author)
# print(b2.title)
# print(b2.author)



# class Employee:
#     bonus_rate=0.1
#     def __init__(self,name,base_salary):
#         self.name=name
#         self.base_salary=base_salary
#     def final_salary(self):
#         return self.base_salary+(self.base_salary*Employee.bonus_rate)
#     @classmethod
#     def update_bonus(cls,new_rate):
#         cls.bonus_rate=new_rate
#     @staticmethod
#     def is_valid(sal):
#         return sal>0
# e1=Employee("ram",30000)
# e2=Employee("dev",40000)
# print(e1.final_salary())
# print(e2.final_salary())
# Employee.update_bonus(0.5)
# print(e1.final_salary())
# print(e2.final_salary())



# class Course:
#     total_students=0
#     def __init__(self,stu_name):
#         self.stu_name=stu_name
#     def enroll(self):
#         Course.total_students+=1
#     @classmethod
#     def show_total(cls):
#         print("total students:",cls.total_students)
#     @staticmethod
#     def is_eligible(age):
#         return age>=18
# c1=Course("ram")
# c2=Course("dev")
# c1.enroll()
# c2.enroll()
# Course.show_total()
# print(Course.is_eligible(18))
# print(Course.is_eligible(17))



# class BankAccount:
#     bank_name="Union"
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         if BankAccount.validate_amount(amount):
#             self.balance=self.balance+amount
#             print("Deposited")
#         else:
#             print("Invalid")
#     @classmethod
#     def change_bank_name(cls,new_name):
#         cls.bank_name=new_name
#     @staticmethod
#     def validate_amount(amount):
#         return amount>0
# a1=BankAccount("ram",15000)
# a2=BankAccount("Devi",8000)
# a1.deposit(3000)
# a2.deposit(2500)
# print(a1.name,a1.balance,a1.bank_name)
# print(a2.name,a2.balance,a2.bank_name)
# BankAccount.change_bank_name("SBI")
# print(a1.name,a1.balance,a1.bank_name)
# print(a2.name,a2.balance,a2.bank_name)





# class Student:
#     passing_marks=40
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def result(self):
#         if self.marks>=Student.passing_marks:
#             print(self.name,"pass")
#         else:
#             print(self.name,"fail")
#     @classmethod
#     def update_passing_marks(cls,new_marks):
#         cls.passing_marks=new_marks
#     @staticmethod
#     def grade_category(marks):
#         if marks>=90:
#             return "A"
#         elif marks>=60:
#             return "B"
#         else:
#             return "C"
# s1=Student("ram",80)
# s2=Student("Neela",55)
# s3=Student("Devi",35)
# print(s1.name, "- grade:",Student.grade_category(s1.marks))
# s1.result()
# print(s2.name, "- Grade:",Student.grade_category(s2.marks))
# s2.result()
# Student.update_passing_marks(60)
# print(s1.name, "- grade:",Student.grade_category(s1.marks))
# s1.result()
# print(s2.name, "- Grade:",Student.grade_category(s2.marks))
# s2.result()



                                                    ## METHODS - PDF 2##


class Student:
    total_students=0
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.total_students+=1
    def result(self):
        if self.marks>=Student.passing_marks:
            return "pass"
        else:
            return "fail"
    @classmethod
    def curve_marks(cls,percentage):
        cls.curve=percentage
    def apply_curve(self):
        self.marks=self.marks+(self.marks*Student.curve/100)
    @staticmethod
    def grade(marks):
        if marks>=90:
            return "A"
        elif marks>=75:
            return "B"
        elif marks>=50:
            return "C"
        elif marks>=40:
            return "D"
        else:
            return "E"
s1=Student("ram",75)
s2=Student("sri",80)
s3=Student("jai",45)
s4=Student("jam",35)
Student.curve_marks(10)
s1.apply_curve()
s2.apply_curve()
s3.apply_curve()
s4.apply_curve()
print("Total Students: ",Student.total_students)
print(s1.name,s1.marks,s1.result(),Student.grade(s1.marks))
print(s2.name,s2.marks,s2.result(),Student.grade(s2.marks))
print(s3.name,s3.marks,s3.result(),Student.grade(s3.marks))
print(s4.name,s4.marks,s4.result(),Student.grade(s4.marks))






















































                                                                ## INHERITANCE BASIC QNS ##


# class Animal:
#     def sound(self):
#         print("Animal sounds")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# a=Animal()
# d=Dog()
# d.sound()
# a.sound()


# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         super().show()
#         print("B")
# b=B()
# b.show()


# class A:
#     def display(self):
#         print(" A class")
# class B(A):
#     def display(self):
#         print("B class")
# class C(B):
#     def display(self):
#         print("C class")
# c=C()
# c.display()


# class Vehicle:
#     def wheels(self):
#         print("Vehicle have wheels")
# class Car(Vehicle):
#     def wheels(self):
#         print("Car has 4 wheels")
# class Bike(Vehicle):
#     def wheels(self):
#         print("Bike has 2 wheels")
# b=Bike()
# c=Car()
# b.wheels()
# c.wheels()



# class Employee:
#     def salary(self):
#         print("emp salary:20000")
# class Manager(Employee):
#     def salary(self):
#         print("manager salary:30000")
#         print("incentive:10000")
# e=Employee()
# m=Manager()
# e.salary()
# m.salary()



# class University:
#     university="mvr"
#     @classmethod
#     def show(cls):
#         print(cls.university)
# class College(University):
#     pass
# c=College()
# c.show()
# print(c.university)


# class MathOps:
#     @staticmethod
#     def add(a,b):
#         return a+b
# class AdvancedOps(MathOps):
#     pass
# print(AdvancedOps.add(10,20))



# class Father:
#     def skills(self):
#         print("father skills")
# class Mother:
#     def skills(self):
#         print("mother skills")
# class Child(Father,Mother):
#     pass
# c=Child()
# c.skills()
# print(Child.mro())



# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def area(self):
#         l=10
#         b=20
#         print("AREA: ",l*b)
# r=Rectangle()
# r.area()



# class Person:
#     def __init__(self,name):
#         self.name=name
# class Student(Person):
#     def __init__(self,name,roll):
#         super().__init__(name)
#         self.roll=roll
# s=Student("Neela",71)
# print("name:", s.name)
# print("roll:", s.roll)


































































































































































































































































































