l = [12, 23, 43, 543, 65, 76]

index = 0
for item in l:
    print(f"The item at index number {index} is {item}.")
    index += 1

# This can be simplified using enumerate 
print("This is second one.")
for index, item in enumerate(l):
    print(f"The item at index number {index} is {item}.")