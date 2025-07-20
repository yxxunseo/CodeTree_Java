let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let w = input[0]
let h = input[1]

if (1 <= w) && (h <= 100) {
    print(w + 8)
    print(h * 3)
    print((w + 8) * (h * 3))
}