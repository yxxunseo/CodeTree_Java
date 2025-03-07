b, a = input().split()

b, a = int(b), int(a)

if 1 <= a <= 100 and 1 <= b <= 100 and a % 2 == 1 and b % 2 == 1 :
    for i in range(b, a-1, -2) :
        print(i, end = " ")
else :
    print("")