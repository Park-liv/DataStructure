def say_hello():
    # block belonging to the function
    print('hello world')
# End of function
say_hello() # call the function
say_hello() # call the function again

'''
함수의 리턴은 메인으로 함
레퍼런스(?)에 리턴 할 수도 있음
파이썬은 선언과 정의를 같이한다(예: 맨위에 쓰는 import)
'''

def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
# directly pass literal values

print_max(3, 4)

x = 5
y = 7

# pass variables as arguments
print_max(x, y)