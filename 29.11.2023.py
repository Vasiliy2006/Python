"""n=100
while n!=200:
    print(n)
    c=[]
    a=list(n)
    a.sort()
    c.append(a[2])
    c.append(a[1])
    print(c)
    n+=1"""

count=0
for n in range(100,1000):
    sp=[]
    c_max=[]
    c_min=[]
    a=n
    while a>0:
        sp.append(a%10)
        a=a//10
    sp.sort()
    c_max.append(sp[2])
    c_max.append(sp[1])
    if sp[0]!=0 and sp[1]!=0 :
        c_min.append(sp[0])
        c_min.append(sp[1])
    elif sp[0]==0 and sp[1]!=0 :
        c_min.append(sp[1])
        c_min.append(sp[0])
    elif sp[0]==0 and sp[1]==0 :
        c_min.append(sp[2])
        c_min.append(sp[1])
    k= int(''.join(map(str, c_max)))
    s= int(''.join(map(str, c_min)))
    rez=k-s
    if rez==35:
        count+=1
print(count)
 

