def binary_search(array, target):
    """
    Perform binary search on a sorted array to find the target value.
    
    Parameters:
        array (list): The sorted list of elements to search through.
        target (any): The value to search for in the array.

    Returns:
        int: The index of the target in the array, or -1 if not found.
    """
    # Initialize the search bounds
    left, right = 0, len(array) - 1
    
    while left <= right:
        # Calculate the middle index of the current search range
        mid = left + (right - left) // 2

        if array[mid] == target:
            # Target found at the middle index
            return mid
        elif array[mid] < target:
            # If target is greater, ignore the left half
            left = mid + 1
        else:
            # If target is smaller, ignore the right half
            right = mid - 1

    # Target is not in the array
    return -1


# Example usage
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
target_value = 7

result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}.")
else:
    print(f"Target {target_value} not found in the array.")
