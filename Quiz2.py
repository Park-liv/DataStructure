A = input().split(',')
A = list(map(int,A))
max = A[0] #배열 첫번째 수로 초기화
flag = 0 # 최대값을 찾기위한 flag

for i in range(len(A)):
    if (A[i] > max): #현재 max값보다 크면 바꾸면서 최대값을 찾음
        max = A[i]
        flag = 1 # 한번이라도 바뀌면 flag는 1이됨

if flag == 0: #한번도 안바꿔졋으면 리스트 첫번째 수가 최대값
    max = A[0]

i = 0
while A[i] != max: #최대값과 같으면 루프 탈출, i는 최대값의 인덱스
    i += 1

min = max # 배열의 최대값으로 초기화
for j in range(len(A)): #최소값 찾기
    if (A[j] < min):
        min = A[j]

j = 0
while A[j] != min: #최소값과 같으면 루프 탈출, j는 최대값의 인덱스
    j += 1

# i와 j중 앞에있는것을 찾고 리스트 슬라이싱한것 사이값으로 출력, 최대 최소값이 같으면 사이수 출력 안함
if i < j: print("최대값 :", A[i], "최소값", A[j], "사이수 :", A[i+1:j])
elif i > j: print("최대값 :", A[i], "최소값", A[j], "사이수 :", A[j+1:i])
else: print("최대값 최소값 같음 :", A[i])