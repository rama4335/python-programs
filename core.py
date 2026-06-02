                           #return stmt programs#
def fun(x,y):
    return x+y
print(fun(10,20))


def fun(x,y):
    print(x,y)
    return x+y
    print(x+x)
    return y+y
print(fun(10,20))

def great(a,b):
    if a>b:
        return a
    else:
        return b
print(great(75,77))


def fun(*a):
    return sum(a)
x=fun(1,7,8,6,5,3,2,8)
if x%2==0:
        print("even:",{x})
else:
        print("odd:",{x})

name=input("enter your name:")
s=f"name:{name}"
print(s)

name="sri"
S=f"name:{name}"
print(S)


                                   ## higher order functions(map(), filter(), reduce(), and sort() )
l=[1,2,3,4,5,6,7,8]
sq=list(map(lambda x:x*x, l))
print(sq)


l=[2,3,6,8,9,4,1,6,8,4]
even=list(filter(lambda x:x%2==0,l))
print(even)


from functools import reduce
str=[".", "j", "o", "i", "n", "(" ")"]
k=reduce(lambda x,y:x+y,str,"@")
print(k)

from functools import reduce
l=[1,7,5,8,9,110]
k=reduce(lambda x,y:x if x>y else y, l)
print(k)


l=[[1,2],[3,4],[5,6]]
k=list(map(lambda x:x+[5],l))
print(k)


l=[[1,2],[3,4],[5,7]]
result=list(map(lambda x:list(map(lambda x:x+5,x)),l))
k=list(map(lambda x:x+[5],l))
print(result)
print(k)


d={"apple":100, "banana":40, "cherry":150}
result=list(filter(lambda item:item[1]>50, d.items()))
print(result)


from functools import reduce
l=[12,45,7,89,23]
k=reduce(lambda x,y:x if x>y else y, l)
print(k)


str="PYTHON"
k=list(map(ord, str))
print(k)


str='RAMADEVI'
k=list(filter(lambda x:x in "AEIOU",str))
print(k)

l=[10,20,30,40,50]
k=list(map(id,l))
print(k)


print(list(map(lambda x:str(x),[1,2,3])))
print(list(map(str,[1,2,3])))

l=[5,10,15,20,25,30]
k=list(map(lambda x:x*x, l))
print(k)

l=[5,10,15,20,25,30]
k=list(filter(lambda x:x%5==0,l))
print(k)

from functools import reduce
l=[5,10,15,20,25,30]
k=reduce(lambda x,y:x+y, l)
print(k)


d={"apple":100, "banana":40, "cherry":150}
result=list(filter(lambda x:d[x]>50,d))
print(result)

d={"apple":100, "banana":40, "cherry":150}
k=list(filter(lambda item:item[1]>50,d.items()))
print(k)


a=[1,2,3,4]
b=[10,20,30,40]
k=list(map(lambda x,y:x+y,a,b))
print(k)


nums=[12,15,7,18,20,21,25]
k=list(filter(lambda x:(x%3==0 or x%5==0) and not (x%3==0 and x%5==0),nums))
print(k)

from functools import reduce
nums=[1,2,3,4]
result=reduce(lambda x,y:x+y,nums,10)
print(result)


nums=[[1,2], [3,4], [5,6]]
result=list(map(lambda x:x.append(10),nums))
print("Result:",result)
print("Nums:",nums)

d={"apple":100, "banana":40, "cherry":150}
k=list(filter(lambda item:item[1]>50,d.items()))
print(k)


l="rama"
k=list(map(ord, l))
print(k)


l='ramadevi'
k=list(filter(lambda x:x in "aeiou", l))
print(k)



def say_hello():
    print("welcome to python!")
say_hello()


def add(a,b):
    print(a+b)
add(1,4)

def add(a,b):
    return a+b
print(add(2,4))

def fun(l,b):
    print(l*b)
fun(6,4)

def fun(l,b):
    return l*b
area=fun(6,4)
print("Area:",area)

def test_function():
    print("This function has no return statement")
result=test_function()
print("Returned value:",result)


def greet(name):
    print("hello," + name + "!")
greet("rama")
greet("devi")


def student_info(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")
student_info('rama', 20,'A')


def product(a,b,c):
    p=a*b*c
    print(p)
product(10,3,4)

def fun(animal,name):
    print(f"My {animal} is named {name}")
fun('cat', 'sofi')


def fun(a,b,c):
    print(a+b+c)
fun(1,2)   #type error#


def power(base,exponent):
    print(base**exponent)
power(10,2)


def full_name(first,middle,last):
    print(f"My name is {first} {middle} {last}")
full_name('Mutyala', 'Rama', 'Devi')

def full_name(first,middle,last):
    k=(f"My name is {first} {middle} {last}")
    print(k)
full_name('Mutyala', 'Rama', 'Devi')




