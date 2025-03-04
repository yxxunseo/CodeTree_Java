user = input()
arr = user.split()

a = int(arr[0])
b = int(arr[1])

if 1 <= a <= 10 and 1 <= b <= 10 :
    if a >= b :
        print(1)
    else :
        print(0)

    if a > b :
        print(1)
    else :
        print(0)
    
    if b >= a :
        print(1)
    else :
        print(0)

    if b > a :
        print(1)
    else :
        print(0)
else :
    print("error")