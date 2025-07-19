let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let c = Int(readLine()!)!

let a = input[0]
let b = input[1]

if (1 <= a && a <= 100) && (1 <= b && b <= 100) && (1 <= c && c <= 100) {
    print(a, b, c)
}