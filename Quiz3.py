A = input().split(',')
A = list(map(int,A))
# 각각 카운트 초기화
asc = 0
des = 0
sta = 0
# 각각을 체크하는 함수:리스트와 현재인덱스 값 입력으로 받음
def Asc_check(A,i):
    while True:
        if i + 1 > len(A) - 1: # 체크하는 인덱스 범위 벗어나면 루프 탈출
            break
        # ascending 마지막 인덱스 체크
        if A[i+1] == A[i]+1:
            i += 1
        else:
            break
    return i # 체크후 마지막 인덱스 리턴

def Des_check(A,i):
    while True:
        if i + 1 > len(A) - 1:
            break
        # descending 마지막 인덱스 체크
        if A[i+1] == A[i]-1:
            i += 1
        else:
            break
    return i

def Sta_check(A,i):
    while True:
        if i + 1 > len(A) - 1:
            break
        # stable 마지막 인덱스 체크
        if A[i+1] == A[i]:
            i += 1
        else:
            break
    return i

i = 0
while True:
    if i+1 >len(A)-1: # 체크 인덱스 범위 벗어나면 루프 탈출
        break
    # 현재 인덱스 asc, des, sta 인지 체크시작
    if A[i+1] == A[i]+1: # 체크되면 각 카운트 1추가
        asc += 1
        i = Asc_check(A, i)
    elif A[i+1] == A[i]-1:
        des += 1
        i = Des_check(A, i)
    elif A[i+1] == A[i]:
        sta += 1
        i = Sta_check(A, i)

    i += 1

print("accending :", asc, "descedning :", des, "stable :", sta)