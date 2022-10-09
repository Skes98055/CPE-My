all = []
number = 0
while True:
    try:
        a=input()
        all.append(a)
        number =max(len(a),number)
    except:
        break
for i in range(number):
    for j in range((len(all)-1),-1,-1):
        try:
            print(all[j][i],end='')
        except:
            print(' ',end='')
    print()

