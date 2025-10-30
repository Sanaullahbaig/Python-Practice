words = ["donkey", "farm", "field"]


with open("multi_words_file.txt", "r") as f:
    data = f.read()

for word in words:

    data = data.replace(word, "*" * len(word))

with open("multi_words_file.txt", "w") as f:
    f.write(data)
