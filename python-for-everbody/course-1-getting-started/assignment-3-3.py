# score = input("Enter score: ")

# try:
#     x = float(score)

# except:
#     if x < 0.0 or x > 1.0:
#         print("Error: score range is from 0.0 to 1.0")
#         quit()

score = float(input("Enter score: "))
x = float(score)

# except:
#     if x < 0.0 or x > 1.0:
#         print("Error: score range is from 0.0 to 1.0")
#         quit()

if x < 0.0 or x > 1.0:
    print("Error: score range is from 0.0 to 1.0")
    quit()
elif x >= 0.9:
    print("A")
elif x >= 0.8:
    print("B")
elif x >= 0.7:
    print("C")
elif x >= 0.6:
    print("D")
else:
    print("F")

