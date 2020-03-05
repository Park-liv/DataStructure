# def main():
#     max(93, 11)
#     min(93, 11)
#     max(11, 11)
#     min(93, 93)
#
# def max(x, y):
#     if x > y:
#         return print(x)
#     elif y > x:
#         return print(y)
#     else:
#         return print("입력된 두 값이 같습니다")
#
# def min(x, y):
#     if x < y:
#         return print(x)
#     elif y < x:
#         return print(y)
#     else:
#         return print("입력된 두 값이 같습니다")
#
# if __name__ == "__main__":
#     main()

# def MaxMin(numList):
#     Max = numList[:]
#     for i in range(1,len(Max)):
#         if Max[0] < Max[i]:
#             temp = Max[0]
#             Max[0] = Max[i]
#             Max[i] = temp
#
#     Min = numList
#     for i in range(1,len(Min)):
#         if Min[0] > Min[i]:
#             temp = Min[0]
#             Min[0] = Min[i]
#             Min[i] = temp
#
#     return print('최대값:', Max[0], "최소값:", Min[0])
#
# MaxMin([5, 9, 7, 6, -2, 11, 8, 4])
# MaxMin([95, 9, 7, 6, 3, 11, 8, 24])
# MaxMin([0, 9, 17, 56, 3, 11, 8, 4])

# def swap(x, y):
#     print('x:', x, 'y:', y)
#     temp = x
#     x = y
#     y = temp
#     print('x:', x, 'y:', y)
#
# swap(20, 55)

# def swap(List, i, j):
#     if(i<0 or j<0 or i>=len(List) or j>=len(List)):
#         return print("입력된 인덱스가 범위를 벗어남")
#     else:
#         if i == j:
#             return print("입력된 두 인덱스 값이 같음")
#         else:
#             print(List, '바뀌는 인덱스',i ,',', j)
#             temp = List[i]
#             List[i] = List[j]
#             List[j] = temp
#             print("위치 바뀜", List)
# A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# swap(A, 100, 2)
# swap(A, 2, 2)
# swap(A, 7, 2)

# def shift(arr, s, t):
#     if(s<0 or t<0 or s>=len(arr) or t>=len(arr)):
#         return print("입력된 인덱스가 범위를 벗어남"), print('')
#     else:
#         if s == t:
#             return print("입력된 두 인덱스 값이 같음"), print('')
#
#     shiftArr = arr[:]
#     temp = arr[t]
#
    # for i in range(t, s, -1):
    #     shiftArr[i] = shiftArr[i-1]
#
#     shiftArr[s] = temp
#
#     print('입력배열', arr)
#     print(s, '부터', t, '까지 한칸씩 이동')
#     print('출력배열', shiftArr)
#     print('')
#
# A = [1, 2, 3, 4, 5, 6, 7, 8]
# shift(A, 2, 10)
# shift(A, 4, 4)
# shift(A, 2, 6)
# shift(A, 0, 7)

def shift(arr, k, LR):
    shiftArr = arr[:]

    if LR == 1:
        strLR = '오른쪽'
        for i in range(len(arr)):
            if i + k < len(arr):
                shiftArr[i+k] = arr[i]
            else:
                shiftArr[i + k - len(arr)] = arr[i]
    else:
        strLR = '왼쪽'
        for i in range(len(arr)):
            if i - k >= 0:
                shiftArr[i - k] = arr[i]
            else:
                shiftArr[i - k + len(arr)] = arr[i]

    print('입력배열', arr)
    print(strLR + '(',LR,') 방향으로', k, '칸 이동')
    print('출력배열', shiftArr)
    print('')

A = [1, 2, 3, 4, 5, 6, 7]
shift(A, 3, 1)
shift(A, 2, 0)