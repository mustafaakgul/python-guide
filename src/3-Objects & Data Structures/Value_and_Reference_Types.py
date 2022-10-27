if __name__ == '__main__':
    # Value Types Stored in Different Locations in Memory
    # strings, numbers ...
    x = 5
    y = 25
    print(x, y) # 5 25

    x = y
    print(x, y) # 25 25

    # Reference Types
    a = ["apple", "banana", "cherry"]
    print(id(a))
    b = ["apple", "banana", "cherry"]
    print(id(b))

    a = b
    print(id(a))
    print(id(b))
    # Now a and b are the same object at same location in memory
    a[0] = "kiwi"
    print(b)