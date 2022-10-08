def compute(a):
    sum=0
    for i in range(len(a)):
        sum+=int(a[i])
    return str(sum)
while True:
    a=input()
    if(a=="0"):
        break
    while(len(compute(a))!=1):
        a=compute(a)
    print(compute(a))
