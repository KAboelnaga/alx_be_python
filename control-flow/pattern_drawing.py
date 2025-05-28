size = input("Enter the size of the pattern:")
if size <= 0:
    print("integer must be positive")
else:
    i = 0
    while i < size:
        j = 0
        while j < size:
            print("*",end="")
            j += 1
        print("")
        i += 1
