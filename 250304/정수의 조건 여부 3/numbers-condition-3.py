a = int(input())

if 1 <= a <= 1000 :
    if a % 13 == 0 or a % 19 == 0 :
        print("True")
    else :
        print("False")
else :
    print("error")