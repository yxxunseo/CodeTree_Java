b, a = input().split()

b, a = int(b), int(a)

if 1 <= a <= 50 and 1 <= b <= 50 and a % 2 == 0 and b % 2 == 0 :
    while b >= a :
        print(b, end = " ")
        b -= 2
else :
    print("error")