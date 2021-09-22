n=int(input())
while n:
    str=input()
    a=0
    b=0
    for i in range(len(str)):
        
        if str[i]=='0':
            a+=1
        elif str[i]=='1':
            b+=1
    if a>b:
            print(b)
    else:
        print(a)
                    
        
    n-=1    
