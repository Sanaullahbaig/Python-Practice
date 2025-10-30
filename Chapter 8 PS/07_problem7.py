def remove(l, word):
    n = []
    for item in l:
        if not (item == word):
            # strip remove the words from side strip remove from both side 
            # lstrip remove from left side and rstrip remove from right side 
            n.append(item.strip(word))
    return n
l = ["Ali", "Haider Ali", "Usman Ali", "Ahmed", "Hassan"]
print(remove(l, "Ali"))

