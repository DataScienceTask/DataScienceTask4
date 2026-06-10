def find_unique(arr):
    """
    Returns the element that occurs exactly once while all others occur twice.
    According to the task, this method does not need to check for unsupported frequencies of elements.
    """
    frequencies = {}
    for value in arr:
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1

    for value, frequency in frequencies.items():
        if frequency == 1:
            return value
