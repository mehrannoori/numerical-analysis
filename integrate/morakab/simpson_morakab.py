import math
def f(x):
    return (
        math.sin(x)/x
    )


def simpsson_morakab(a,b,h,n):
    lx = []
    a0 = a+0.0000001
    for i in range(n+1):
        lx.append(a0)
        a0 = a0+h
    f1 = [f(lx[i])for i in range(len(lx))]
    
    r1 = 0
    r2 = 0

    for k in range(1,n-1):
         r1 = r1 + f1[2*k]
         r2 = r2 + f1[2*k-1]
    
    res = (h/3)*( f1[0] + 2*r1 + 4*r2 + f1[n] )
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
        simpsson_morakab(a,b,h,n)
    )
if __name__=="__main__":
    main()
    #print((math.pi+8)/6)
