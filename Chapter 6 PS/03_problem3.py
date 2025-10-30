phase1 = "Make a lot of money"
phase2 = "Buy now"
phase3 = "subscribe this"
phase4 = "click this"

message = input("Enter your comment: ")

if ((phase1 in message) or (phase2 in message) or (phase3 in message) or (phase4 in message)):
    print("This is a spam comment.")
else:
    print("This is not a spam Comment.")