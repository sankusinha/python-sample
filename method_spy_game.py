def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.remove(num)
    if code[0] == 'x':
        return True
    else:
        return False
