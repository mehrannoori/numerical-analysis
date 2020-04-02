
#=======> مثال 7 صفحه 141  <=======#


def f(xn,yn):
    return 1-2*xn*yn

def k1(h,xn,yn):
    return h*f(xn,yn)

def k2(h,xn,yn,a,b):
    return h*f(xn+a*h, yn+b*k1(h,xn,yn))

def main():
    #روش نقطه میانی
    a,b = 0.5,0.5
    A = 0
    B = 1

    #روش هیون
    #a,b = 2/3, 2/3
    #A = 1/4
    #B = 3/4

    x0 = 0
    y0 = 0
    c = 1
    N = 10
    h = (c-x0)/10
    x = [0 for i in range(N+1)]
    y = [0 for i in range(N+1)]
    x[0] = x0
    y[0] = y0

    for n in range(1,N+1):
        x[n] = x[n-1]+h
        y[n] = round(y[n-1] + A*k1(h,x[n-1],y[n-1]) + B*k2(h,x[n-1],y[n-1],a,b),2)
    
    print(f"y({x0}) = {y0}")
    print("Answer is :")
    print( f"y({c}) = {y[-1]}" )
    print()
    print(f"y = {y}")


if __name__ == "__main__":
    main()
