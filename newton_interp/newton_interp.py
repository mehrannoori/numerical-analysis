def read_file(x,y,z,address):
    file_ = open(address,"r")
    r1 =  file_.readline().split(" ")
    r2 =  file_.readline().split(" ")
    r3 =  file_.readline().split(" ")
    for i in range(len(r1)):
        x.append( float(r1[i]) )
        y.append( float(r2[i]) )
    for i in range(len(r3)):
        z.append( float(r3[i]) )



def pr(i,z,x):
    p = 1
    for j in range(i):
        p = p*(z-x[j])
    return p

def formul(z,x,f,n):
    sum = f[0][0]
    for i in range(1,n):
        sum = sum + (pr(i,z,x)*f[0][i])
    return sum

def divid(x,f,n):
    for i in range(1,n):
        for j in range(n-i):
            f[j][i] = (f[j][i-1]-f[j+1][i-1])/(x[j]-x[i+j])
    return f


if __name__ == "__main__":
    x = []
    y = []
    z = []
    address = "input.txt"
    read_file(x,y,z,address)
    n = len(x)
    
    f = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        f[i][0] = y[i]
    f = divid(x,f,n)
    for i in range(len(z)):
        print( 
            formul(z[i], x, f, n)
            ,end=" " 
            )
    #print(f)
