a, b = input().split()

a, b = int(a), int(b)

if 1 <= a <= 100 and 1 <= b <= 100 :
    for i in range(b, a-1, -1) :
        print(i, end = " ")
else :
    print("")