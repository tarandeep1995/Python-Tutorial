# List are mutable means we can modify the list but string are not
list1 = [22, 4, 12, 62, 83,200,234]
print(type(list1))
print(list1)

# list1.remove("TARAN")   # It MODIFY the existing list without creating a new one
# print(list1)

# print(list1.count(62))    # COUNT number of 62 in the list

# list1.sort()              # SORT the list
# print(list1)

# list1.pop()               # POP the last element from the list
# print(list1)

# list1.append(78)          # ADD the element at the end of the list
# print(list1)

# list1.clear()               # CLEAR the list
# print(list1)

# list1.extend([23, 45, 24, 564, 64])  # add elements at the end of the existing list
# print(list1)
#
# list1.reverse()               # REVERSE the list
# print(list1)
#
# print(list1.index(564))       # tell the INDEX of the value
print(list1[0:4])

