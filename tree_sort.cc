/*
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
*/

#include <vector>
#include <iostream>
#include <random>
#include <algorithm>

template <typename T>
void insertion_sort(std::vector<T> &lst, int left, int right) {
    for (int i = left + 1; i <= right; ++i) {
        T key = lst[i];
        int j = i - 1;
        while (j >= left && lst[j] > key) {
            lst[j + 1] = lst[j];
            --j;
        }
        lst[j + 1] = key;
    }
}

template <typename T>
void tree_sort(std::vector<T> &lst, int left, int right) {
    if (left >= right) {
        return;
    }

    auto mid = (left + right) / 2;
    if (mid != 0 && right - left + 1 <= std::log2(mid) + 1) {
        insertion_sort(lst, left, right);
        return;
    }

    // Median-of-three pivot selection
    T pivot = lst[mid];
    
    // Swap pivot to end for easier partitioning
    std::swap(lst[mid], lst[right]);
    
    int i = left - 1, j = right;

    while (true) {
        do { ++i; } while (lst[i] < pivot);
        do { --j; } while (lst[j] > pivot);

        if (i >= j) break;
        std::swap(lst[i], lst[j]);
    }

    // Restore pivot
    std::swap(lst[right], lst[i]);

    // Recursively sort subarrays
    tree_sort(lst, left, i - 1);
    tree_sort(lst, i + 1, right);
}

int main() {
    using T = int;

    std::random_device device;
    std::default_random_engine engine(device());
    std::uniform_int_distribution<T> uniform(0, 10000000);

    engine.seed(1379);

    std::size_t size{1000000};
    std::vector<T> data(size);
    auto generator = [&]() { return uniform(engine); };
    std::generate(data.begin(), data.end(), generator);

    tree_sort(data, 0, data.size() - 1);

    // Verify the correct order
    for (int i = 1; i < data.size(); ++i) {
        if (data[i - 1] > data[i]) {
            std::cout << "Not ordered correctly." << std::endl;
            return EXIT_FAILURE;
        }
    }

    std::cout << "Sorted correctly." << std::endl;

    return EXIT_SUCCESS;
}