handle = open('mbox-short.txt')

for line in handle:
    line = line.rstrip()
    # print(line)
    
    if line.startswith('From:'):
        print(line)

    