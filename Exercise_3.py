
year = int(input("Please insert the year you want to check: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("YES")
else:
    print("NO")


