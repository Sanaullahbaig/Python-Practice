myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

# squaredList = []
# for i in myList:
#     squaredList.append(i*i)
# print(squaredList)
    
# we can simply do it by using comprehensions in one line

squaredList = [i*i for i in myList]
print(squaredList)