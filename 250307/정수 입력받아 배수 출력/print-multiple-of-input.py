N = int(input())

if 1 <= N <= 100 :
    for i in range(N, 6 * N, N) :
        print(i, end=" ")
else :
    print("error")