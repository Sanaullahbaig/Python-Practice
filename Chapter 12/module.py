def myFun():
    print("Hello World!")



if (__name__ == "__main__"):
    # if this code is directly executed by running the file its present in 
    print("We are directly running this code.")
    myFun()
    print(__name__)  # if we run this file it will print __main__

# When we run this in other file it will print nothing 