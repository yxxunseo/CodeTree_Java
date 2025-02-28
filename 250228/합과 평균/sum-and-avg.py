user = input()
arr = user.split()

a = int(arr[0])
b = int(arr[1])

if 1 <= a <= 100 and 1 <= b <= 100 :
    print(a+b, (a+b) / 2)