import math
def f(x):
    return (
        math.sin(x)/x
    )


def middle_point_morakab(a,b,h,n):
    lx = []
    a0 = a+0.000001
    for i in range(n+1):
        lx.append(a0)
        a0 = a0+h
    f1 = [f(lx[i])for i in range(n+1)]
    #print(lx)
    #print(f1)
    r = 0

    for k in range(n-1):
         r = r + f1[2*k-1]
    
    res = (2*h)*(r)
    return res


def main():
    a = 0
    b = math.pi
    n = 4
    m = n/2
    h = math.pi/n
    print("f(x)= Sin(x)/x  in [%d,%d]"%(a,b))
    print("h=%f"%(h))
    print("Result : ",
        middle_point_morakab(a,b,h,n)
    )
if __name__=="__main__":
    main()
    #print((math.pi+8)/6)
