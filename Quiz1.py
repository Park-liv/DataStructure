A = []

while True:
    x = input("수 입력 : ")
    if x == '00':
        print(A)
        break
    else:
        x = int(x)
        A.append(x)