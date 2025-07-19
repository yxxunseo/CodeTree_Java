import Foundation

let a = Double(readLine()!)!
let b = Double(readLine()!)!
let c = Double(readLine()!)!

if (1 <= a && a <= 1000) && (1 <= b && b <= 1000) && (1 <= c && c <= 1000) {
    print(String(format: "%.3f", a))
    print(String(format: "%.3f", b))
    print(String(format: "%.3f", c))
}