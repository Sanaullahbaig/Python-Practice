def inches_to_cm(inch):
    cm = inches * 2.54
    return cm

inches = int(input("Enter inches: "))

print(f"{inches} inches are equal to {inches_to_cm(inches)} cm")