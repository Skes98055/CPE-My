while True:
    try:
        all="abcdefghijklmnopqrstuvwxyz"
        ans=""
        a=input().lower()
        b=input().lower()
        for i in range(len(all)):
            a1=a.count(all[i])
            b1=b.count(all[i])
            ans+=(all[i]*min(a1,b1))
        print(ans)
    except:
        break
