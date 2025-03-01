user = input()
arr = user.split()

a = int(arr[0])
b = int(arr[1])

if 1 <= a <= 100 and 1 <= b <= 100 :
    if a % 2 == 0 :
        print("even")
    else :
        print("odd")

    if b % 2 == 0 :
        print("even")
    else :
        print("odd")
else :
    print("error")