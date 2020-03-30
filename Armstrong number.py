def armstrong (num):
    n1=1
    n2=1
    n3=0
    while(num>1):
        n1=num%10
        #print(n1)
        n2=(n1*n1*n1)
        #print(n2)
        n3=n2+n3
        #print(n3)
        num=int(num/10)
    return (n3)
value1=int(input('Enter the first number '))
value2=int(input('Enter the second number '))
d=range(value1,value2)
u=0
for x in d:
    res=armstrong(x)
#print(res)
#m=range(0,value)
#for(p in m):
    if(res==x):
        print(res)
        u+=1
    #else:
        #u=0
if(u==0):
    print('no armstrog number in given range')
#else:
    #print('given number is not armstrong number')
