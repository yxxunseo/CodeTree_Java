import Foundation

let input = readLine()!.split(separator: " ").map {Int(String($0))! }
let h = input[0]
let w = input[1]

if (1 <= h && h <= 1000) && (1 <= w && w <= 1000) {
    let b = ((10000 * w) / (h * h))
    print(b)
    if b >= 25 {
        print("Obesity")
    }
}