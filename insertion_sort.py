def insertion_sort(nums):    
    
    for index, num in enumerate(nums):
        j = index
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1

    return nums
        

    # for i in range(len(nums)):
    #     j = i
    #     while j > 0 and nums[j - 1] > nums[j]:
    #         nums[j], nums[j - 1] = nums[j - 1], nums[j]
    #         j -= 1
    # return nums