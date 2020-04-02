

#=======> مثال 3 صفحه 134  <=======#
import math

# y'= 0.1*sqrt(y) + 0.4x^2   =>   f(x,y) = 0.1*sqrt(y) + 0.4x^2
def f(xn, yn):
    return 0.1*math.sqrt(yn) + 0.4*xn*xn

# y[n+1] = y[n] + h*f(x[n],y[n])
def y1(xn,yn,h):
    return round(yn + h*f(xn,yn),4)

def main():
    x0 = 2.0
    y0 = 4.0
    
    h = 0.1
    c = 2.5
    
    N = int((c-x0)/h)

    x = [0 for i in range(N+1)]
    y = [0 for i in range(N+1)]

    x[0] = x0
    y[0] = y0
    for n in range(1,N+1):
        y[n] = y1(x[n-1],y[n-1],h)
        x[n] = x[n-1] + h
    
    print(f"y({x0}) = {y0}")
    print("Answer is :")
    print( f"y({c}) = {y[-1]}" )
    print()
    print(f"y = {y}")


if __name__ == "__main__":
    main()
    
