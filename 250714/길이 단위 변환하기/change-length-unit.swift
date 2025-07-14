import Foundation
var ft = 30.48
var mi = 160934

var r_ft = ft * 9.2
var r_mi = Double(mi) * 1.3

print(String(format: "9.2ft = %.1fcm", r_ft))
print("1.3mi = \(r_mi)cm")