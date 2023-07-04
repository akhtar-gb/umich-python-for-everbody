fname = input("Enter file name: ")

# if len(fname) < 1:
#     fname = "mbox-short.txt"

# fh = open(fname)
# count = 0

try:
    fhandle = open('mbox-short.txt')
except:
    print('Error file name typed cannot be opened: ', fname)
    quit()

count = 0
for line in fhandle:
    line = line.rstrip()
    # print(line)

    ls = list()
    if not line.startswith('From '):
        continue
    ls = line.split()
    
    print(ls)
    # print(ls[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
