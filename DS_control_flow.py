'''
파이썬은 iterator가 있다
range 범위 주의
while문에는 break과 continue가 있다.
'''
# 여러개 if문, 다중 if문, elif 문 차이 알아오기

for i in range(1, 5):
    print(i)
else:
    print("The for loop is over")

while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print("Length of the string is ", len(s))
print('done')