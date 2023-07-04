largest = None
smallest = None

while True:

    num = input('Enter a number: ')
    if num == 'done':
        break

    try:
        num = int(num)

    except:
        print('Invalid input')
        continue

    if smallest is None or largest is None:
        largest = num
        smallest = num
    else:
        largest = max(num, largest)
        smallest = min(num, smallest)

print('Maximum is', largest)
print('Minimum is', smallest)


# def minmax(list):
#     for item in list:
