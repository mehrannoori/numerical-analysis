
#=======> مثال 5 صفحه 136  <=======#


# y'= y(-2x + 1/x)
def f(xn, yn):
    if xn == 0:
        return 1
    else:
        return yn*(-2*xn + 1/xn)

# رابطه اویلر اصلاح شده
def y1(xn,yn, xn1,h):
    return round( 
        yn+h/2*(f(xn,yn) + f(xn1,yn+h*f(xn,yn))) 
        ,4)

def main():
    x0 = 0.0
    y0 = 0.0
    
    h = 0.25
   #h=0.5 
    c = 2.0
    
    N = int((c-x0)/h)

    x = [0 for i in range(N+1)]
    y = [0 for i in range(N+1)]

    x[0] = x0
    y[0] = y0
    for n in range(1,N+1):
        x[n] = x[n-1] + h
        y[n] = y1(x[n-1],y[n-1],x[n],h)
        
    
    print(f"y({x0}) = {y0}")
    print("Answer is :")
    print( f"y({c}) = {y[-1]}" )
    print(y)


if __name__ == "__main__":
    main()
    
