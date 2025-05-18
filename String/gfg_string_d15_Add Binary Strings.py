def addBinary(s1, s2):
    result, carry = [], 0
    s1, s2 = s1.lstrip('0') or "0", s2.lstrip('0') or "0"
    n, m = len(s1), len(s2)
    if n < m: s1, s2 = s2, s1

    for i in range(1, len(s1) + 1):
        bit1 = int(s1[-i])
        bit2 = int(s2[-i]) if i <= len(s2) else 0
        bitSum = bit1 + bit2 + carry
        result.append(str(bitSum % 2))
        carry = bitSum // 2

    if carry: result.append('1')
    return ''.join(result[::-1])
s1="1001"
s2="1012"
print(addBinary(s1,s2))
