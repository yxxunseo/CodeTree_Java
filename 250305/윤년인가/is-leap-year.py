Y = int(input())

if 1 <= Y <= 2222 :
    if Y % 4 != 0 or (Y % 100 == 0 and Y % 400 != 0) :
        print("false")
    else :
        print("true")
else :
    print("error")
