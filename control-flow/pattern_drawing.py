while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size > 0:
            break
        else:
            print("Please enter a **positive** integer.")
    except ValueError:
        print("Invalid input. Please enter a **number**.")
i = 0
while i < size:
    j = 0
    while j < size:
        print("*",end="")
        j += 1
    print("")
    i += 1
