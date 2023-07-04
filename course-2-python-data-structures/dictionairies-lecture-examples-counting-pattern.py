counts = dict()
print("Enter your text:")
line = input('')

words = line.split()

# print(' ')
# print('Words list:', words)

# print('')
# print('Counting key value pairs in the dictionary...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
# print('Counts', counts)
# print(' ')

for key in counts:
    print(key, counts[key])

print('----------------------------------------------------------------')
print(list(counts))
print('----------------------------------------------------------------')
print(list(counts.keys()))
print('----------------------------------------------------------------')
print(list(counts.values()))
print('----------------------------------------------------------------')
print(list(counts.items()))