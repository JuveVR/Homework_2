a = float(input("Please enter the length of A"))
b = float(input("Please enter the length of B"))
c = float(input("Please enter the length of C"))

if a < b + c and b < c + a and c < b + a:
    print("Yes")
else:
    print("No")

