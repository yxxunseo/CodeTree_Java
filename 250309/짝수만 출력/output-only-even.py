a, b = input().split()

a, b = int(a), int(b)

if 1 <= a <= 50 and 1 <= b <= 50 and a % 2 == 0 and b % 2 == 0 :
    while a <= b :
        print(a, end = " ")
        a += 2 
else :
    print("error")