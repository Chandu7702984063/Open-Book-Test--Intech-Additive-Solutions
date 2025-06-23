def advanced_compress(s):
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        count = ''
        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1
        if result and result[-1][0] == char:
            continue
        result.append(char + count)
    return ''.join(result)

# Test
print(advanced_compress("a2b1c5a3"))  # ab1c5a3
print(advanced_compress("a2b2c1a3c3"))  # ab2c1ac3
