# merge dictionares in one dictionary

# For two Dict
dict1 = {"Ali" : 5, "Ahmed" : 55}
dict2 = {"Usman" : 8, "Umer" : 78}

merged1 = dict1 | dict2
print(merged1)

# For Three Dict
dict1 = {"Ali" : 5, "Ahmed" : 55}
dict2 = {"Usman" : 8, "Umer" : 78}
dict3 = {"Harry" : 1098, "Hassan" : 89}

merged = dict1 | dict2 | dict3
print(merged)
