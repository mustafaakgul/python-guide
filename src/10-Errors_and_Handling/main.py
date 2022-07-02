import sys

# Handling Exceptions
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Error
# print(a) => NameError
# int('1a2') => ValueError
# print(10/0) => ZeroDivisionError
# print('denem'e) => SyntaxError
# 10 * (1/0) => ZeroDivisionError: division by zero
# 4 + spam*3 => NameError: name 'spam' is not defined
# '2' + 2 => TypeError: can only concatenate str (not "int") to str
while 1:
    x = input('Enter a number: ')
    try:
        # f = open('myfile.txt')
        # s = f.readline()
        # i = int(s.strip())
        print(10/0)
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError as err:
        print(f"Could not convert data to an integer. {err=}, {type(err)=}.")
    except BaseException as err: # Exception as err:
        print(f"Unexpected {err=}, {type(err)=}, {err.args=}")
        # The raise statement allows the programmer to force a specified exception to occur.
        raise
        #raise err
        #raise Exception("This is an exception")

# try:
#     linux_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print('Cleaning up, irrespective of any exceptions.')