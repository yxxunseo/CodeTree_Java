f = input()
s = input()
t = input()

arr1 = f.split()
arr2 = s.split()
arr3 = t.split()

f_s = arr1[0]
f_f = int(arr1[1])

s_s = arr2[0]
s_f = int(arr2[1])

t_s = arr3[0]
t_f = int(arr3[1])

a = 0


if f_s == "Y" and f_f >= 37 :
    a += 1
if s_s == "Y" and s_f >= 37 :
    a += 1
if t_s == "Y" and t_f >= 37 :
    a += 1

if a >= 2 :
    print("E")
else :
    print("N") 
