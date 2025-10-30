marks = {
    "Harry" : 100,
    "Ali" : 56,
    "Hassan" : 89,
    "list" : [1, 2, 3],
    0 : "Ahmed"
}


# print all items
print(marks.items())
# print only keys
print(marks.keys())
# print only values
print(marks.values())
# update the value and add the value
marks.update({"Ali" : 76, "Ahmed": 49})
# get method returns the value of specific key, if value does not exist it will return none
print(marks.get("Ali"))
print(marks)

# .clear for clearing the dictionary it will remove all items 