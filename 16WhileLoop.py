i = 0
while i < 10:
    print(i)
    i += 1

    while True:
        num = int(input("Enter Number: "))
        print(num)
        if num == 0:
            # Set flag to break the outer loop
            exit_outer_loop = True
            break

    if exit_outer_loop:
        break

print("Program has finished executing")
