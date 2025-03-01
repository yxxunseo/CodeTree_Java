user = input()
arr = user.split()

h = int(arr[0])
w = int(arr[1])

b = int((10000 * w) / (h * h))

if 1 <= h <= 1000 and 1 <= w <= 1000 :
    if b >= 25 :
        print(b)
        print("Obesity")
    else :
        print(b)
else : 
    print("error")