# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def example(val):
    val = val + '4'
    val = val * 2
    return val

def strange(j):
    k = 0
    while j > 0:
        k = 10 * k + j % 10
        j = j // 10
    return k


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # print("foo" * 3)
    # print(2 ** 3)
    # print(example("jump"))
    # word = "positive"
    # print(word[:2])
    # print(strange(1230))
    print(type(3/4))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
