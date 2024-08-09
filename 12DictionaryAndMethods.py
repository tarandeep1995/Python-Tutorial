# Dictionary is mutable
dict1 = {}
a = {}
print(dict1, type(dict1))
print(a, type(a))

dict1 = {"good": "Somthing pleasant", "Fetch": "to bring", "1": "The number 1"}
print(dict1["good"])

marks = {"Harshit": 34, "Taran": 80, "Harry": 90, "Harshita": 74, "Karan": 56, "Ronak": 68}  # key:value pair
print(marks["Taran"])          # we can fetch the value using the key

print(marks["Harshita"])       # we can fetch the value using the key

marks["Priyanka"] = 34         # Added Priyanka in the list
print(marks)
print(marks.get("Priyanka"))   # get method basically save you from the error if there is no key available

print(marks.keys())            # give key of the dictionary
print(marks.values())          # give value of the dictionary
print(marks.items())           # give tuples of the dictionary