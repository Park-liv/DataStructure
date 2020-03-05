def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        print(data[low:high + 1])
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
print(binary_search([1,2,3,4,5,6,7,8,9,0], 9, 0, 9))

def reverse(S, start, stop):
    if start < stop-1:
        print(start, stop-1)
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start+1, stop-1)
    print(S)
reverse([0,1,2,3,4,5,6],0,7)

def power(x, n):
    answer = 1
    for i in range(n):
        answer = answer * x
    return answer
print(power(2, 10))