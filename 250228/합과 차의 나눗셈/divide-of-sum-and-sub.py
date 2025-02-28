user = input()
arr = user.split()

a = int(arr[0])
b = int(arr[1])
c = ((a+b) / (a-b))

if 1 <= b < a <= 1000 :
    print(f"{c:.2f}")
else :
    print("error")