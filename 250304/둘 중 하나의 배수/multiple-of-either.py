a = int(input())

if 1 <= a <= 1000 :
    if a % 3 == 0 or a % 5 == 0 :
        print(1)
    else :
        print(0)
else :
    print("error")