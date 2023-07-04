#Use words.txt as the file name
fname = input("Enter file name: ")

try:
    fhandle = open('words.txt')
    # print(fhandle)
except:
    print('File cannot be opened', fname)
    quit()

for line in fhandle:
    line = line.rstrip()
    print(line.upper())