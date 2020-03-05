B = int(input())
A = input().split()
A = list(map(int,A))

C = []

# 나머지를 하나씩 C에 추가
for i in range(len(A)):
    temp = A[i] % B
    C.append(temp)

# set은 중복제거
C = list(set(C))

print(len(C))