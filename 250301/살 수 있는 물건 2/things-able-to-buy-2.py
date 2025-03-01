N = int(input())

if 0 <= N <= 10000 :
    if N >= 3000 :
        print("book")
    elif 1000 <= N < 3000 :
        print("mask")
    elif 500 <= N < 1000 :
        print("pen")
    else :
        print("no")
else :
    print("error")