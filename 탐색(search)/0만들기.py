import copy

def make_operator(array, n):
    if len(array) == n:
        operator_list.append(copy.deepcopy(array))
        return

    array.append(' ')
    make_operator(array, n)
    array.pop()

    array.append('+')
    make_operator(array, n)
    array.pop()

    array.append('-')
    make_operator(array, n)
    array.pop()


test_case = int(input())

for _ in range(test_case):

    n = int(input())

    integers = [i for i in range(1, n + 1)]
    operator_list = []

    make_operator([], n - 1)

    for operators in operator_list:
        string = ""

        for i in range(n - 1):
            string = string + str(integers[i]) + operators[i]
        string += str(integers[-1])

        if eval(string.replace(' ', '')) == 0:
            print(string)
    print()
