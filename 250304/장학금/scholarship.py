user = input()
arr = user.split()

m = int(arr[0])
l = int(arr[1])

if 0 <= m <= 100 and 0 <= l <= 100 :
    if m >= 90 :
        if l >= 95 :
            print("100000")
        elif l >= 90 :
            print("50000")
        else :
            print("0")
    else :
        print("0")
else :
    print("error")