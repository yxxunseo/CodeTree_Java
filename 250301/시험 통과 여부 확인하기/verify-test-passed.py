N = int(input())

if 0 <= N <= 100 :
    if N >= 80 :
        print("pass")
    else :
        print(f"{80 - N} more score")
else :
    print("error")