ls=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
ls1=[]
c=int(input("enter the last value of tuple"))
for i in range(len(ls)):
    j=0
    a=ls[i][j]
    b=ls[i][j+1]
    new_tuple=(a,b,c)
    ls1.append(new_tuple)
print(ls1)