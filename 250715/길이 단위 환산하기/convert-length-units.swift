import Foundation

var N = Double(readLine()!)!

if 0 <= N && N <= 100 {
    print(String(format: "%.1f", N * 30.48))
}
else {
    print("Error")
}