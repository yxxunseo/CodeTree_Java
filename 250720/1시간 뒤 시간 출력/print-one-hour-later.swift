let input = readLine()!.split(separator: ":").map { Int(String($0))! }

let h = input[0]
let m = input[1]

if (1 <= h && h <= 22) && (0 <= m && m < 60) {
    print("\(h+1):\(m)")
}