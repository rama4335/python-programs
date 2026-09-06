#even nums#
# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     if i%2==0:
#         print(i,end=" ")
from mimetypes import init
from time import process_time


# n=7
# if n%2==1:
#     print("odd")
# else:
#     print("even")


# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     if i%2==1:
#         print(i,end=" ")

#sum of even nums#
# a=int(input())
# b=int(input())
# sum=0
# for i in range(a,b+1):
#     if i%2==1:
#         sum=sum+i
# print(sum)


# avg of even nums#
# a=int(input())
# b=int(input())
# sum=0
# c=0
# for i in range(a,b+1):
#     if i%2==0:
#         sum=sum+i
#         c=c+1
#         avg=sum/c
# print(avg)


# a=1           #alternative even nums#
# b=25
# if a%2==1:
#     a+=1
# c=0
# for i in range(a,b+1):
#     if i%2==0:
#         c=c+1
#         if c%2==1:
#             print(i)



# a=int(input())
# b=int(input())
# if a%2==1:
#     a+=1
# c=0
# for i in range(a,b+1):
#     if i%2==0:
#         c=c+1
#         if c%2==0:
#             print(i)



# a=int(input())        #sum of alternative even nums#
# b=int(input())
# c=0
# sum=0
# for i in range(a,b+1):
#     if i%2==0:
#         c+=1
#         if c%2==1:
#             sum=sum+i
# print(sum)



# a=int(input())        #avg of alternative even nums#
# b=int(input())
# c=0
# sum=0
# count=0
# for i in range(a,b+1):
#     if i%2==0:
#         c+=1
#         if c%2==1:
#             sum=sum+i
#             count=count+1
# print(sum/count)


# def odd(n):
#     for i in range(1,n+1,2):
#         yield i
# x=odd(10)
# for i in x:
#     print(i)


# def primes(n):
#     for i in range(2,n+1):
#         fc=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 fc=fc+1
#         if fc==2:
#             yield i
# x=primes(20)
# for i in x:
#     print(i)



# def nums(n):
#     for i in range(1,n+1):
#         if i%5==0:
#             yield i
# x=nums(20)
# for i in x:
#     print(i)
#
#
# def posit(l):
#     for i in l:
#         if i>0:
#             yield i
# x=posit([1,2,-4,-5,8,5])
# for i in x:
#     print(i)


# def fun():
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     print(a+b)
# fun()

# def add(a,b):
#     return a+b
# x=add(10,20)
# print(x)


# def fun(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# fun(19)


# def fun(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             print(i)
# fun(10)


# def fun(a,b):
#     for i in range(a,b+1):
#         fc=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 fc=fc+1
#         if fc==2:
#             print(i)
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# fun(a,b)
# # fun(1,20)


# n=5
# num=2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num=num+2
#     print()
#

# def fun(n,num):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(num,end=" ")
#             num=num+2
#         print()
# n=int(input("enter number"))
# num=int(input("enter number"))
# fun(n,num)
# fun(5,2)

# l=[10,20,30,40,50,50,50,90]
# x=max(l)
# print(x)


# def maximum(l):
#     l=list(set(l))
#     l.sort()
#     print(l[-3])
# l=[10,20,30,40,90,90,]
# maximum(l)


# def fun(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# x=fun(6)
# y=fun(5)
# print(x)
# print(x+y)


# def fun(n):
#     sum=0
#     while n>0:
#         r=n%10
#         sum+=r
#         n=n//10
#     return sum
# n=int(input("enter a number"))
# # x=fun(12345)
# print(fun(n))


# n=121
# rev=0
# t=n
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# if rev==t:
#     print("palindrome")
# else:
#     print("not")


# def fun(n):
#     rev=0
#     t=n
#     while n>0:
#         r=n%10
#         rev=rev*10+r
#         n=n//10
#     if t==rev:
#         print("palindrome")
#     else:
#         print("not")
# fun(100)

# def fun(n):
#     for i in range(1,n+1):
#         t=i
#         rev=0
#         while i>0:
#             r=i%10
#             rev=rev*10+r
#             i=i//10
#         if rev==t:
#             # return t
#             print(t)
# fun(50)



