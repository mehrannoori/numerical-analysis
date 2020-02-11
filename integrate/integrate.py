import math

def function(x):
    return math.sin(x)/x

def middle_point(a,b):
    return (
        (b-a)*function( (a+b)/2 )
    )

def zouzanaghe(a,b,ep):
    return (
        ( (b-a)/2 ) * ( function(a+ep)+function(b) )
    )
    
def simpson(a,b,ep):
    h = (b-a)/2
    c = (a+b)/2
    return (
        (h/3) * (function(a+ep) + 4*function(c) + function(b))
    )

if __name__ == "__main__":
    a = 0
    b = math.pi
    ep = 0.00001
    print("f(x)=Sin(x)/x")
    print("Integrate result 1 : ",middle_point(a,b) )
    print("Integrate result 2 : ",zouzanaghe(a,b,ep) )
    print("Integrate result 3 : ",simpson(a,b,ep) )
