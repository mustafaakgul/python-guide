def func_flatten(input_type):
    for i in input_type:
        if type(i) == list:
            func_flatten(i)
        else:
            flatten_list.append(i)
    return flatten_list

if __name__ == '__main__':
    global flatten_list
    flatten_list = []
    processing_array = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    print(processing_array)
    result = func_flatten(processing_array)
    print(result)