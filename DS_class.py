'''
클래스에선 __init__ 메소드가 필수
객체화가 될때 바로 호출됨
인스턴스 생성 초기에 변수를 지정해줌

self란
레퍼런스를 가르킴
클래스 내부 함수는 무조건 self가 필요
실제 사용되지 않음
다른 목적으로 사용됨

클래스 메소드의 첫번째 인수로 self를 써줘야 해당 메소드를
인스턴스의 메소드로 사용할 수 있게 됩니다.

클래스 변수와 함수는
클래스 내에 하나만존재

스태틱 함수는 클래스내에 있는 변수를
사용하지않는다.
스태틱함수를 쓰면 객체를 사용하지 않아도된다

클래스 함수와 스태틱 함수는 self를
사용하지 않는다.
'''

class Employee:
    def __init__(self, name):
        self.name = name
    def display(self):
        print('The name of employee is:',self.name)

first =  Employee('Rsuhabh')
second = Employee('Dhaval')

second.display()
first.display()


class Calculator:

    count = [0, 0, 0, 0]    # 클래스 변수

    def __init__(self):
        Calculator.count = [0, 0, 0, 0]

    @staticmethod
    def Add(a, b):
        Calculator.count[0] += 1
        return a+b

    @staticmethod
    def Min(a, b):
        Calculator.count[1] += 1
        return a - b

    @staticmethod
    def Mul(a, b):
        Calculator.count[2] += 1
        return a * b

    @staticmethod
    def Div(a, b):
        if b == 0:
            print("0으로 나누어짐")
            return "Nan"
        else:
            Calculator.count[3] += 1
            return a / b

    @classmethod
    def PrintCount(cls):    # 클래스 함수
        Hap = 0
        print("덧셈 :", cls.count[0])
        print("뺄셈 :", cls.count[1])
        print("곱셈 :", cls.count[2])
        print("나눗셈 :", cls.count[3])
        for i in range(len(cls.count)):
            Hap += cls.count[i]
        print("총 계산수 :", Hap)

cal = Calculator()
print("10 + 20 =", cal.Add(10,20))
print("10 - 20 =", cal.Min(10,20))
print("10 * 20 =", cal.Mul(10,20))
print("10 ÷ 0 =", cal.Div(10,0))
print("10 ÷ 2 =", cal.Div(10,2))
print("10 ÷ 2 =", cal.Div(10,7))
Calculator.PrintCount()
