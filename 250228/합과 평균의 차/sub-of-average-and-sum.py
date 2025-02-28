user = input()
arr = user.split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if 1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100 :
    print(a + b + c)
    print(int((a + b +c) / 3))
    print(int((a + b + c) - ((a + b + c) / 3)))
else :
    print("error")