def summ(a,b):
    c=a+b
    return c

def raz(a,b):
    r=a-b
    return r
a=float(input("Введи первое число"))
b=float(input("Введи второе число"))
znak=(input("Введите знак"))
if znak=='+':
    c=summ(a,b)
elif znak=='-':
    c=raz(a,b)
elif znak=='*':
    def umn(a,b):
        n=a*b
        return n
elif znak=='/':
    def dele(a,b):
        z=a/b
        return z
elif znak=='**':
    def st(a,b):
        t=a**b
        return t
print(f"{a}{znak}{b}={c}")
