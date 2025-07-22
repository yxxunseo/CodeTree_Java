let n = Int(readLine()!)!

if 0 <= n && n <= 10000 {
    if n >= 3000 {
        print("book")
    }
    else if n >= 1000 {
        print("mask")
    }
    else if n >= 500 {
        print("pen")
    }
    else {
        print("no")
    }
}