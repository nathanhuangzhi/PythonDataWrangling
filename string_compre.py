def str_compress(s):

    cnt = 1
    i = 1
    length = len(s)
    letter = s[0]
    output = ''
    while i < length:

        if s[i-1] == s[i]:
            cnt += 1
        else:
            output  = output + letter + str(cnt)
            cnt = 1
            letter = s[i]
        i += 1
    output = output + letter + str(cnt)

    return output

print(str_compress('AAAABBBB'))