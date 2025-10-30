old_word = "donkey"
new_word = "######"


with open("donkey_file.txt", "r") as f:
    data = f.read()
data = data.replace(old_word, new_word)

with open("donkey_file.txt", "w") as f:
    f.write(data)
