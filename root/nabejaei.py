import math

def f( x):
    return x*math.sin(x)-1

def res():
    a = float(input("a : "))
    b = float(input("b : "))
    e = float(input("error : "))

    while True:
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        if abs(a-c)<= e:
            return c
        a = c
    

if __name__ == "__main__":
    print(res())
