user = input()
arr = user.split()

a = int(arr[0])
b = int(arr[1])
c = int(a // b)
d = int(a % b)

if (1 <= a <= 100) & (1 <= b <= 100) :
    print(f"{c}...{d}")
else :
    print("error")