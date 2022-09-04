num=int(input("Enter Number :"))

var= False

for i in range(2,num):
    if(num % i==0):
        var=True

if var:
    print("Number is Not prime...")
else:
    print("Number is Prime...")