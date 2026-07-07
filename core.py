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


from functools import reduce
l=["Hello", 'Hi', "who','are", "you?"]
vowels='aeiou'
k=list(map(lambda x:''.join(filter(lambda x:x not in vowels,x)),l))
print(k)
m=list(map(lambda x:sum(map(ord,x)),k))
print(m)



l=["hello", 'hii', "who','are", "you?"]
k=list(map(lambda x:x if x not in "aeiou" else " ",l))
print(k)



l=["hello", 'hii', "who','are", "you?"]
k=list(map(func,l))


def func(x):
    s=" "
    for i in x:
        if i not in "aeiou":
            s+=1
    return s


def func(x):
    k=list(map(fun2,x))
    k=" ".join(k)
    return k

def fun2(y):
    if y not in "aeiou":
        return y

result=list(map(lambda x:reduce(lambda y,z:y+(ord(z),x,0),k)))



def fun():
    return 'hello'
x=fun()
print(x)


def add(c,b):
    return c+b
x=add(9,4)
print(x)

def add(a,b):
    print(a+b)
add(2,3)

def welcome():
    print("Welcome to Python")
welcome()

def fun():
    return'welcome to python'
x=fun()
print(x)

def sq(n):
    print(n*n)
sq(10)

def sq(n):
    return n*n
x=sq(7)
print(x)

def cube(n):
    print(n**3)
cube(4)

def area_of_rect(l,b):
    print(l*b)
area_of_rect(6,4)

def fun(name):
    print(f"my name is",name)
fun("rama")

def fun(*a):
    total=0
    for i in a:
        total=total+i
    return total
print(fun(1,2,3,4,5))

def greet(name):
    print("hello",name)
greet('rama')
greet('devi')

def stu(name, age, gender):
    print(f"name:{name},age:{age},gender:{gender}")
stu('rama', 21, 'female')


def stu(name, age, gender):
    print(f"name:",{name})
    print(f"age:",{age})
    print(f"gender:",{gender})
stu('rama', 21, 'female')

def fun(animal,name):
    print(f"my {animal} is named as {name}")
fun('cat','rama')


def fun(base,exponent):
    print(base**exponent)
fun(2,3)

def fun(first,middle,last):
    print(first,middle,last)
fun('rama','devi','mutyala')

def avg(a,b,c):
    return (a+b+c)/3
x=avg(10,20,30)
print(x)

def intro(name,city,hobby):
    print(f"my name is {name}")
    print(f"i am from {city}")
    print(f"my hobby is {hobby}")
intro('rama','hyd','listening music')

def sub(a,b):
    return a-b
x=sub(10,3)
print(x)

def bio(first_name,last_name,age):
    return first_name,last_name,age
x=bio('mutyala','ramadevi',21)
print(x)
def address(city,state,country):
    return f"city:{city}\nstate:{state}\ncountry:{country}"
x=address('kpd','ap','india')
print(x)

def bio(name,age,gender):
    return f"{name},{age},{gender}"
x=bio(age=21,gender='female',name='rama')
print(x)

def booking(name,source,destination,tickets):
    return f"name:{name}\nsource:{source}\ndestination:{destination},tickets:{tickets}"
x=booking(tickets=2,name='rama',destination='hyd',source='kpd')
print(x)


def power(base,exponent=2):
    return base**exponent
print(power(5))
print(power(5,3))



def fun(name='guest'):
    return f"welcome {name}"
x=fun()
print(x)


k=lambda x:x**3
print(k(3))


k=lambda x,y:x if x>y else y
print(k(2,4))

add=lambda x,y:x+y
print(add(10,20))

even=lambda x:x%2==0
print(even(8))
print(even(5))

data=[(1, 'banana'), (2, 'rama'), (3, 'cherry')]
data.sort(key=lambda x:x[1])
print(data)

def pro_all(*a):
    product=1
    for i in a:
        product=product*i
    return product
print(pro_all(10,10,10,10))

def des_per(name,*hobbies):
    print("name:",name)
    print("hobbies:",hobbies)
des_per('rama','reading','music','dance')

def f(*a):
    print(type(a))
