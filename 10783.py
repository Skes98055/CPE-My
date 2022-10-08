for i in range(eval(input())):
    sum=0
    for j in range(eval(input()),eval(input())+1):
        if(j%2!=0):
            sum+=j
    print("Case %d: %d"%(i+1,sum))
