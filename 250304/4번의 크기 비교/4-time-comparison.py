a = int(input())
user = input()
arr = user.split()
b = int(arr[0])
c = int(arr[1])
d = int(arr[2])
e = int(arr[3])

if 1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100 and 1 <= d <= 100 and 1 <= e <= 100 :
    if a > b :
        print(1)
    else :
        print(0)
    
    if a > c :
        print(1)
    else :
        print(0)

    if a > d :
        print(1)
    else :
        print(0)

    if a > e :
        print(1)
    else :
        print(0)

else :
    print("error")