from functools import reduce
myList = ["Raj","Rani","Farhan","Rutwik","Neha"]
map_object=map(lambda s:s[1]=="a",myList)
print(list(map_object))

mydata = [20,30,50,30,30,50,60]
print(reduce(lambda x,y:x*y,mydata))