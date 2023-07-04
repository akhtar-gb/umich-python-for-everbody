fname = input('Enter file name: ')

try:
    fhandle = open('romeo.txt')
except:
    print('Error file name typed cannot be opened: ', fname)
    quit()


romeolist = list()
for line in fhandle:
    line = line.rstrip()

    ls = list()
    ls = line.split()
    # print(ls)

    for word in ls:
        if word not in romeolist:
            romeolist.append(word)

romeolist.sort()
print(romeolist)

    
    

    

