x = []
y = []
z = []
res = []

def read_file():
    file_ = open("input.txt","r")
    r1 =  file_.readline().split(" ")
    r2 =  file_.readline().split(" ")
    r3 =  file_.readline().split(" ") 
    for i in range(len(r1)):
        x.append( float(r1[i]) )
        y.append( float(r2[i]) )
    for i in range(len(r3)):
        z.append( float(r3[i]) )


def lk(k,a):
    l = 1
    for j in range(len(x)):
        if not j==k:
            l *= (a-x[j])/(x[k]-x[j])
    return l
                  
def pn(a):
    p = 0
    for i in range(len(y)):
        p += lk(i,a)*y[i]
    return p

if __name__ == "__main__":
    read_file()
    for i in z:
        res.append(pn(i))
    print("x : ", x)
    print("y : ", y)
    print("x0 : ", z)
    print("interp points : ", res)
