a, b, c = input().split()

a, b, c = int(a), int(b), int(c)

if -100 <= a <= 100 and -100 <= b <= 100 and -100 <= c <= 100 and a != b and a!= c and b != c:
    print(sorted([a,b,c])[1])
else :
    print("error")