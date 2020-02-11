def factor(x):
    if x==0 or x==1 :
        return 1
    return x * factor( x-1 )

def divid(x,f,n):
    for i in range(1,n):
        for j in range(n-i):
            f[j][i] = f[j+1][i-1]-f[j][i-1]
    return f

def display(x,n,f):
    for i in range(n):
        print( x[i], end="\t" )
        for j in range(n-i):
            print(f[i][j], end="\t")
        print()

def tarkib(r,k):
    t = r
    for i in range(1,k):
        t = t*(r-i)
    return t


def formul(x,n,f,z):
    sum = f[0][0]
    r = (z-x[0])/(x[1]-x[0])
    for k in range(1,n):
        sum = sum + ( tarkib(r,k) * f[0][k] ) / factor(k)
    return sum
if __name__ == "__main__":
    #x = [45,50,55,60]
    #y = [ 0.7071, 0.7660, 0.8192, 0.8660 ]
    #n = len(x)
    #z = 52

    x = [4, 6, 8, 10]
    y = [1,-2,-3,-6]
    z = 4.3
    n = len(x)

    f = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        f[i][0] = y[i]

    f = divid(x,f,n)
    print("f(",z,") = ",formul(x,n,f,z))
    #display(x,n,f)


    
