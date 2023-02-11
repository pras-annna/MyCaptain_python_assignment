def freq(n):
    d=dict()
    for k in n:
        if k not in d:
            d[k]=1
        else:
            d[k]+=1
    return d
n=input("enter string")
x=freq(n)
x=sorted(x.items(),key=lambda i:i[1],reverse=True)
print(x)
