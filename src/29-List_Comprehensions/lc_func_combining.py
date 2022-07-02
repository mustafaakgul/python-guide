def cube(x):
    return x ** 3


if __name__ == '__main__':
    print(cube(3))

    cube = [cube(x) for x in range(5)]
    print(cube)