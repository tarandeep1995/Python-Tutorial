def greetHello(name, ending):
    print("Hello", name)
    print(ending)


print("Executing Function")
greetHello("Taran", "Thank you")
print("Done")


# If you want to use the VARIABLE inside the STRING then we use f"" string

def letterGenerator(name, date):
    st = f"Hi Mam,\n This is {name}, I am not abe to attend the school on {date}."
    print(st)


def average(a, b):
    return (a + b) / 2


letterGenerator("Taran", "25 Aug")
letterGenerator("RONAK", "24 JULY")


print(average(23, 41))
