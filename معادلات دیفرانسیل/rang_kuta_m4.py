
## رانگ کوتا مرتبه 4

#============>مثال 8 صفحه 142 <==============#


def f(xn,yn):
    return 2*xn*yn

def k1(h,xn,yn):
    return f(xn,yn)

def k2(h,xn,yn):
    return f(xn+h/2, yn+h/2*k1(h,xn,yn))

def k3(h,xn,yn):
    return f( xn+h/2 , yn+h/2*k2(h,xn,yn) )

def k4(h,xn,yn):
    return f( xn+h , yn+h*k3(h,xn,yn) )

def main():
    
    x0 = 1
    y0 = 1
    c = 1.5
    h = 0.1
    N = int((c-x0)/h)
    x = [0 for i in range(N+1)]
    y = [0 for i in range(N+1)]
    x[0] = x0
    y[0] = y0

    for n in range(1,N+1):
        x[n] = x[n-1]+h
        y[n] = round(y[n-1] + (h/6)*( k1(h,x[n-1],y[n-1])+  2*k2(h,x[n-1],y[n-1]) + 2*k3(h,x[n-1],y[n-1]) + k4(h,x[n-1],y[n-1]) ),4)
    
    print(f"y({x0}) = {y0}")
    print("Answer is :")
    print( f"y({c}) = {y[-1]}" )
    print()
    print(f"y = {y}")

if __name__ == "__main__":
    main()
