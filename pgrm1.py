# age=18
# if age<=18:
#     print("eligible")
# else:
#     print("not eligible")

# a=10
# b=20
# if a<b:
#     print("a")
# else:
#     print("b")


# def display(n, a, b):
#     print(f"name:{n}")
#     print(f"age:{a}")
#     print(f"Branch:{b}")
# display("rama", 21, "cse")


# def display():
#     print(f"name:{n}")
#     print(f"age:{a}")
#     print(f"branch:{b}")
#     n="rama"
#     a=21
#     b="cse"
# display()


# def greet():
#     print("hello!")
# greet()



# def display(n="unknown", a=0, b="none"):
#     print(f"name:{n}")
#     print(f"age:{a}")
#     print(f"branch:{b}")
# display()


# def rama(name, age, gender):
#     print(f"name:{name}")
#     print(f"age:{age}")
#     print(f"gender:{gender}")
# rama("rama", 21, "female")


# def f(x):
#     return x**3+7*x+10
# def g(y):
#     return y**2+2*y+35
# def v(x,y):
#     return f(x),g(y)
# print(v(2,3))


# def f():
#     print("x^3+7x+10")
# f()
# def f():
#     print("y^2+2y+35")
# f()


# def func(x=10, y=70, z=50):
#     print(x,y,z)
#     print(x+y+z)
# func(70,70)
# func()


# list=[10,20,30,40,50]
# list.append(20)
# list.insert(1,100)
# list.copy()
# list.clear()
# list.append(20)
# print(list[::-1])


# a=12
# if a%2==0:
#     print("even")
# else:
#     print("odd")


# num=int(input("enter a number"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# n=20
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#     else:
#         print("prime number")




# def fun(*a):
#     print(a)
#     print(*a)
# fun(10,20,30,40,50)
# # above we use single parameter and pass multiple arguments,in this it stores in the tuple format#
# #by using * symbol#


# def fun2(**b):
#     print(b)
#     print(**b)# error came
# fun2(a=75,b=30,c=40,d=70)

# def fun2(**b):
#     print(b)
# fun2(a=75,b=30,c=40,d=70)


# def fun3(a,b,c,d):
#     print(a,b,c,d)
# def fun2(**b):
#         print(b)
#         fun3(**b)
# fun2(a=75, b=30, c=40, d=70)


# def fun5(*a,**b):
#     print(a,b,sep="\n")
# fun5(10,2,7,b=29)


# def fun6(*a):
#     print(sum(a))
# fun6(1,2,3,4)

# def fun(*a): #total sum#
#     sum=0
#     for i in a:
#         sum+=i
#     print(sum)
# fun(1,2,3,4,5)


# def fun(*a):  # even numbers sum#
#     sum=0
#     for i in a:
#        if i%2 == 0:
#            sum+=i
#     print(sum)
# fun(1,2,3,4,5)

#fun(1,2,3,4,5,6,7,8,8,9,10)#

# def fun(*a):  # alternate numbers sum#
#     sum=0
#     c = 0
#     for i in a:
#         if c%2 == 1:
#            sum+=i
#         c=c+1
#     print(sum)
# fun(1,2,3,4,5,6)


#using while loop#
# def fun(*a):
#     i=0
#     c=0
#     s=0
#     while i<len(a):
#         if c%2==0:
#             s+=a[i]
#
#         i+=1
#         c+=1
# fun(1,4,6,8,2,3,4,55)



# def fun(*a):
#     print(sum(a[1::2]))
# fun(1,2,3,4,5,6,7)