# def fun(n):
#     arm=0
#     dc=0
#     t=n
#     while n>0:
#         dc=dc+1
#         n=n//10
#     n=t
#     while n>0:
#         r=n%10
#         arm=arm+(r**dc)
#         n=n//10
#     if arm==t:
#         print("armstrong")
#     else:
#         print("not armstrong")
# fun(154)


# def fun(n):
#     sum=0
#     while n>0:
#         r=n%10
#         sum=sum+r
#         n=n//10
#     return sum
# n=int(input("enter a number"))
# print(fun(n))

# def fun(n):
#     rev=0
#     while n>0:
#         r=n%10
#         rev=rev*10+r
#         n=n//10
#     return rev
# print(fun(675))
#     print(rev)
# fun(153)


# def fun(n):
#     c=0
#     while n>0:
#         c=c+1
#         n=n//10
#     print(c)
# fun(5379298)


# def outer():
#     print("hello")
#     def inner(a,b):
#         print(a+b)
#     inner(10,10)
# outer()


# def shopping(item):
#     print("shopping item:",item)
#     def item_details(colour,price):
#         print("colour:",colour)
#         print("price:",price)
#     item_details('green',500)
# shopping('shirt')
#
#
# def outer(n):
#     def inner():
#         return n*n
#     print(inner())
# outer(5)



# l=[10,20,30,40]
# for i in l:
#     print(i)
# i=iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# def fun(l):
#     i=iter(l)
#     print(next(i))
#     print(next(i))
#     print(next(i))
# fun([10,20,30])


# def fun(l):
#     i=iter(l)
#     while True:
#         try:
#             print(next(i))
#         except StopIteration:
#             break
# fun([20,40,10,40,33,5,66,54,24,24])

# class Iterator:
#     def __init__(self):
#         self.n=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n==1:
#             self.n+=1
#         elif self.n<=10:
#             x=self.n
#             self.n=self.n+2
#             return x
#         # elif self.n==1:
#         #     self.n=self.n+1
#         else:
#
#             raise StopIteration
# obj=Iterator()
# for i in obj:
#     print(i)


# def fun(n):
#     for i in range(1,n+1):
#         yield i
# for i in fun(5):
#     print(i)


# def fun(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             yield i
# for i in fun(10):
#     print(i)


# def fun(a,b):
#     for i in range(a,b+1):
#         fc=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 fc=fc+1
#         if fc==2:
#             yield i
# for i in fun(10,20):
#     print(i)

# def fun(n):
#         fc=0
#         for i in range(1,n+1):
#             if n%i==0:
#                 fc=fc+1
#         if fc==2:
#             yield "prime"
#         else:
#             yield "not prime"
# n=int(input("enter a number"))
# for i in fun(n):
#     print(i)

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return self.name+" "+str(self.age)
# s=Student("rama",21)
# print(s)


# class Students:
#     def __init__(self,names):
#         self.names=names
#     def __len__(self):
#         return len(self.names)
# s=Students(["ram", "dev", "Sita","leela"])
# print(len(s))

# class Add:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,other):
#         return self.a+other.b
# c=Add(10,20)
# d=Add(20,20)
# print(c+d)

# class Num:
#     def __init__(self,n):
#         self.n=n
#     def __mul__(self, other):
#         return self.n*other.n
# a=Num(10)
# b=Num(50)
# print(a*b)


# class Eq:
#     def __init__(self,marks):
#         self.marks=marks
#     def __eq__(self, other):
#         return self.marks==other.marks
# a=Eq(75)
# b=Eq(75)
# print(a==b)


# class Eq:
#     def __init__(self,marks):
#         self.marks=marks
#     def __gt__(self, other):
#         return self.marks>other.marks
# a=Eq(90)
# b=Eq(87)
# print(a>b)

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def __str__(self):
#         return self.name+" "+str(self.marks)
#     def __gt__(self, other):
#         return self.marks>other.marks
# s1=Student("rama",90)
# s2=Student("Devi",85)
# print(s1)
# print(s1>s2)


# class Parent:
#     def display(self):
#         print("this is parent")
# class Child(Parent):
#     def show(self):
#         print("this is child")
# c=Child()
# c.show()
# c.display()

