def subset_sum(nums, target):
    # nums: list of integers (repr follower counts of influencers)
    # target: target sum we want to find a subset for
    
    last_index = len(nums) - 1    
    
    if find_subset_sum(nums, target, last_index) == True:
        return True
    return False
        

def find_subset_sum(nums, target, index):
    if target == 0:
        return True
    
    if index < 0 and target != 0:
        return False

    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)

    else:
        result = find_subset_sum(nums, target, index - 1)

        reduced_target = target - nums[index]
        other_result = find_subset_sum(nums, reduced_target, index - 1)

        if result == True or other_result == True:
            return True
        else:
            return False

    

    
