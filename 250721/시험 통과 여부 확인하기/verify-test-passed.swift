let n = Int(readLine()!)!

if (0 <= n && n <= 100) {
    if (n >= 80) {
        print("pass")
    } 
    else {
        print("\(80 - n) more score")
    }
}