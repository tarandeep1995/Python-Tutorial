# MatchCaseStatement is a new edition to the python 3.10 onwards

# a = int(input("Enter the number: "))
#
# match a:
#     case 1:
#         print("Case is 1")
#     case 2:
#         print("Case is 2")
#     case 33:
#         print("Case is 33")
#     case 43:
#         print("Case is 43")
#     case _:  # it is DEFAULT case
#         print("No match Found")

# Write a python program to print table of a number which lies between 1 and 10
def print_table(number):
    if number < 1 or number > 10:
        print("Number must be between 1 and 10")
        return

    tables = {
        1: lambda: [print(f"{1} x {i} = {1 * i}") for i in range(1, 11)],
        2: lambda: [print(f"{2} x {i} = {2 * i}") for i in range(1, 11)],
        3: lambda: [print(f"{3} x {i} = {3 * i}") for i in range(1, 11)],
        4: lambda: [print(f"{4} x {i} = {4 * i}") for i in range(1, 11)],
        5: lambda: [print(f"{5} x {i} = {5 * i}") for i in range(1, 11)],
        6: lambda: [print(f"{6} x {i} = {6 * i}") for i in range(1, 11)],
        7: lambda: [print(f"{7} x {i} = {7 * i}") for i in range(1, 11)],
        8: lambda: [print(f"{8} x {i} = {8 * i}") for i in range(1, 11)],
        9: lambda: [print(f"{9} x {i} = {9 * i}") for i in range(1, 11)],
        10: lambda: [print(f"{10} x {i} = {10 * i}") for i in range(1, 11)]
    }

    tables[number]()


# Example usage
num = int(input("Enter a number between 1 and 10: "))
print_table(num)
