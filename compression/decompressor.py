def decompress(s):
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        count = ''
        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1
        result.append(char * int(count))
    return ''.join(result)

# Test
print(decompress("ab2c1ac3"))  # aabbcaaaccc
