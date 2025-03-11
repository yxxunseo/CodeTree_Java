a, b = input().split()
a, b = int(a), int(b)

if -9 <= a <= 9 and 1 <= b <= 50 :
    if a > 0 :
        for i in range(b) :
            print(a, end = "")
    if a <= 0 :
        print("0")
else :
    print("error")