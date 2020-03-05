if __name__ == '__main__': #내가 실행시키는 파일이 메인인지
    print('THis program is being run by itself')
else: #임포트 되면 메인이 아니기때문에 밑에 문구가 출력됨
    print('I am being imported from another module')

def say_hi():
    print('Hi, this is mymodule speaking')

__version__ = '0.1'
