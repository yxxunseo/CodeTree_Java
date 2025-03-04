user = input()
arr = user.split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if 1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100 :
    if a <= b and a <= c:
            print("1", end=" ")
    else :
        print("0", end=" ")
    if a == b and b == c :
        print("1")
    else :
        print("0")

else :
    print("error")