time = input()
arr = time.split(":")

h = int(arr[0])
m = int(arr[1])

h = h + 1

h = str(h)
m = str(m)

print(h + ":" + m)