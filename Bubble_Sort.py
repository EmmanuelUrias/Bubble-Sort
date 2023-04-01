list = [2, 34, 43, 1, 5, 3]


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        swapped = False
        print(f'Iteration: {i}')
        print(lst)
        for j in range(len(lst) - 1):
            print(f'Comparing {lst[j]} and {lst[j + 1]}')
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            return

    return lst


bubble_sort(list)
