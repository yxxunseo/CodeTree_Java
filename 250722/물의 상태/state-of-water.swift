let n = Int(readLine()!)!

if (-200 <= n && n <= 200) {
    if (n < 0) {
        print("ice")
    }
    else if (n >= 100) {
        print("vapor")
    }
    else {
        print("water")
    }
}