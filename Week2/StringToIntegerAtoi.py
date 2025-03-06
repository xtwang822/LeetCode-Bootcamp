def myAtoi(s: str) -> int:
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    s = s.lstrip()

    if not s:
        return 0

    sign = 1
    index = 0

    if s[index] == '-':
        sign = -1
        index += 1
    elif s[index] == '+':
        index += 1

    num = 0
    while index < len(s) and s[index].isdigit():
        num = num * 10 + int(s[index])
        index += 1

    num *= sign

    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX

    return num

s = " -42"
print(myAtoi(s))