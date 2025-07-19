import Foundation

let a = Double(readLine()!)!
let b = Double(readLine()!)!

if (1 <= a && a <= 100) && (1 <= b && b <= 100) {
    print(String(format: "%.2f", a + b))
}