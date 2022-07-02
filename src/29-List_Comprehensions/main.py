if __name__ == '__main__':
    squares = []
    for i in range(1, 11):
        squares.append(i ** 2)
    print(squares)

    squares_list_comprehension = [i ** 2 for i in range(1, 11)]
    print(squares_list_comprehension)