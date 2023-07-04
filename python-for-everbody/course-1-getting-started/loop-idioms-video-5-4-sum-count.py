count = 0
sum = 0
print("Before loop", "count", count, "sum", sum)
for key in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + key
    print("count", count, "sum", sum)
print("After the loop", "count", count, "sum", sum, float(sum / count))