a = int(input("Please enter any integer number A: "))
b = int(input("Please enter any integer number B: "))
c = int(input("Please enter any integer number C: "))

if a == b == c:
    print("3")
elif a != b and b != c and c != a:
    print("0")
else:
    print("2")
