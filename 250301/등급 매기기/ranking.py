N = int(input())

if 0 <= N <= 100 :
    if N >= 90 :
        print("A")
    elif 80 <= N < 90 :
        print("B")
    elif 70 <= N < 80 :
        print("C")
    elif 60 <= N < 70 :
        print("D")
    else :
        print("F")
else :
    print("error")