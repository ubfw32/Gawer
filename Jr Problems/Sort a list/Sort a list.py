list = [35, 67, 3, 48, 11, 13, 8, 66, 22]
order = ['asc', 'desc', 'none']


def sort(list, order):

    print('Choose a term to view the list: \nasc \ndesc \nnone')
    ans = input()
    if ans == order[0]:
        l1 = list.sort()
        print(list)
        return l1

    elif ans == order[1]:
        l1 = list.sort(reverse=True)
        print(list)
        return l1

    elif ans == order[2]:
        print(list)
        return list

    else:
        print('Invalid answer')
        sort(list, order)


sort(list, order)
