user = input()
arr = user.split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if -100 <= a <= 100 and -100 <= b <= 100 and -100 <= c <= 100 :
    if a <= b and a <= c :
        print(a)
    elif a <= b and a >= c :
        print(c)
    elif b <= a and b <= c :
        print(b)
    elif b <= a and b >= c:
        print(c)
    else :
        print(c)
else :
    print("error")