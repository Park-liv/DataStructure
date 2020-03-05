# 트리
# • 조직이나 기관의 계층구조
# • 컴퓨터 운영체제의 파일 시스템
# • 자바 클래스 계층구조 등
# • 트리는 일반적인 트리와 이진트리(Binary Tree)로 구분
# • 다양한 탐색트리(Search Tree), 힙(Heap) 자료구조, 컴파일러의
# 수식을 위한 구문트리(Syntax Tree) 등의 기본이 되는 자료구조로
# 서 광범위하게 응용
# • 일반적인 트리(General Tree)는 실제 트리를 거꾸로 세워 놓은 형
# 태의 자료구조
# • HTML과 XML 의 문서 트리, 자바 클래스 계층구조, 운영체제의
# 파일시스템, 탐색트리, 이항(Binomial)힙, 피보나치(Fibonacci)힙
# 에서 사용
# • 일반적인 트리의 정의
# • 트리는 empty이거나, empty가 아니면 루트노드 R과 트리의 집합으
# 로 구성되는데 각 트리의 루트노드는 R의 자식노드이다. 단, 트리의 집
# 합은 공집합일 수도 있다
# • 루트(Root) – 트리의최상위에 있는 노드
# • 자식(Child) – 노드하위에 연결된 노드
# • 차수(Degree) – 자식노드 수
# • 부모(Parent) – 노드 의 상위에 연결된 노 드
# • 이파리(Leaf) – 자식 이 없는 노드
# • 형제(Sibling) – 동일 한 부모를 가지는 노 드
# • 조상(Ancestor) – 루트까지의 경로상에 있는 모든 노드들의 집합
# • 후손(Descendant) – 노드 아래로 매달린 모든 노드들의 집합
# • 서브트리(Subtree) – 노드 자신과 후손노드로 구성 된 트리
# • 레벨(Level) – 루트는 레벨 1, 아래 층으로 내려가며 레벨이
# 1씩 증가
# • 레벨은 깊이(Depth)와 동일
# • 높이(Height) – 트리의 최대 레벨
# • 키(Key) – 탐색에 사용되는 노드에 저장된 정보
# • 이파리: 단말(Terminal)노드 또는 외부(External)노드
# • 내부(Internal)노드 또는 비 단말(Non-Terminal)노드: 이파리가 아
# 닌 노드
# • 일반적인 트리를 메모리에 저장하려면 각 노드에 키와 자
# 식 수만큼의 레퍼런스 저장 필요
# • 노드의 최대 차수가 k라면, k개의 레퍼런스 필드를 다
# 음과 같이 선언해야
# • N개의 노드가 있는 최대 차수가 k인 트리
# • None 레퍼런스 수 (자식으로 연결이 없는 연결의 수)
# = Nk – (N-1) = N(k-1) + 1
# • Nk = 총 레퍼런스의 수
# • (N-1) = 트리에서 부모-자식을 연결하는 레퍼런스 수
# 왼쪽자식–오른쪽형제
# (Left Child-Right Sibling, LCRS) 표현
# • 노드의 왼쪽 자식과 왼쪽 자식의 오른쪽 형제를 가리키는 2개의 레
# 퍼런스만을 사용