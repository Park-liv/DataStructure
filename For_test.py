# x = 50
#
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
#
# func(x)
# print('x is still', x)

# def func():
#     global x
#
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
#
#
# func()
# print('Vakue of x is', x)

# def getPerson():
#     name = "Leona"
#     age = 35
#     country = "UK"
#     return name, age, country
# name1, age1, country1 = getPerson()
# print(name1)
# print(age1)
# print(country1)

# bri = set(['brazil', 'russia', 'india'])
# print('india' in bri)
# print('usa' in bri)
# bric = bri.copy()
# bric.add('china')
# print(bric.issuperset(bri))
# print(bric.issubset(bri))
# bri.remove('russia')
# print(bri & bric)
# print(bri | bric)

shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist
del(shoplist[0])
print('shoplist', shoplist)
print('mylist', mylist)
mylist = shoplist[:]
del(shoplist[0])
# del(mylist[0])
print('shoplist', shoplist)
print('mylist', mylist)

'''
• 입력: 외부로 공급되는 수량이 0개 이상이다.
• 출력: 최소 1개 이상의 수량이 생산된다.
• 명확성: 각 지침은 명확하고 명확해야 한다.
• 완성도: 알고리즘의 지침을 추적하면 모든 경우에 대해 알고리즘은 제한된 수의 단계 후에 종료된다.
• 효율성: 모든 지침은 원칙적으로 연필과 종이만을 사용하는 사람이 수행할 수 있을 정도로 충분히 기초적이어야 한다. 
        각각의 작전이 확실하다고는 할 수 없지만, 또한 실현 가능해야 한다.
        
• 최악경우 분석(Worst-case Analysis)
    어떤 입력이 주어지더라도 알고리즘의 수행시간이 얼마 이상은 넘지 않는다’라는 상한(Upper Bound)의 의미
• 평균경우 분석(Average-case Analysis)
    입력의 확률 분포를 가정하여 분석하는데, 일반적으로 균등분포(Uniform Distribution)를 가정
• 최선경우 분석(Best-case Analysis)
    가장 빠른 수행시간을 분석
'''