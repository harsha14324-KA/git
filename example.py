num=int(input("enter a  number:"))
for i in range(num):
    for j in range(i,num):
        print("*",end="")
    print()


num=int(input("enter a number:"))
for i in range(num+1):
    for j in range(i):
        print(i,end="")
    print()