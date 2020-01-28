# f(x)=x^2-2
def f(x):
    return x*x-2

# f'(x)=2x
def fp(x):
    return 2*x
    
# error = 0.0001
# x0 = 1
def res():
    x = 1 
    xk = 0
    while True :
        xk = x - ( f(x) / fp(x) )
        if abs(xk-x)<=0.0001 :
            return xk
        x = xk

if __name__ == "__main__":
    print( res() )
