a = int(input())

if 1 <= a <= 100 :
    if a % 2 == 0 :
        a = a / 2
    if a % 2 != 0 :
        a = (a + 1) / 2

    print(int(a))
else :
    print("error")
    