lst=[]
while True:
    n=input("Enter num or # to stop:")
    if n=='#':
        break
    elif int(n)>0:
        lst.append(int(n))
print(lst)
