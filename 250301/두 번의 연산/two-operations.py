A = int(input())

if 1 <= A <= 100 :
    if A % 2 != 0 :
        A = A + 3
    if A % 3 == 0 :
        A = A / 3
    
    print(int(A))
else :
    print("Error")