import math
def f(x):
    return (
        math.exp(-x)/(x*x+1)
    )

def zouzanaghe_morakab(h,a,b,n):
    res = 0
    x0 = a+h
    for i in range(n-1):
        res = res + f(x0)
        x0 = x0+h
    return (
        (h/2)*(f(a) + 2*res + f(b))
    )

def main():
    a = 0.0
    b = 1.0
    n = 4
    h = ((b-a)/n)
    print("f(x)= exp(x)/x^2+1 in [%d,%d]"%(a,b))
    print("h=%f"%(h))
    print("Result : ",
        zouzanaghe_morakab(h,a,b,n)
    )

if __name__=="__main__":
    main()
