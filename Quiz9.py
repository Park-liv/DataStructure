'''
2부터 N-1 까지 모든수(i)를 소수인지 검사한다
i를 2부터 i까지 모든수(j)로 나누어 0인지 검사한다.
그때 j가 i와 같으면 i는 소수이므로 i를 문자형으로 변환해 빈리스트 A에 더한다.
아니면(j가 i보다 작으면) i는 소수가 아니므로
break한다(하지 않으면 for문은 j가 i와 같아질때 까지 돌아 소수가 아닌 수도 A에 더해지므로)
'''

def  Sosu():
    N = int(input())
    A = []

    for i in range(2,N):
        for j in range(2,i+1):
            if i % j == 0:
                if i == j:
                    A.append(i)
                else:
                    break

    A = list(map(str, A))   # 리스트 원소를 문자로 바꿈
    A = ', '.join(A)         # 리스트 A를 구분자 ,를 추가하여 문자열로 변환
    print(A)

Sosu()
Sosu()
Sosu()
Sosu()
Sosu()