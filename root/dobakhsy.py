import math

def f(x):
    return x*math.exp(x)-1

def res():
    a = float(input("enter a : "))
    b = float(input("enter b : "))
    c, c1 = 0, 1
    while True:
        c = (a+b)/2
        if abs(c1-c)<0.0001 :
            return (c+c1)/2 
        if f(a)*f(c)<0:
            c1 = c
            b = c
        if f(b)*f(c)<0:
            c1 = c
            a = c
        if f(c)==0:
            return c

if __name__ == "__main__":
    print(res())
