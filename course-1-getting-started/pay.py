hrs = input("Enter Hours:")
rate = input("Enter Pay Rate:")

try:
    h = float(hrs)
    r = float(rate)

except:
    print("Error, enter numeric values only") 
    quit()
    
if h <= 40.0:
	pay = h * r
	print(pay)
elif h > 40:
	pay = (40 * r) + ((h - 40) * r * 1.5)
print(pay)