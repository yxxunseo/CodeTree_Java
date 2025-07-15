import Foundation

var a = Double(readLine()!)!

if 1 <= a && a <= 100 {
    print(String(format: "%.2f", a + 1.5))
}
else {
    print("Error")
}