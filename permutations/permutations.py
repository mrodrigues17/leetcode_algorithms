def permute(nums):
    # Approach uses recursion:
    # Base case is if list is length 1, then return that list    
    # Find the ith element in the list
    # Find the remaining elements in the list
    # Call the permute function on the remaining elements list
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    lst = []
    for i in range(len(nums)):
        k = [nums[i]]
        remaining_lst = nums[:i] + nums[i+1:]
        for j in permute(remaining_lst):
            lst.append(k + j)
    return lst

print(permute(['1','2','3','4','5']))