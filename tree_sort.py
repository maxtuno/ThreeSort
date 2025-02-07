import random
import math

def insertion_sort(lst, left, right):
    for i in range(left + 1, right + 1):
        key = lst[i]
        j = i - 1
        while j >= left and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

def tree_sort(lst, left, right):
    if left >= right:
        return
    
    mid = (left + right) // 2
    if mid != 0:
        if right - left + 1 <= math.log2(mid) + 1:  # Use insertion sort for small sublists
            insertion_sort(lst, left, right)
            return

    # Median-of-three pivot selection
    pivot = lst[mid]
    
    # Swap pivot to end for partitioning
    lst[mid], lst[right] = lst[right], lst[mid]

    i, j = left - 1, right

    while True:
        i += 1
        while lst[i] < pivot:
            i += 1
        
        j -= 1
        while lst[j] > pivot:
            j -= 1
        
        if i >= j:
            break
        
        lst[i], lst[j] = lst[j], lst[i]
    
    # Swap pivot back to its correct position
    lst[right], lst[i] = lst[i], lst[right]

    tree_sort(lst, left, i - 1)
    tree_sort(lst, i + 1, right)


# write an article in MD about the algorithm 3 Sort created by Oscar Riveros, explain and proof the complexity, temporal and spatial.
# Example usage:
if __name__ == "__main__":
    random.seed(42)
    data = [random.randint(1, 10) for _ in range(10)]
    
    tree_sort(data, 0, len(data) - 1)
    print(f"Sorted with {data} complexity steps.")

    print(data)
    
    assert all(data[i] <= data[i + 1] for i in range(len(data) - 1)), "Not properly sorted."
