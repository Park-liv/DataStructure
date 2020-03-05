def SR(R):
    S = input()
    S = list(S)
    P = []

    for i in range(len(S)):
        temp = S[i] * R
        P.append(temp)

    PP = ''.join(P)
    # print(PP)

    return PP

a = SR(2)
b = SR(5)
print(a)
print(b)