A = int(input())

if 1 <= A <= 100 :
    if A % 3 == 0 :
        print("YES")
    else :
        print("NO")
    if A % 5 == 0 :
        print("YES")
    else :
        print("NO")
else :
    print("error")