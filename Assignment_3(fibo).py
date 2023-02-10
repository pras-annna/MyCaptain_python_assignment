lim=int(input("enter limit:"))
f,s,sum=0,1,0
while sum<=lim:
    print(sum)
    f=s
    s=sum
    sum=f+s
