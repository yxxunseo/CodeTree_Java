user = int(input())

if 0 <= user <= 100 :
    result = "pass" if user == 100 else "failure"
    print(result)
else :
    print("error")