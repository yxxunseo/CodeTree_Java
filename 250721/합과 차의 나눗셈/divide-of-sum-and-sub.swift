import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let a = input[0]
let b = input[1]

if (1 <= b && b <= a && a <= 1000) {
    print(String(format: "%.2f", Double(a + b) /  Double(a - b)))
}