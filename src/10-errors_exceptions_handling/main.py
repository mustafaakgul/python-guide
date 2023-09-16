import sys

# Three elements of traceback : a file path, line number and exception
# except Exception is unhelpful cuz it can hide what the real problem is

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
        # f = open('myfile.txt')  # FileNotFoundError can be occur cuz use exception handling try except
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

# Exception block can be useful seperately for each case because you can use handling block for each case.

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()

# An unuseful way of handling this error would be to catch all possible exceptions to prevent a traceback.
# To understand why catching all exceptions is problematic, try it by updating the main() function:
def main():
    try:
        configuration = open('config.txt')
    except Exception as err:
        print("Couldn't find the config.txt file!", err)

#Let's fix this piece of code to address all these frustrations. Revert to catching FileNotFoundError,
# and then add another except block to catch PermissionError:
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")

#When errors are of a similar nature and there's no need to handle them individually, you can group the exceptions
# together as one by using parentheses in the except line. For example, if the navigation system is under heavy loads
# and the file system becomes too busy, it makes sense to catch BlockingIOError and TimeOutError together:
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


#In this case, as err means that err becomes a variable with the exception object as a value. It then uses this
# value to print the error message that's associated with the exception. Another reason to use this technique is
# to access attributes of the error directly. For example, if you're catching a more generic OSError exception,
# which is the parent exception of both FilenotFoundError and PermissionError, you can tell them apart by the .errno
# attribute:
try:
    open("config.txt")
except OSError as err:
    if err.errno == 2:
       print("Couldn't find the config.txt file!")
    elif err.errno == 13:
       print("Found config.txt but couldn't read it")


try:
    open("config.txt")
except OSError as err:
    if err.errno == 2:
       print("Couldn't find the config.txt file!")
    elif err.errno == 13:
       print("Found config.txt but couldn't read it")
    else:
        print("Another error happened:", err.errno)
finally:
    print("This always executes")