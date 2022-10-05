def printMonth(start, max_days):
    print("KIT")
    print('-'*27)
    count = 0
    for i in range(start):
        print('{:3s}'.format(''),end=' ')
        count = count + 1
    for day in range(1, max_days+1):
        if count % 7 ==0 and count !=0:
            print()
        print ('{:3d}'.format(day),end=' ')
        count = count + 1
    print()
    print('-'*27)
printMonth(0,31)

