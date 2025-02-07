"""
Copyright (c) 2025 Oscar Riveros [https://www.instagram.com/riverosartist/].

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

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

# Example usage:
if __name__ == "__main__":
    random.seed(42)
    data = [random.randint(1, 10) for _ in range(10)]
    
    tree_sort(data, 0, len(data) - 1)

    print(data)
    
    assert all(data[i] <= data[i + 1] for i in range(len(data) - 1)), "Not properly sorted."
