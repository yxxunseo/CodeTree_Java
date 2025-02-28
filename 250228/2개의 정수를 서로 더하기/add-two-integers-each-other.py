user = input()
arr = user.split()

a = int(arr[0])
b = int(arr[1])

a += b
b += a

if 1 <= a <= 1000 and 1 <= b <= 1000 :
    print(a, b)
else :
    print("error")
