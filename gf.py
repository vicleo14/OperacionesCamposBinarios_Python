#Author: Morales Flores Victor Leonel
#Date: 24/04/2019
#Description:
#This porgram multiplies two polynomials module m. m,a and b are given by the user as integers.
def potM(m):
    potencia=0
    pol=""
    while(m!=0):
        if(m%2!=0):
            #print("Potencia:"+str(potencia))
            #pol="x^{}+".format(potencia)+pol
            pol="1"+pol
        else:
            pol="0"+pol
        potencia+=1
        m=m>>1
    potencia-=1
    print(pol)
    print("Potencia máxima:{}".format(potencia))
    return potencia
def f(m,n,a,b):
    potActual=0
    result=0
    while(a!=0):
        if(a%2!=0):
            for i in range(potActual):
                result+=multX(m,n,b)
        potActual+=1
        a=a>>1
    return result


def multX(m,n,b):
    if(n<=1):
        return b
    elif (2**n>b):
        return b<<1
    else:
        return (b<<1)^m

def main():
    m=int(input("Indica m:"))
    n=potM(m)
    a=int(input("Indica a:"))
    b=int(input("Indica b:"))
    result=f(m,n,a,b)
    print(potM(result))

if __name__ == '__main__':
    main()
