class Student:
    total=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.total+=1
    def display(self,phno,Branch):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"Branch: {Branch}")
        print(f"Phone: {phno}")
    @classmethod
    def total_students(cls):
        print(f"Total_Students: {cls.total}")
    #another classmethod#
    @classmethod
    def change(cls,n):
        cls.total=n
    ##static method##
    @staticmethod
    def just(name,age):
        print("Hii")
s1=Student("rama`", 21)
s2=Student("devi", 25)
s3=Student("bob", 30)
print(s1.display(1234567892,"CSE"))
print(s2.display(1234567892,"CSE"))
print(s3.display(1234567892,"CSE"))
Student.total_students()
Student.change(10)
Student.just("rama",21)


##QUESTION 1 ##
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        return self.marks>40
s1=Student("rama",70)
s2=Student("devi",35)
if s1.is_passed():
    print(s1.name,"passed")
else:
    print(s1.name,"failed")
if s2.is_passed():
    print(s2.name,"passed")
else:
    print(s2.name,"failed")


##QUESTION 2##
class Employee:
    company_name = "TechCorp"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
e1=Employee("rama")
e2=Employee("devi")
print(e1.company_name)
print(e2.company_name)
Employee.change_company("Delloitte")
print(e1.company_name)
print(e2.company_name)


## QUESTION 3 ##
class MathOps:
    @staticmethod
    def is_even(num):
        if num%2==0:
            return True
        else:
            return False
print(MathOps.is_even(19))
obj=MathOps()
print(obj.is_even(8))



## QUESTION 4 ##
class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display_specs(self):
        print("mileage:",self.mileage)
        print("wheels:",self.wheels)
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels=new_wheels
c1=Car(20)
c1.display_specs()
Car.change_wheels(6)
c1.display_specs()


## QUESTION 5 ##
class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius*9/5)+32
    def show_conversion(self):
        fahrenheit=Temperature.to_fahrenheit(self.celsius)
        print("Celsius:",self.celsius)
        print("Fahrenheit:",fahrenheit)
t1=Temperature(30)
t1.show_conversion()


## QUESTION 7 ##
class Employee:
    bonus_rate=0.1
    def __init__(self,name,salary):
        self.name=name
        self.base_salary=salary
    def final_salary(self):
        return self.base_salary+(self.base_salary*Employee.bonus_rate)
    @classmethod
    def update_bonus(cls,nb):
        cls.bonus_rate=nb
    @staticmethod
    def valid(sal):
        return sal > 0
e1=Employee("Rama", 50000)
e2=Employee("devi",10000)
print(e1.final_salary())
print(e2.final_salary())
e1.update_bonus(0.2)
print(e1.final_salary())
print(e2.final_salary())



## QUESTION 6 ##
class Book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        Book.total_books+=1
    @classmethod
    def from_string(cls,book_str):
        t,a=book_str.split("-")
        if cls.is_valid(t):
            return cls(t,a)
        else:
            return "Invalid book string"

    @staticmethod
    def is_valid(t):
        return len(t)>=3
bts="harry potter - J.K.Rowling"
b1=Book.from_string(bts)
# b1=Book("harry potter", "J.KRoeling")
b2=Book("The song of ice and fire", "R.R.Martin")
print(b1.title)
print(b1.author)
print(b2.title)
print(b2.author)


## QUESTION 8 ##
class Course:
    total_students=0
    def __init__(self,student_name):
        self.student_name=student_name
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print("total_students:",cls.total_students)
    @staticmethod
    def is_eligible(age):
        return age>=18
s1=Course("rama")
s2=Course("devi")
s3=Course("sita")
s1.enroll()
s2.enroll()
s3.enroll()
Course.show_total()
print(Course.is_eligible(18))
print(Course.is_eligible(17))


## QUESTION 9 ##
class BankAccount:
    bank_name="SBI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        if BankAccount.validate_amount(amount):
            self.balance+=amount
            print("Amount Depositd")
        else:
            print("Invalid Amount")
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def validate_amount(amount):
        return amount>0
a1=BankAccount("rama",5000)
a2=BankAccount("devi",2000)
a1.deposit(5000)
a2.deposit(2000)
BankAccount.change_bank_name("Union")
print(a1.holder,a1.balance,a1.bank_name)
print(a2.holder,a2.balance,a2.bank_name)



## QUESTION 10 ##
class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>Student.passing_marks:
            print(self.name,"passed")
        else:
            print(self.name,"failed")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if marks>=90:
            return 'A'
        elif marks>=75:
            return 'B'
        else:
            return 'C'
s1=Student("rama",75)
s2=Student("devi",91)
s3=Student("sri",40)
print(s1.name,"grade:",Student.grade_category(s1.marks))
print(s2.name,"grade:",Student.grade_category(s2.marks))
print(s3.name,"grade:",Student.grade_category(s3.marks))
s1.result()
s2.result()
s3.result()
Student.update_passing_marks(35)
s1.result()
s2.result()
s3.result()








