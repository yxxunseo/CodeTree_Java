a, n = input().split()
a, n = int(a), int(n)

if 1 <= a <= 10 and 1 <= n <= 10 :
    for i in range(a + n, (a + n * n) + 1 , n) :
        print(i)

else :
    print("error")