f(1,2,3)

def mixed(a,b,*args,**kwargs):
    print("a=",a)
    print("b=",b)
    print("args=",args)
    print("kwargs=",kwargs)
mixed(10,20,30,40,50,60,name='rama',age=21,gender='female')



l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result=list(map(lambda x:x*x,filter(lambda x:x%3==0,l)))
print(result)

students=[{'rama':'rama', 'score':30},
          {'name':'devi', 'score':65},
          {'name':'sri', 'score':70}]
k=list(filter(lambda x:x['score']>=60,students))
m=list(map(lambda x:{**x,'grade':'pass'},k))
n=sorted(m,key=lambda x:x["score"],reverse=True)
print(n)


data=[("rama",70),
      ("devi",80),
      ("sri",90)]
strategies={'by_name':lambda x:x[0],
            'by_score':lambda x:x[1],
            'by_length':lambda x:x[0]}
choice='by_score'
result=sorted(data,key=strategies[choice])
print(result)



l=[1,2,3,4,5,6,7,8,9,10]
k=list(map(lambda x:x*x,filter(lambda x:x%3==0,l)))
print(k)


double=lambda x:x*2
triple=lambda x:x*3
quadruple=lambda x:x*4
funs=[double,triple,quadruple]
def apply_all(funcs,value):
    for i in funs:
        value=i(value)
    return value
print(apply_all(funs,2))


def make_greeting(name,prefix='Hello',formatter=lambda x:x):
    return formatter(f"{prefix} {name}")
print(make_greeting("rama"))
print(make_greeting("rama",formatter=str.upper))


from functools import reduce
def avg(**scores):
    values=list(scores.values())
    total=reduce(lambda x,y:x+y,values)
    return total/len(values)
print(avg(maths=90,
          phy=80,
          che=70))


students=[{'name':'rama','score':80},
          {'name':'devi','score':50},
          {'name':'sri','score':70}]
n=sorted(map(lambda x:{**x,'grade':'pass'},filter(lambda x:x['score']>=60,students)),key=lambda x:x["score"],reverse=True)
print(n)




data=[("rama",90),
      ("devii",80),
      ("sri",70)]
strategies={'by_name':lambda x:x[0],
            'by_score':lambda x:x[1],
            'by_length':lambda x:x[0]}
choice='by_score'
result=sorted(data,key=strategies[choice])
print(result)

from functools import reduce
def calculator(*args,operation='add',**options):
    k={'add':lambda x:sum(x),
       'multiply':lambda x,y:x*y,
       'max':lambda x:max(x),
       'min':lambda x:min(x)}
    if options.get("show_steps"):
        print('numbers',args)
        print('operation',operation)
    return k[operation](args)
print(calculator(2,4,8))


##ATM transaction##

def atm(balance,withdraw_amount):
    def can_withdraw():
        return balance>=withdraw_amount
    if can_withdraw():
        print("withdraw successful")
        print("Remaining Balance=", balance-withdraw_amount)
    else:
        print("Insufficient balance")
atm(10000,8000)


company_budget=500000
def company_tracker():
    total_projects=100
    def update_projects():
        nonlocal total_projects
        total_projects=total_projects+20
        global company_budget
        company_budget+=100000
    update_projects()
    print(total_projects)
company_tracker()
print(company_budget)


def atm(balance,withdraw):
    def can_withdraw():
        return balance>=withdraw
    if can_withdraw():
        print("successful")
        print("remaining balance=",balance-withdraw)
    else:
        print("insufficient")
atm(5000,1000)


##online shopping##

def shopping(cart_amount):
    def cal_discount():
        if cart_amount>5000:
            return cart_amount* 0.20
        return 0
    discount=cal_discount()
    final_amount=cart_amount-discount
    print("Original amount=",cart_amount)
    print("discount=",discount)
    print("final_amount=",final_amount)
shopping(8000)


def shopping(amount):
    def discount():
        if amount>7000:
            return amount*0.10
        return 0
    def gst():
        return amount*0.15
    print("original=",amount)
    print("discount=",discount())
    print("gst=",gst())
shopping(10000)




