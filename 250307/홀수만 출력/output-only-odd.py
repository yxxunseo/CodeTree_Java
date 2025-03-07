a,b = input().split()

a,b = int(a), int(b)

if 1 <= a <= 100 and 1 <= b <= 100 and a % 2 == 1 and a % 2 == 1 :
    for i in range(a, b+1, 2) :
        print(i, end = " ")
else :
    print("error")