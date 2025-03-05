user = input()
arr = user.split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if -100 <= a <= 100 and -100 <= b <= 100 and -100 <= c <= 100 :
    if a > 0 and b > 0 and c > 0:
        if a > b and b > c :
            print(a)
        elif b > a and b > c :
            print(b)
        else :
            print(c)
    else :
        if a < b and a < c :
            print(a)
        elif b < a and b < c :
            print(b)
        else :
            print(c)
else :
    print("error")