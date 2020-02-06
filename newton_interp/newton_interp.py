x = []
y = []
x0 = []
def read_file():
    file_ = open("input.txt","r")
    r1 =  file_.readline().split(" ")
    r2 =  file_.readline().split(" ")
    r3 =  file_.readline().split(" ") 
    for i in range(len(r1)):
        x.append( float(r1[i]) )
        y.append( float(r2[i]) )
    for i in range(len(r3)):
        x0.append( float(r3[i]) )

def p(i, z, x):
    p = 1
    for j in range(i):
        p = p*(z-x[j])
    return p

def formul(z, x, f, n):
    sum = f[0][0]
    for i in range(1,n):
        sum = sum + (p(i, z, x)*f[0][i])

def divid(x,f,n):
    for i in range(1,n):
        for j in range(n-i):
            f[j][i] = (f[j][i-1]-f[j+1][i-1])/(x[j]-x[i+j])
    return f

if __name__ == "__main__":
    read_file()
    n = len(x)
    f = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        f[i][0] = y[i]
    f = divid(x,f,n)
    for i in range(len(x0)):
        print(formul(x0[i], x, f, n),end = " ")
