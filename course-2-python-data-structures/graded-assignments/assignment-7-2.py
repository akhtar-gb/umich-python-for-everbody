# Use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')

try:
    fhandle = open('mbox-short.txt')
    # print(fhandle)
except:
    print('File cannot be loaded: ', fname)
    quit()

count = 0
total = 0
for line in fhandle:
    if not ('X-DSPAM-Confidence:') in line:
        continue
    # print(line)
    conflevel = float((line[20:]))
    # print(conflevel)
    total = total + conflevel
    count = count + 1
    # print('count: ' + str(count) + ' spam conf level: ' + str(conflevel) + ' running total: ' + str(total))

# print(count)
# print(total)
average = total / count
print('Average spam confidence:', average)







