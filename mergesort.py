import matplotlib.pyplot as plt


def merge_sort(arr):
    """
    Sorts arr recursively using merge sort.
    """
    if len(arr) < 2:
        return

    # split list into halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # sort halves
    merge_sort(left)
    merge_sort(right)


    left_i = right_i = total_i = 0

    # merge while both lists have elements
    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            arr[total_i] = left[left_i]
            left_i += 1
        else:
            arr[total_i] = right[right_i]
            right_i += 1
        total_i += 1

    # merge remaining left elements
    while left_i < len(left):
        arr[total_i] = left[left_i]
        left_i += 1
        total_i += 1

    # merge remaining right elements
    while right_i < len(right):
        arr[total_i] = right[right_i]
        right_i += 1
        total_i += 1


def plot_linear(arr):
    """
    Plots arr on a linear scale.
    """
    plt.plot(arr)
    plt.show()


if __name__ == "__main__":
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    plot_linear(data)
    merge_sort(data)
    plot_linear(data)
