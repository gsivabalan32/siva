def bubble_sort(arr):
    """Sorts a list using the bubble sort algorithm."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break # Optimization: If no swaps occur in a pass, the list is sorted
    return arr

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print(sorted_list) # Output: [11, 12, 22, 25, 34, 64, 90]