#
# class Parent:
#     def __init__(self):
#         self.a=10
# class Child(Parent):
#     def show(self):
#         print(self.a)
# c=Child()
# c.show()


# class Animal:
#     def eats(self):
#         print("animal eats")
# class Dog(Animal):
#     def barks(self):
#         print("dog barks")
# d=Dog()
# d.eats()
# d.barks()


# class Parent:
#     def __init__(self):
#         self.a=10
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.b=20
# c=Child()
# print(c.b)
# print(c.a)


# class Parent:
#
#     def show(self):
#         print("Parent")
# class Child(Parent):
#
#     def show(self):
#         super().show()
#         print("Child")
# c = Child()
# c.show()

# class Employee:
#     def __init__(self,name,sal):
#         self.name=name
#         self.sal=sal
#     def display(self):
#         print("name:",self.name)
#         print("salary:",self.sal)
# class Manager(Employee):
#     def display(self):
#         super().display()
#         print("manager manages the team")
# m=Manager("rama",40000)
# m.display()


# class Animal:
#     def eat(self):
#         print("animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("dog is barking")
# d=Dog()
# d.eat()
# d.bark()


# class Vehicle:
#     def start(self):
#         print("vehicle started")
# class Car(Vehicle):
#     def drive(self):
#         print("car is driving")
# c=Car()
# c.start()
# c.drive()


# class BankAccount:
#     def __init__(self,holder,balance):
#         self.holder=holder
#         self.balance=balance
#     def display(self):
#         print("name:",self.holder)
#         print("bal:",self.balance)
# class SavingsAccount(BankAccount):
#     def __init__(self,holder,balance,interest_rate):
#         super().__init__(holder,balance)
#         self.interest_rate=interest_rate
#     def display(self):
#         super().display()
#         print("interest_rate:",self.interest_rate)
# s=SavingsAccount("neela",10000,2)
# s.display()




# class Bank:
#     def __init__(self,balance,deposit,withdraw):
#         self.balance=balance
#         self.deposit=deposit
#         self.withdraw=withdraw
#     def display(self):
#         print("balance:",self.balance)
#         print("deposit:",self.deposit)
#         print("total_bal:",self.balance+self.deposit)
#         print("withdraw:",self.withdraw)
#         print("check_balance:",(self.balance+self.deposit)-self.withdraw)
# class User(Bank):
#     # def __init__(self,balance,deposit,withdraw,check_bal,name):
#     #     super().__init__(balance,deposit,withdraw)
#     def show(self,name):
#         self.name=name
#         print("name:",self.name)
# a=User(10000,2000,600)
# a.display()
# a.show("neela")

                                            ##INHERITANCE##
# class Bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#     def withdraw(self,amount):
#         self.balance=self.balance-amount
#     def check_balance(self):
#         print("balance:",self.balance)
# class User(Bank):
#     def __init__(self,balance,name):
#         super().__init__(balance)
#         self.name=name
#     def show(self):
#         print("name:",self.name)
# u=User(10000,'neela')
# u.show()
# u.deposit(5000)
# u.withdraw(700)
# u.check_balance()


# class Employee:
#     def __init__(self,emp_name,salary):
#         self.emp_name=emp_name
#         self.salary=salary
#     def display_details(self):
#         print("emp_name:",self.emp_name)
#         print("salary:",self.salary)
# class Manager(Employee):
#     def __init__(self,emp_name,salary,extra):
#         super().__init__(emp_name,salary)
#         self.extra=extra
#     def bonus(self):
#         print("bonus:",self.extra)
#         print("total salary:",self.salary+self.extra)
# m=Manager("rama",50000,8000)
# m.display_details()
# m.bonus()



# class Emp:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display_details(self):
#         print("name:",self.name)
#         print("salary:",self.salary)
# class Manager(Emp):
#     def __init__(self,name,salary,extra):
#         super().__init__(name,salary)
#         self.extra=extra
#     def bonus(self):
#         print("bonus:",self.extra)
#         print("total_salary=",self.salary+self.extra)
# m=Manager('rama',40000,2000)
# m.display_details()
# m.bonus()



# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display_marks(self):
#         print("name:",self.name)
#         print("marks:",self.marks)
# class Result(Student):
#     def result(self):
#         if self.marks>=50:
#             print("passed")
#         else:
#             print("failed")
# name=input("enter a name:")
# marks=int(input("enter your marks:"))
# r=Result(name,marks)
# # r=Result("rama",75)
# r.display_marks()
# r.result()

                                    ##MULTILEVEL##

# class Restaurant:
#     def menu(self,item):
#         prices={
#             "biryani": 150,
#             "pizza": 100,
#             "chicken biryani": 250,
#             "burger": 80,
#             "milkshakes": 100
#         }
#         return prices.get(item,0)
# class FoodCourt(Restaurant):
#     def display_menu(self):
#         print("Available food items:")
#         print("biryani - 150")
#         print("pizza - 100")
#         print("chicken biryani - 250")
#         print("burger - 80")
#         print("milkshakes - 100")
#     def order(self):
#         self.total=0
#         while True:
#             item=input("enter food item: ").lower()
#
#             price=self.menu(item)
#             if price==0:
#                 print("item not available")
#             else:
#                 self.total+=price
#                 print("added :",item,price)
#             choice=input("do you want to order more? (yes/no):").lower()
#             if choice=="no":
#                 break
#         self.billing()
#     def billing(self):
#         print("food bill:",self.total)
#         print("packing charge: 20")
#         print("Total bill: ",self.total+20)
# class Customer(FoodCourt):
#     pass
#
# c=Customer()
# c.order()



# class Movie:
#     def ticket(self,movie):
#         prices={
#             "pushpa": 100,
#             "madhi": 150,
#             "bhahubali": 200,
#             "dc": 250,
#             "rrr": 200,
#             "salaar": 180
#
#         }
#         return prices.get(movie,0)
# class Booking(Movie):
#     def movies(self):
#         print("Available movies:")
#         print("Pushpa - 100")
#         print("Madhi - 150")
#         print("Bhahubali - 200")
#         print("DC - 250")
#         print("RRR - 200")
#         print("Salaar - 180")
#     def selection(self):
#         self.total=0
#         while True:
#             movie=input("Enter movie name:").lower()
#             price=self.ticket(movie)
#             if price==0:
#                 print("not available")
#             else:
#                 self.total+=price
#                 print("Ticket booked:",movie,price)
#             choice=input("do you want to book more tickets? (yes/no)").lower()
#             if choice=='no':
#                 break
#         self.billing()
#     def billing(self):
#         print("ticket price:",self.total)
#         print("booking charge : 30")
#         print("Total amount:",self.total+30)
# class Customer(Booking):
#     pass
# c=Customer()
# c.movies()
# c.selection()


# class Course:
#     def fees(self,course):
#         fee={
#             "python": 25000,
#             "java": 30000,
#             "data analytics": 35000,
#             "aiml": 40000
#         }
#         return fee.get(course,0)
# class Academy(Course):
#     def courses(self):
#         print("Available courses :")
#         print("Python: 25000")
#         print("Java: 30000")
#         print("Data analytics: 35000")
#         print("AIML: 40000")
#     def enroll(self):
#         self.total=0
#         while True:
#             course=input("choose your course:").lower()
#             fees=self.fees(course)
#             if fees==0:
#                 print("not available")
#             else:
#                 self.total+=fees
#                 print("course choosed",course,fees)
#             choice=input("do you want choose more courses? (yes/no)").lower()
#             if choice=='no':
#                 break
#         self.billing()
#     def billing(self):
#         print("course fee:",self.total)
#         print("registration fee : 100")
#         print("Total fee:",self.total+100)
# class Student(Academy):
#     pass
# s=Student()
# s.enroll()


                                        ##HIERARCHICAL##

