text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
text = float(text[pos + 5:])
print(text)


# text = "X-DSPAM-Confidence:    0.8475"
# floatstart = text.rfind(' ') 
# print(floatstart)
# text = float(text[floatstart + 1:])
# print(text)

# zeropos = text.find('0')
# print('position of zero', zeropos)
# text = float(text[zeropos:])
# text = float(text[floatstart + 1:])
# print(text)
# print(text[23:])
