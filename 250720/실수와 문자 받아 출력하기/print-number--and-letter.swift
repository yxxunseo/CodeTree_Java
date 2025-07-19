import Foundation

let c = readLine()!
let a = Double(readLine()!)!
let b = Double(readLine()!)!

if (1 <= a && a <= 1000) && ((1 <= b && b <= 1000)) {
    print(c)
    print(String(format: "%.2f", a))
    print(String(format: "%.2f", b))
}