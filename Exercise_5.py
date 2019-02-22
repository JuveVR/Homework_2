a = float(input("Please enter number A"))
b = float(input("Please enter number B"))
c = float(input("Please enter numcber C"))

l = sorted([a, b, c])
print(a)
print(b)
print(c)

print(l)
a,b,c = l[-3],l[-2],l[-1]

if a <= b <= c:
    print("This is new A " + str(a))
    print("This is new B " + str(b))
    print("This is new C " + str(c))
else:
    print("You are stupid student")

