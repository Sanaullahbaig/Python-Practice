
try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

 # It will run when try runs, if try does not runs else will not run.
else:
    print("I'm inside else, the try is successful.") 