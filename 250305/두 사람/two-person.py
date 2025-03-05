''' f = input()
s = input()

arr_f = f.split()
arr_s = s.split()

f_a = int(arr_f[0])
f_s = arr_f[1]

s_a = int(arr_s[0])
s_s = arr_s[1]

if 1 <= f_a <= 100 and 1 <= s_a <= 100 :
    if (f_a >= 19 or s_a >= 19) and (f_s == "M" or s_s == "M") :
        print(1)
    else :
        print(0)
else :
    print("error") '''

f = input()
s = input()

arr_f = f.split()
arr_s = s.split()

f_a = int(arr_f[0])
f_s = arr_f[1]

s_a = int(arr_s[0])
s_s = arr_s[1]

if (f_a >= 19 and f_s == "M") or (s_a >= 19 and s_s == "M"):
    print(1)
else:
    print(0)