def Totalscore():
    OX = input()
    OX = list(OX)
    score = [0] * len(OX) #각 문제당 점수 0으로 초기화
    # print(score)
    flag = 0 # 연속된 정답 혹은 오답을 위한 변수 정답이면 1 오답이면 -1
            # 첫 문제에서는 flag = 0 그러므로 for문 안에서 i-1은
            # 인덱스 에러를 일으키지 않음
    for i in range(len(OX)):
        if OX[i] == 'O': # 현재 문제 정답
            if flag == 1: # 직전 문제가 정답일경우
                score[i] = score[i-1] + 1 # 직전 문제의 점수에 +1
            else: # 직전 문제가 오답 혹은 첫 문제일 경우
                score[i] = 1
                flag = 1 # 다음문제를 위해 1로 바꿈
        else: # 현재문제 오답
            if flag == -1: # 직전 문제가 오답일경우
                score[i] = score[i-1] - 1 # 직전 문제의 점수에 -1
            else: # 직전 문제가 정답 혹은 첫 문제일 경우
                score[i] = -1
                flag = -1 # 다음문제를 위해 -1로 바꿈
    # 총점 구함
    total_score = 0
    for i in range(len(score)):
        total_score += score[i]
    print(score) # 생략 가능
    print(total_score)
#5번 실행
Totalscore()
Totalscore()
Totalscore()
Totalscore()
Totalscore()