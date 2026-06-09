import matplotlib.pyplot as plt
import numpy as np


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


def plot_scattered(original_data, sorted_data):
    '''
    Plots two arrays of the same length (original and sorted) on a scatter plot for visual comparison.
    Note: Scatter plot is used since there aren't values between discrete indices.
    '''
    assert len(original_data) == len(sorted_data)

    x = np.arange(len(original_data))
    plt.scatter(x, original_data, marker='o', label='Original', alpha=0.7)
    plt.scatter(x, sorted_data, marker='o', label='Sorted', alpha=0.7)

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.title("Original and Sorted Values")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.xticks(range(len(original_data)))
    plt.legend()
    plt.show()


if __name__ == "__main__":
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    original = data.copy()
    merge_sort(data)
    plot_scattered(original, data)
