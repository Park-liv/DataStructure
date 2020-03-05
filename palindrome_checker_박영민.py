def palindrome(str):
    pal_list = []
    for c in str:
        pal_list.append(c)
    l = len(pal_list) // 2
    stack = []
    for i in range(l):
        stack.append(pal_list[i])
    if len(pal_list)%2 == 0:
        for i in range(l):
            if stack[-1] == pal_list[l+i]:
                stack.pop(-1)
            else:
                return False
        return True
    else:
        for i in range(l):
            if stack[-1] == pal_list[l+i+1]:
                stack.pop(-1)
            else:
                return False
        return True

print(palindrome("ABSSBA"))
print(palindrome("RACECAR"))
print(palindrome("KART"))
print(palindrome("APPLE"))