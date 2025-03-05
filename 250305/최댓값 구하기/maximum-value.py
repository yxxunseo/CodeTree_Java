user = input()
arr = user.split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if -100 <= a <= 100 and -100 <= b <= 100 and -100 <= c <= 100 :
    if a >= b :
        if a >= c :
            print(a)
        else :
            print(c)
    else :
        if b >= c :
            print(b)
        else : 
            print(c)
else :
    print("error")