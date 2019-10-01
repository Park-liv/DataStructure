def dataCalc1(data):
    data = data + 1
def dataCalc2(data):
    data[0] = data[0] + 1
def main():
    data1 = 1
    data2 = [1]

    dataCalc1(data1)
    print('data1 : ', data1)
    dataCalc2(data2)
    print('data2 : ', data2)

if __name__ == '__main__':
    main()