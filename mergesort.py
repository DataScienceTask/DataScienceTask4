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


def plot_bars(original_data, sorted_data):
    '''
    Plots two arrays of the same length (original and sorted) on bar plots for visual comparison.
    Note: Bar plot is used since there aren't values between discrete indices.
    '''
    assert len(original_data) == len(sorted_data)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    x = np.arange(len(original_data))
    ax[0].bar(x, original_data)
    ax[0].set_title("Original values")
    ax[1].bar(x, sorted_data)
    ax[1].set_title("Sorted values")

    for i in range(2):
        ax[i].spines['top'].set_visible(False)
        ax[i].spines['right'].set_visible(False)
        ax[i].set_xlabel("Index")
        ax[i].set_ylabel("Value")
        ax[i].set_xticks(range(len(original_data)))

    plt.show()


if __name__ == "__main__":
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    original = data.copy()
    merge_sort(data)
    plot_bars(original, data)
