let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let a = input[0]
let b = input[1]
let c = input[2]


if (1 <= a && a <= 100) && (1 <= b && b <= 100) && (1 <= c && c <= 100) {
    let sum = a + b + c
    let avg = (a + b + c) / 3
    print(sum)
    print(avg)
    print(sum - avg)
}