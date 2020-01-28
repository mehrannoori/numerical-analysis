import math
# f(x)=3x^2-e^x=0
def f(x):
    return 3*x*x - math.exp(x)

# f(x)=x-g(x)
# g(x)=sqrt(e^x/3) for [0,1]
def g(x):
    return math.sqrt(math.exp(x)/3)

def res():
    x0 = 1
    x = 0
    while True:
        x = g(x0)
        if abs( x0-x <= 0.001 ):
            return g(x)
        x0 = x

if __name__ == "__main__":
    print(res())
