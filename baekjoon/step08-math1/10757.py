def addBigInteger(s1, s2):
    len1 = len(s1)
    len2 = len(s2)

    idx = 1
    carry = 0
    result = []
    while idx <= len1 and idx <= len2:
        sum = int(s1[len1 - idx]) + int(s2[len2 - idx]) + carry
        carry = sum // 10
        result.append(sum % 10)
        idx += 1
 
    if idx <= len1:
        while idx <= len1:
            sum = int(s1[len1 - idx]) + carry
            carry = sum // 10
            result.append(sum % 10)
            idx += 1
    elif idx <= len2:
        while idx <= len2:
            sum = int(s2[len2 - idx]) + carry
            carry = sum // 10
            result.append(sum % 10)
            idx += 1
    if carry == 1:
        result.append(1)

    return ''.join(str(d) for d in reversed(result))

if __name__ == '__main__':
    strs = input().split()
    
    result = addBigInteger(strs[0], strs[1])

    print(result)