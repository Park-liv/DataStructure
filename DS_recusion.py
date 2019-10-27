def reverse(S, start, stop):
    if start < stop -1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start + 1, stop - 1)

A = [0,1,2,3,4,5]
reverse(A, 0, len(A))
print(A)

def power(x, n):
    answer = 1
    for i in range(n):
        answer = answer * x
    return answer
print(power(2, 10))