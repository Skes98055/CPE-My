for i in range(eval(input())):
    a,b=map(int,input().split())
    s=(a+b)/2
    d=(a-b)/2
    
    if(a>=b and s%1==0 and d>=0):
        print("%d %d"%(s,d))
    else:
        print("impossible")
