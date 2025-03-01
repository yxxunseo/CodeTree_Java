a = float(input())

if 0 <= a <= 5 :
    if a >= 1.0 :
        print("High")
    elif 0.5 <= a < 1.0 :
        print("Middle")
    else : 
        print("Low")
else :
    print("error")