a = input()
b = input()

arr_a = a.split()
arr_b = b.split()

a_m = int(arr_a[0])
a_e = int(arr_a[1])

b_m = int(arr_b[0])
b_e = int(arr_b[1])

if 1 <= a_m <= 100 and 1 <= a_e <= 100 and 1 <= b_m <= 100 and 1 <= b_e <= 100 :
    if a_m > b_m and a_e > b_e :
        print(1)
    else :
        print(0)
else :
    print("error")