# class Cab:
#     def bike(self,distance):
#         return distance * 10
#     def auto(self,distance):
#         return distance * 15
#     def car(self,distance):
#         return distance * 20
# class Uber(Cab):
#     def menu(self):
#         print("Uber:")
#         print("1. bike - 10rs/km")
#         print("2. auto - 15rs/km")
#         print("3. car - 20rs/km")
#     def booking(self):
#         self.menu()
#         choice=input("enter ride type:").lower()
#         distance=int(input("enter distance in km:"))
#         if choice=="bike":
#             self.total=self.bike(distance)
#         elif choice=="auto":
#             self.total=self.auto(distance)
#         elif choice=="car":
#             self.total=self.car(distance)
#         else:
#             print("Invalid ride")
#             return
#         self.billing()
#     def billing(self):
#         gst=self.total *10/100
#         amount=self.total+gst
#         if amount >1000:
#             discount=amount * 15/100
#         else:
#             discount=0
#         final_amount=amount-discount
#         print("fare:",self.total)
#         print("gst:",gst)
#         print("discount:",discount)
#         print("Final bill:",final_amount)
# class Ola(Cab):
#     def menu(self):
#         print("Ola:")
#         print("1. bike - 10rs/km")
#         print("2. auto - 15rs/km")
#         print("3. car - 20rs/km")
#     def booking(self):
#         self.menu()
#         choice = input("enter ride type:").lower()
#         distance = int(input("enter distance in km:"))
#         if choice == "bike":
#             self.total = self.bike(distance)
#         elif choice == "auto":
#             self.total = self.auto(distance)
#         elif choice == "car":
#             self.total = self.car(distance)
#         else:
#             print("Invalid ride")
#             return
#         self.billing()
#     def billing(self):
#         gst = self.total * 12 / 100
#         amount = self.total + gst
#         if amount > 1500:
#             discount = amount * 20 / 100
#         else:
#             discount = 0
#         final_amount = amount - discount
#         print("fare:", self.total)
#         print("gst:", gst)
#         print("discount:", discount)
#         print("Final bill:", final_amount)
# choice=input("choose Uber or Ola:").lower()
# if choice=="uber":
#     u=Uber()
#     u.booking()
# elif choice=="ola":
#     o=Ola()
#     o.booking()
# else:
#     print("Invalid choice")



# class Grocery:
#     def rice(self,quantity):
#         return quantity * 60
#     def sugar(self,quantity):
#         return quantity * 50
#     def oil(self,quantity):
#         return quantity * 100
# class Dmart(Grocery):
#     def items(self):
#         print("Available items")
#         print("Rice - 60rs/kg")
#         print("Sugar - 50rs/kg")
#         print("oil - 100rs/kg")
#     def shopping(self):
#         self.items()
#         choice=input("Enter your item:").lower()
#         quantity=int(input("Enter quantity in kg"))
#         if choice=='rice':
#             self.total=self.rice(quantity)
#         elif choice=="sugar":
#             self.total=self.sugar(quantity)
#         elif choice=="oil":
#             self.total=self.oil(quantity)
#         else:
#             print("Item not available")
#             return
#         self.billing()
#     def billing(self):
#         gst=self.total * 5/100
#         amount=self.total+gst
#         if amount>2000:
#             discount=amount * 10/100
#         else:
#             discount=0
#         final_amount=amount-discount
#         print("price:",self.total)
#         print("gst:",gst)
#         print("discount:",discount)
#         print("final bill:",final_amount)
# class RelianceSmart(Grocery):
#     def items(self):
#         print("Available items")
#         print("Rice - 60rs/kg")
#         print("Sugar - 50rs/kg")
#         print("oil - 100rs/kg")
#     def shopping(self):
#         self.items()
#         choice=input("Enter your item:").lower()
#         quantity=int(input("Enter quantity in kg:"))
#         if choice=='rice':
#             self.total=self.rice(quantity)
#         elif choice=="sugar":
#             self.total=self.sugar(quantity)
#         elif choice=="oil":
#             self.total=self.oil(quantity)
#         else:
#             print("Item not available")
#             return
#         self.billing()
#
#     def billing(self):
#         gst = self.total * 5 / 100
#         amount = self.total + gst
#         if amount > 2500:
#             discount = amount * 15 / 100
#         else:
#             discount = 0
#         final_amount = amount - discount
#         print("price:", self.total)
#         print("gst:", gst)
#         print("discount:", discount)
#         print("final bill:", final_amount)
# choice=input("Choose the Supermarket: ")
# if choice=="Dmart":
#     d=Dmart()
#     d.shopping()
# elif choice=="RelianceSmart":
#     s=RelianceSmart()
#     s.shopping()
# else:
#     print("Invalid market")





