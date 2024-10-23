def power_set(input_set):
      
    # Step 1: Check if the input list is empty
    if not input_set:
        return [[]]
    
    # Step 2: Create an empty list to hold all the final subsets
    final_subsets = []
    
    # Step 3: Recursively call power_set with all elements except the first one
    subsets = power_set(input_set[1:])
    
    # Step 4: Iterate over the subsets returned from the recursive call
    for subset in subsets:
        # Step 4.1: Add the subset with the first item from input_set
        final_subsets.append([input_set[0]] + subset)
        # Step 4.2: Add the subset without the first item
        final_subsets.append(subset)
    
    # Step 5: Return the list of subsets
    return final_subsets
