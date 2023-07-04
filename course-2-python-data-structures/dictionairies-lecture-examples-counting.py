counts = dict()
names = ['csev', 'cwen', 'zqian', 'cwen', 'cwen', 'zqian', 'cwen', 'csev', 'cwen', 'zqian', 'cwen']

# counting using a counter
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# counting using the get() method
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

