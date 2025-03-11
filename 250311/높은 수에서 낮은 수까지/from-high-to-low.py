a, b = input().split()
a, b = int(a), int(b)

if 1 <= a <= 50 and 1 <= b <= 50 :
    if a > b :
        for i in range(a, b-1, -1) :
            print(i, end = " ")
    if b > a :
        for i in range(b, a-1, -1) :
            print(i, end = " ")
    if a == b :
        print(a)
else :
    print("error")