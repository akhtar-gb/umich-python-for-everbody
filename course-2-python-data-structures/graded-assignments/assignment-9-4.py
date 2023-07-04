# name = input('Enter file name: ')

# if len(name) < 1:
#     name = 'mbox-short.txt'

# handle = open(name)

# fromlines = list()
# emails = list()
# for lines in handle:
#     lines = lines.rstrip()
#     # print(lines)

#     if not lines.startswith('From '):
#         continue
#     # print(lines)

#     fromlines = lines.split()
#     # print(fromlines)
#     email = fromlines[1]
#     emails.append(email)
#     # print(email)
# # print(emails)

# dictionary = dict()
# for email in emails:
#     dictionary[email] = dictionary.get(email, 0) + 1
# # print(dictionary)

# emailaddress = None
# emailcount = None
# for key,value in dictionary.items():
#     if emailcount is None or value > emailcount:
#         emailaddress = key
#         emailcount = value
# print(emailaddress, emailcount)



# ----------------------------------------------------------------------------------------------------------------------
name = input('Enter file name: ')

if len(name) < 1:
    name = 'mbox-short.txt'

handle = open(name)


dictionary = dict()
emailaddress = None
for lines in handle:
    lines = lines.rstrip()
    # print(lines)

    if not lines.startswith('From '):
        continue
    # print(lines)

    fromlines = lines.split()
    # print(fromlines)
    email = fromlines[1]
    # print(email)
    dictionary[email] = dictionary.get(email, 0) + 1
    print(dictionary)

    if dictionary[email] > dictionary.get(emailaddress, 0):
        emailaddress = email
        # print(emailaddress)
        
print(emailaddress, dictionary[emailaddress])