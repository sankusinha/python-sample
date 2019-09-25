def has_33(nums = [], *args):
    len_nums = len(nums)
    i=0
    while i<len_nums:
        if nums[i] == nums[i-1]:
            return True
        i = i+1
    if i == len_nums:
        return False