# class Bus:
#     def sleeper(self):
#         return 800
#     def semi_sleeper(self):
#         return 600
#     def ac(self):
#         return 1000
# class RedBus(Bus):
#     def routes(self):
#         print("Available routes")
#         print("Hyd to Vij")
#         print("Hyd to Bangalore")
#         print("Vij to Chennai")
#         print("Vij to Madhurai")
#     def booking(self):
#         self.routes()
#         route = input("Enter route: ").lower()
#
#         if route == "hyd to vij":
#             print("Route selected:", route)
#         elif route == "hyd to bangalore":
#             print("Route selected:", route)
#         elif route == "vij to chennai":
#             print("Route selected:", route)
#         elif route=="vij to madhurai":
#             print("route selected:",route)
#         else:
#             print("Route not available")
#             return
#
#         bus=input("Enter bus type: ").lower()
#
#         if bus=="sleeper":
#             self.total=self.sleeper()
#         elif bus=="semi_sleeper":
#             self.total=self.semi_sleeper()
#         elif bus=="ac":
#             self.total=self.ac()
#         else:
#             print(" Bus type not available")
#             return
#         self.billing()
#     def billing(self):
#         gst=self.total * 10/100
#         amount=self.total+gst
#         charge=30
#         final_amount=amount +charge
#         print("fare: ",self.total)
#         print("gst: ",gst)
#         print("charge: ",charge)
#         print("final amount: ",final_amount)
# class AbhiBus(Bus):
#     def routes(self):
#         print("Available routes")
#         print("Hyd to Vij")
#         print("Hyd to Banglore")
#         print("Vij to Chennai")
#         print("Vij to Madhurai")
#     def booking(self):
#         self.routes()
#         route = input("Enter route: ").lower()
#
#         if route == "hyd to vij":
#             print("Route selected:", route)
#         elif route == "hyd to bangalore":
#             print("Route selected:", route)
#         elif route == "vij to chennai":
#             print("Route selected:", route)
#         elif route == "vij to madhurai":
#             print("route selected:", route)
#         else:
#             print("Route not available")
#             return
#
#         bus=input("Enter bus type: ").lower()
#         if bus=="sleeper":
#             self.total=self.sleeper()
#         elif bus=="semi_sleeper":
#             self.total=self.semi_sleeper()
#         elif bus=="ac":
#             self.total=self.ac()
#         else:
#             print(" Bus type not available")
#             return
#         self.billing()
#     def billing(self):
#         gst=self.total * 10/100
#         amount=self.total+gst
#         charge=20
#         final_amount=amount +charge
#         print("fare: ",self.total)
#         print("gst: ",gst)
#         print("charge: ",charge)
#         print("final amount: ",final_amount)
# choice=input("Choose the platform:").lower()
# if choice=="redbus":
#     r=RedBus()
#     r.booking()
# elif choice=="abhibus":
#     a=AbhiBus()
#     a.booking()
# else:
#     print("Invalid platform")



                                        ##MULTIPLE INHERITANCE##
class SBI:
    def deposit(self,amount):
        self.balance+=amount
        print("Amount deposited:",amount)
    def check_bal(self):
        print("Balance:",self.balance)
class UnionBank:
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdraw success:", amount)
        else:
            print("Invalid amount")
    def mini_stmt(self):
        print("mini_statement")
        print("Current balance:",self.balance)
class ATM(SBI,UnionBank):
    def menu(self):
        print("ATM menu:")
        print("1. deposit")
        print("2. withdraw")
        print("3. check balance")
        print("4. mini-statement")
        print("5. Exit")
    def transaction(self):
        self.balance=0
        while True:
            self.menu()
            choice=input("enter your choice:")
            if choice==1:
                amount=int(input("enter amount to deposit:"))
                self.deposit(amount)
            elif choice==2:
                amount=int(input("enter amount to withdraw:"))
                self.withdraw(amount)
            elif choice==3:
                self.check_bal()
            elif choice==4:
                self.mini_stmt()
            elif choice==5:
                print("Thank you for using")























                                                        ###POLYMORPHISM###
