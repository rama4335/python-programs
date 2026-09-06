# class Student:
#     def __init__(self,name,age,clg):
#         self.name=name
#         self.age=age
#         self.clg=clg
#     def __str__(self):
#         return f" my name is {self.name},my age is {self.age},my clg is {self.clg}"
#     def __repr__(self):
#         return f"{self.name}"
# s1=Student("rama",21,"MVR")
# s2=Student("devi",22,"KLU")
# print(s1)
# l=[s1,s2]
# print(l)

# l=list(range(1,10))
# for i in l:
#     print(i)

class Num:
    def __init__(self):
        self.num=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<5:
            value=self.num
            self.num+=1
            return value
        else:
            raise StopIteration
a=Num()
for i in a:
    print(i)


