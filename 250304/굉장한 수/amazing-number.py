n = int(input())

if 1 <= n <= 100 :
    if (n % 2 != 0 and n % 3 == 0) or (n % 2 == 0 and n % 5 == 0) :
        print("true")
    else :
        print("false")
else :
    print("error")