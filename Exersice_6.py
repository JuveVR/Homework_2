a = int(input("Please enter any integer number A: "))
b = int(input("Please enter any integer number B: "))
c = int(input("Please enter any integer number C: "))

if a == b == c:
    print("3")
if a != b and b != c and c != a:
    print("0")
if (a == b and c != a) or (b == c and a != b) or (c == a and b != c):
    print("2")