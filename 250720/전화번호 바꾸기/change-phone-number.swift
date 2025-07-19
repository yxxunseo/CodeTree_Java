let input = readLine()!.split(separator: "-").map { Int(String($0))! }
let n = input[0]
let f = input[1]
let s = input[2]

print("010-\(s)-\(f)")