import timeit

code_to_test = """
N = int(input())
A = []
for i in range(2,N):
    for j in range(2,i+1):
        if i % j == 0:
            if i == j:
                A.append(i)
            else:
                break
A = list(map(str, A))
A = ', '.join(A)
print(A)
"""

# code_to_test를 number만큼 반복한 만큼의 시간(단위는 초)을 반환하므로 1번만 실행
elapsed_time = timeit.timeit(code_to_test, number=1)
print(elapsed_time, 'sec')