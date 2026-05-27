
# l=[1,2,3,4,5,6,7,8]
# sq=list(map(lambda x:x*x,l))
# print(sq)
#
#
# l=[2,3,6,8,9,4,1,6,8,4]
# even=list(filter(lambda x:x%2==0,l))
# print(even)
#
#
# from functools import reduce
# str=[".", "j", "o", "i", "n", "(" ")"]
# k=reduce(lambda x,y:x+y,str,"@")
# print(k)
#
# from functools import reduce
# l=[1,7,5,8,9,110]
# k=reduce(lambda x,y:x if x>y else y,l)
# print(k)
#
#
# l=[[1,2],[3,4],[5,6]]
# k=list(map(lambda x:x+[5],l))
# print(k)


# l=[[1,2],[3,4],[5,7]]
# result=list(map(lambda x:list(map(lambda x:x+5,x)),l))
# k=list(map(lambda x:x+[5],l))
# print(result)
# print(k)


# d={"apple":100, "banana":40, "cherry":150}
# result=list(filter(lambda item:item[1]>50, d.items()))
# print(result)


# from functools import reduce
# l=[12,45,7,89,23]
# k=reduce(lambda x,y:x if x>y else y,l)
# print(k)


# str="PYTHON"
# k=list(map(ord, str))
# print(k)


# str="RAMADEVI"
# k=list(filter(lambda x:x in "AEIOU",str))
# print(k)

# l=[10,20,30,40,50]
# k=list(map(id,l))
# print(k)


# print(list(map(lambda x:str(x),[1,2,3])))
# print(list(map(str,[1,2,3])))


