# You can use multiple context managers in a single "with" statement
# more cleanly useing the parenthesised context manager.

with (
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    
    data1 = f1.read()
    data2 = f2.read()

    print(data1, data2)

# We can also write it without parenthesis
with open('file1.txt') as f1, open('file2.txt') as f2:
    data1 = f1.read()
    data2 = f2.read()

    print(data1, data2)
