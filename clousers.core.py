def electricity(rate_per_unit):
    def units(no_of_units):
        print("total electricity bill:",rate_per_unit * no_of_units)
    return units
obj=electricity(50)
obj(100)


def salary(bonus):
    def inner(emp_basic_sal):
        print("total salary:",bonus+emp_basic_sal)
    return inner
obj=salary(5000)
obj(40000)



def discount(percent):
    def inner(price):
        final_price=price-(price * percent / 100)
        print("final price:",final_price)
    return inner
obj=discount(20)
obj(500)



def bank_acc(balance):
    def inner(withdraw):
        print("remaining balance:",balance-withdraw)
    return inner
obj=bank_acc(40000)
obj(15000)



def movie(movie_name):
    def inner(p_name):
        print(p_name,"booked a ticket for the movie",movie_name)
    return inner
obj=movie('chennai love story')
obj("rama")



def multiplier(number):
    def inner(another_num):
        print(number*another_num)
    return inner
obj=multiplier(25)
obj(20)



def res(food_item):
    def inner(quantity):
        print("food item:",food_item)
        print("quantity:",quantity)
    return inner
obj=res('biryani')
obj(2)




def create_password(password):
    def inner(other_password):
        if password==other_password:
            print("Access granted")
        else:
            print("Access denied")
    return inner
obj=create_password('rama123')
obj('rama1234')


def shopping_cart(item_name):
    def inner(quantity,price):
        print("item name:",item_name)
        print("quantity:",quantity)
        print("total price:",quantity*price)
    return inner
obj=shopping_cart('biryani')
obj(2,500)



def counter():
    count=0
    def increments():
        nonlocal count
        count+=1
        print("count:",count)
    return increments
c=counter()
c()
c()
c()
c()
c()
