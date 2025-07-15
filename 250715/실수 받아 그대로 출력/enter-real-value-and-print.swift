import Foundation

var N = Double(readLine()!)!

if 0 <= N && N <= 50 {
    print(String(format: "%.2f", N))
}
else {
    print("Error")
}