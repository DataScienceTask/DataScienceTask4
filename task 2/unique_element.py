def find_unique(arr):
    """
    Returns the element that occurs exactly once while all others occur twice.
    According to task 1b, this method would not need to check for unsupported frequencies of elements.
    But since task 1a asks us to implement test functions for invalid inputs, we check them anyway.
    """
    if not isinstance(arr, list):
        raise ValueError("Input must be a non-empty list")

    frequencies = {}
    for value in arr:
        if not isinstance(value, int):
            raise ValueError("Array must only include integers")
        if value in frequencies:
            frequencies[value] += 1
            if frequencies[value] > 2:
                raise ValueError("Array contains an element more than twice")
        else:
            frequencies[value] = 1

    print(len(frequencies), len(arr), frequencies, arr)
    if len(frequencies) != (len(arr) + 1) / 2:
        raise ValueError("Array must contain every integer exactly twice except for one unique element")

    for value, frequency in frequencies.items():
        if frequency == 1:
            return value
