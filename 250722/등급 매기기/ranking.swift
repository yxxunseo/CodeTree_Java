let n = Int(readLine()!)!

if 0 <= n && n <= 100 {
    if n >= 90 {
        print("A")
    }
    else if n >= 80 {
        print("B")
    }
    else if n >= 70 {
        print("C")
    }
    else if n >= 60 {
        print("D")
    }
    else {
        print("F")
    }
}