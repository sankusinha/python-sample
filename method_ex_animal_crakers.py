def animal_crackers(org_str):
    split_str = org_str.split()
    if (split_str[0][0] == split_str[1][0]):
        return True
    else:
        return False
