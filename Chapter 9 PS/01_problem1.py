with open("file_1.txt") as f:
    
    data = f.read()
    data = data.lower()
    count_twnikle = data.count("twinkle")
    if "twinkle" in data:
        print("Yes it has the word \"Twinkle\".")
        print(f"Your poem contain {count_twnikle} Twinkles!")
    else: 
        print("It does not contain the word \"Twinkle\".")

