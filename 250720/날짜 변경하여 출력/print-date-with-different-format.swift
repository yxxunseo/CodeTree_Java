let input = readLine()!.split(separator: ".").map { Int(String($0))! }
let y = input[0]
let m = input[1]
let d = input[2]

if (1 <= y && y <= 2021) && (1 <= m && m <= 12) && (1 <= d && d <= 28) {
    print("\(m)-\(d)-\(y)")
}