def uni_char(s):

    exist = set()
    for i in s:
        if i not in exist:
            exist.add(i)
        else:
            return False
    return True
print(uni_char('abcda'))