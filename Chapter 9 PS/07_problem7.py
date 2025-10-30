with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"Yes it contain the word \"python\" in line no: {lineno}")
        break
    lineno += 1
else:
    print("No it does not contain the word \"python\"")
