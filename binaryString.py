#Author: Morales Flores Victor Leonel
#Date: 24/04/2019
#Description:
#This porgram convert a binary string into a polynomial representation
def validate(a):
    for i in a:
        if(i!="1" and i!="0"):
            return False
    return True
def conversion(a):
    pol=""
    pot=len(a)-1
    for i in a:
        if(i=="1"):
            pol+="X^{}+".format(pot) if (pot!=0) else "1+"
        pot-=1
    pol=pol[0:-1]
    return pol


def main():
    a=input("Introduce una cadena binaria:")
    if(validate(a)):
        print("Representación:"+conversion(a))
    else:
        print("La cadena introducida no es binaria.")
if __name__ == '__main__':
    main()
