let a = Double(readLine()!)!

if (0 <= a && a <= 5) {
    if a >= 1.0 {
        print("High")
    }
    else if a >= 0.5 {
        print("Middle")
    }
    else {
        print("Low")
    }
}