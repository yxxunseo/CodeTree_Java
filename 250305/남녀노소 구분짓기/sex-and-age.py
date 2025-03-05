sex = int(input())
age = int(input())

if 1 <= age <= 100 :
    if sex == 0 :
        if age >= 19 :
            print("MAN")
        else :
            print("BOY")
    if sex == 1 :
        if age >= 19 :
            print("WOMAN")
        else :
            print("GIRL")
else :
    print("error")
