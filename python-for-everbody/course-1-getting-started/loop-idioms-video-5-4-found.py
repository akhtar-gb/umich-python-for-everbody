found = False
x = int(input("Enter a integer: "))

print("Before loop", "value entered", x)
for value in [9, 41, 12, 3, 74, 15]:
    if value == x:
        found = True
print("After loop", "value entered found", found)