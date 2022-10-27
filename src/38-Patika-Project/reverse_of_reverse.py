def func_reverse(line):
    fully_reverse_list = []
    for i in line:
        if type(i) == list:
            #print("list", i)
            #print("rev", type(i))
            fully_reverse_list.append(list(reversed(i)))
            #print(fully_reverse_list)
    fully_reverse_list.reverse()
    #print(fully_reverse_list)
    return fully_reverse_list

if __name__ == '__main__':
    array_of_array = [[1, 2], [3, 4], [5, 6, 7]]
    print(array_of_array)
    result = func_reverse(array_of_array)
    print(result)