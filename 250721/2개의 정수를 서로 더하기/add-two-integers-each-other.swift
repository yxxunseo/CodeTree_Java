let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let a = input[0]
let b = input[1]

if (1 <= a && a <= 1000) && (1 <= a && a <= 1000) {
    print((b + a), (b + a + b))
}
