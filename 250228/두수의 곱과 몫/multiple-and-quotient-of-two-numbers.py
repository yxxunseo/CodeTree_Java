user = input()
arr = user.split()

a = int(arr[0])
b = int(arr[1])
c = a * b
d = int(a / b)

if 1 <= b <= a <= 500 :
    print(f"{a} * {b} = {c}")
    print(f"{a} / {b} = {d}")
else :
    print("error")
