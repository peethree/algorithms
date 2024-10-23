def merge_sort(nums):
    
    if len(nums) < 2:
        return nums

    middle_index = len(nums) // 2

    left = nums[:middle_index]
    right = nums[middle_index:]

    sorted_first = merge_sort(left)
    sorted_second = merge_sort(right)

    return merge(sorted_first, sorted_second)


def merge(first, second):
    final = []

    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    
    final.extend(first[i:])
    final.extend(second[j:])

    return final