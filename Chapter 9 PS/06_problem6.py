with open("log.txt") as f:
    data = f.read()

if "python" in data:
    print("Yes it contain the word\"python\"")
else:
    print("No it does not contain the word\"python\"")
