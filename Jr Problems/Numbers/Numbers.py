'''6. The Numbers

Create a Python function named "get_integers" that accepts a
list of mixed non-negative integers and strings.
The function should filter and return only the integers in the same order
as they appear in the original list.'''

list = [10, 5, 'dos', 1, 'ocho', 40, 'casita', 5, 32, 7, '6']

def get_integers(list):
    list2 = []
    for v in list:
        if type(v) == int:
            list2.append(v)
    print(list2)
    return list2

list2 = get_integers(list)


