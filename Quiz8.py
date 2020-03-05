def Sugar():
    N = int(input())
    NN = N

    A = [5,3,1] # 설탕 kg 수
    B = []      # 각각 몇 봉지인지 저장하는 리스트

    for i in range(len(A)):
        mok = int(NN / A[i])    # NN / 각 봉지 kg의 몫 = 몇봉지
        nmg = NN % A[i]         # 나머지 -> 몫 만큼 들고간후 남은 설탈 kg수

        B.append(mok)           # 몫을 리스트에 추가
        NN = nmg                # 나머지를 새로운 NN 으로 둔다

    for i in range(len(B)):     # 1, 3, 5 순으로 나와야하기 때문에
        if B[len(B)-1-i] != 0:  # 리스트 길이 - 1 - i 로 역순으로 출력
            print("{}({})".format(A[len(A)-1-i], B[len(B)-1-i]), end=' ')
                                # end=' ' 로 줄바꿈 없이 한칸 띄우고 출력
    print('')   # 줄바꾸기위한 출력

Sugar()
Sugar()
Sugar()