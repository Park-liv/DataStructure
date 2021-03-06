# 스택 (Stack)
# • 한 쪽 끝에서만 item(항목)을 삭제하거나 새로운 item을 저장하는
# 자료구조
# • 새 item을 저장하는 연산: push
# • Top item을 삭제하는 연산: pop
# • 후입 선출(Last-In First-Out, LIFO) 원칙 하에 item의 삽입과 삭
# 제 수행
# 수행시간
# • 파이썬의 리스트로 구현한 스택의 push와 pop 연산은 각각 O(1) 시
# 간이 소요
# • 파이썬의 리스트는 크기가 동적으로 확대 또는 축소되며, 이러한 크
# 기 조절은 사용자도 모르게 수행된다. 이러한 동적 크기 조절은 스택
# (리스트)의 모든 항목들을 새 리스트로 복사해야 하기 때문에 O(N)
# 시간이 소요
# • 단순연결리스트로 구현한 스택의 push와 pop 연산은 각각 O(1) 시
# 간
# • 연결리스트의 맨 앞 부분에서 노드를 삽입하거나 삭제하기 때문
#
# 수식표기법
# • 중위표기법(Infix Notation)
# • 프로그램을 작성할 때 수식에서 +, –, *, /와 같은 이항연산자는 2개
# 의 피연산자들 사이에 위치
# • 컴파일러는 중위표기법 수식을 후위표기법(Postfix Notation)으로 바
# 꾼다.
# • 그 이유는 후위표기법 수식은 괄호 없이 중위표기법 수식을 표현할
# 수 있기 때문
# • 전위표기법(Prefix Notation): 연산자를 피연산자들 앞에 두는 표기법
#
# 큐
# • 큐(Queue): 삽입과 삭제가 양 끝에서 각각 수행되는 자료구조
# • 일상생활의 관공서, 은행, 우체국, 병원 등에서 번호표를 이용한 줄서기
# 가 대표적인 큐
# • 선입 선출(First-In First-Out,FIFO) 원칙 하에 item의 삽입과 삭
# 제 수행
# 수행복잡도
# • 리스트로 구현한 큐의 add와 remove 연산은 각각 O(1) 시간이 소
# 요
# • 하지만 리스트 크기를 확대 또는 축소시키는 경우에 큐의 모든 항목
# 들을 새 리스트로 복사해야 하므로 O(N) 시간이 소요
# • 단순연결리스트로 구현한 큐의 add와 remove 연산은 각각 O(1)
# 시간
# • 삽입 또는 삭제 연산이 rear 와 front로 인해 연결리스트의 다른 노
# 드들을 일일이 방문할 필요 없이 각 연산이 수행되기 때문
#
# 데크 (DeQue)
# • 데크(Double-ended Queue, Deque): 양쪽 끝에서 삽입과 삭제
# 를 허용하는 자료구조
# • 데크는 스택과 큐 자료구조를 혼합한 자료구조
# • 따라서 데크는 스택과 큐를 동시에 구현하는데 사용
# 데크의 구현
# • 이중연결리스트로 구현하는 것이 가장 이상적
# • 단순연결리스트는 rear가 가리키는 노드의 이전 노드의 레퍼런
# 스를 알아야 삭제가 가능하기 때문
# 수행복잡도
# • 데크를 배열이나 이중연결리스트로 구현한 경우, 스택과 큐의 수행
# 시간과 동일
# • 양 끝에서 삽입과 삭제가 가능하므로 프로그램이 다소 복잡
# • 이중연결리스트로 구현한 경우는 더 복잡함