# class Animal:
#     def Sound(self):
#         print("animal sounds")
# class Dog(Animal):
#     def Sound(self):
#         print("dog barks")
# class Cat(Animal):
#     def Sound(self):
#         print("cat meows")
# a=Animal()
# d=Dog()
# c=Cat()
# a.Sound()
# d.Sound()
# c.Sound()



# class Payment:
#     def Pay(self):
#         print("pay amount")
# class Creditcard(Payment):
#     def Pay(self):
#         print("pay through creditcard")
# class UPI(Payment):
#     def Pay(self):
#         print("pay through upi")
# class Cash(Payment):
#     def Pay(self):
#         print("pay through cash")
# c=Creditcard()
# u=UPI()
# ca=Cash()
# c.Pay()
# u.Pay()
# ca.Pay()



# class Employee:
#     def work(self):
#         print("employee works")
# class Developer(Employee):
#     def work(self):
#         print("developer writes the code")
# class Tester(Employee):
#     def work(self):
#         print("tester tests the software")
# class Manager(Employee):
#     def work(self):
#         print("Manager manages the team ")
# d=Developer()
# t=Tester()
# m=Manager()
# d.work()
# t.work()
# m.work()



# class Bank:
#     def __init__(self,balance):
#         self.__balance=balance
#     def get_bal(self):
#         return self.__balance
#     def set_bal(self,balance):
#         self.__balance=balance
#
# b=Bank(10000)
# obj=b.get_bal()
# print(obj)
# b.set_bal(20000)
# print(b.get_bal())



# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance=self.__balance+amount
#     def check_bal(self):
#         print(self.__balance)
# b=BankAccount(10000)
# b.deposit(15000)
# b.check_bal()



# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#         # print("animal sounds")
# class Dog(Animal):
#     def sound(self):
#         print("dog barks")
# d=Dog()
# d.sound()


                                                ##encapsulation##

# class BankAccount:
#     def __init__(self,acc_num,balance):
#         self.acc_num=acc_num
#         self.__balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print("deposited=",amount)
#         else:
#             print("insufficient deposit amount")
#     def withdraw(self,amount):
#         if amount<=0:
#             print("invalid withdraw amount")
#         elif amount>self.__balance:
#             print("insufficient balance")
#         else:
#             self.__balance-=amount
#             print("withdrawl=",amount)
#     def check_bal(self):
#         print("balance:",self.__balance)
# b=BankAccount("1234567890",10000)
# b.check_bal()
# b.deposit(5000)
# b.check_bal()
# b.withdraw(3000)
# b.check_bal()
# b.withdraw(15000)
# b.__balance=15000




# class Securefile:
#     def __init__(self,content,pwd):
#         self.__content=content
#         self.__pwd=pwd
#         self.__log=[]
#     def read(self,pwd):
#         if (pwd==self.__pwd):
#             int(self.__content)
#             self.__log.append("content are read")
#         else:
#             self.__log.append("incorrect pwd attempt")
#     def get_logs(self):
#         return self.__log.copy()
# p1=Securefile("photos",123)
# p1.read(1234)
# p1.read(3665)
# log=p1.get_logs()
# print(log)



# class Product:
#     def __init__(self,price,discount):
#         if price>0:
#             self.__price=price
#         if discount<=70 and discount>0:
#             self.__discount=discount
#     def __cal_final_price(self):
#         final=self.__price-(self.__price*(self.__discount/100))
#         print(final)
#     def get_final(self):
#         self.__cal_final_price()
# p1=Product(500,10)
# p1.__cal_final_price()
# p1.get_final()




# class Character:
#     def __init__(self,max_health):
#         self.max_health=max_health
#         self.__health=max_health
#     def heal(self,point):
#         if point>0:
#             self.__health+=point
#             if self.__health>self.max_health:
#                 self.__health=self.max_health
#     def damage(self,points):
#         if points>0:
#             self.__health-=points
#             if self.__health<0:
#                 self.__health=0
# ch=Character(100)
# ch.damage(50)
# ch.damage(60)
# ch.heal(100)
# ch.heal(20)


# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#     def area(self):


