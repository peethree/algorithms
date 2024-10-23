def quick_sort(nums, low, high):
    if low < high:
        partition_index = partition(nums, low, high)
        
        quick_sort(nums, low, partition_index - 1)
        
        quick_sort(nums, partition_index + 1, high)


def partition(nums, low, high):
    pivot = nums[high]

    i = low - 1

    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
            
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


"""
Fixing Quick Sort Big O
As we discussed, while the version of quicksort that we implemented is almost always able to perform at speeds of O(n*log(n)), its Big O is still technically O(n^2). We can fix this by altering the algorithm slightly.

There are two approaches:

Shuffle input randomly before sorting. This can trivially be done in O(n) time
Actively find the median of a sample of data from the partition, this can be done in O(1) time.
Random Approach
The random approach is easy to code, works practically all of the time, and as such is often used.

The idea is to quickly shuffle the list before sorting it. The likelihood of shuffling into a sorted list is astronomically unlikely, and is also more unlikely the larger the input.

Median Approach
One of the most popular solutions is to use the "median of three" approach. Three elements (for example: the first, middle, and last elements) of each partition are chosen and the median is found between them. That item is then used as the pivot.

This approach has the advantage that it can't break down to O(n^2) time because we are guaranteed to never use the worst item in the partition as the pivot. That said, it can still be slower because a true median isn't used.

"""