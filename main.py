def print_average(arr):
    print(sum(arr) / max(1, len(arr)))


def print_statistics(arr):
    print(len(arr))
    print_average(arr)
    if not arr:
        arr = [0]
    print(min(arr))
    print(max(arr))
    arr.sort()
    print(arr[len(arr) // 2] / 2 + arr[(len(arr) - 1) // 2] / 2)


print_statistics([1, 2])

