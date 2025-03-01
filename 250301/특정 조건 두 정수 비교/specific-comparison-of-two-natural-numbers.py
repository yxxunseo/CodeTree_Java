user = input()
arr = user.split()

a = int(arr[0])
b = int(arr[1])

if 1 <= a <= 100 and 1 <= b <= 100 :
    print("1" if a < b else "0", 1 if a == b else "0")
else :
    print("error")