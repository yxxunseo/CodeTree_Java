var input = readLine()!.split(separator: " ").map { Int($0)! }
var a = input[0]
var b = input[1]
var temp = 0

if (1 <= a && a <= 100) && (1 <= b && b <= 100) {
    temp = a
    a = b
    b = temp
    print(a, b)
}
else {
    print("Error")
}