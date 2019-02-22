#2.1
katet1 = 3
katet2 = 4

gipotenuza = (katet1**2 + katet2**2)**0.5

print(gipotenuza)

# 2.2
print(56 // 10)

# 2.3
c = str(156)
summa = 0
for i in c:
    summa += int(i)
print(summa)
#second way
d = 344
d1 = d % 10
d = d // 10
d2 = d % 10
d = d // 10
d3 = d % 10

sum = d1 + d2 + d3
print(sum)

#2.4
n = input("Please enter any whole number: ")
integ = int(n) # Converts input string to integer value.
#I know that my code will fail here if user inputs string or float,
# but I dont know how to solve this despite exception handling
next_even = 0
if integ % 2 == 1:
    next_even = integ + 1
elif integ % 2 == 0:
    next_even = integ + 2
else:
    print("You entered wrong number")

print(next_even)

#2.5
x = float(input("Please enter any number: "))
print(str(x%1)[2:])
# or in another way:
print(x - int(x))

#2.6
x1 = float(input("Please enter any number: "))
print(str(x1%1)[2])
