# 이진트리 (Binary Tree)
# [정의] 이진트리는 empty이거나, empty가 아니면, 루트노드와 2개의 이
# 진트리인 왼쪽 서브트리와 오른쪽 서브트리로 구성된다.
# • 이진트리(Binary Tree): 각 노드의 자식 수가 2 이하인 트리
# • 컴퓨터 분야에서 널리 활용되는 기본적인 자료구조
# • 이진트리가 데이터의 구조적인 관계를 잘 반영하고, 효율적인 삽
# 입과 탐색을 가능하게 하며, 이진트리의 서브트리를 다른 이진트
# 리의 서브트리와 교환하는 것이 쉽기 때문
# • 포화이진트리(Full Binary Tree): 각 내부노드가 2개의 자식노드를
# 가지는 트리
# • 완전이진트리(Complete Binary Tree): 마지막 레벨을 제외한 각
# 레벨이 노드들로 꽉 차있고, 마지막 레벨에는 노드들이 왼쪽부터 빠
# 짐없이 채워진 트리
# • [정리] 포화이진트리는 완전이진트리이다
# • 레벨 k에 있는 최대 노드 수 = 2k-1 , k = 1, 2, 3, …
# • 높이가 h인 포화이진트리에 있는 노드 수 = 2h - 1
# • N개의 노드를 가진 완전이진트리의 높이 = [log2(N + 1)]
# • a[i]의 부모는 a[i//2]에 있다. 단, i > 1이다. e.g.) E의 부모는 a[5//2] = a[2]
# • a[i]의 왼쪽자식은 a[2i]에 있다. 단, 2i ≤ N이다. e.g.) E의 왼쪽 자식은 a[2x5] = a[10]
# • a[i]의 오른쪽자식은 a[2i+1]에 있다. 단, 2i + 1 ≤ N이다. e.g.) E의 오른쪽 자식은
# a[2x5+1] = a[11]
# 전위순회 (NLR)
# • 전위순회는 노드 n에 도착했을 때 n을 먼저 방문
# • 그 다음에 n의 왼쪽 자식노드로 순회를 계속
# • n의 왼쪽 서브트리의 모든 노드들을 방문한 후에는 n의 오른쪽
# 서브트리의 모든 후손 노드들을 방문
#
#  전위    중위     후위
#   1         2         3
# 2   3    1   3    1    2
#
# 트리연산: 총 노드수
# • 트리의 노드 수를 계산하는 것은 트리의 아래에서 위로 각 자식의
# 후손노드 수를 합하며 올라가는 과정을 통해 수행되며, 최종적으로
# 루트노드에서 총 합을 구함 (후위순회)
# • 트리의 높이도 아래에서 위로 두 자식을 각각 루트노드로 하는 서브
# 트리의 높이를 비교하여 보다 큰 높이에 1을 더하는 것으로 자신의
# 높이를 계산하며, 최종적으로 루트노드의 높이가 트리의 높이가 됨
# (후위순회방법)
# • 2개의 이진트리를 비교하는 것은 다른 부분을 발견하는 즉시 비교
# 연산을 멈추기 위해 전위순회 방법을 사용
# 총 노드수 계산
# • 트리의 노드 수 = 1 +
#  (루트노드의 왼쪽 서브트리에 있는 노드 수) +
#  (루트노드의 오른쪽 서브트리에 있는 노드 수)
# • 1은 루트노드 자신을 계산에 반영하는 것
# 수행시간
# • 앞서 설명된 각 연산은 트리의 각 노드를 한 번씩만 방문하므로
# O(N) 시간이 소요
#
# 이진트리의 높이
# • 트리의 높이
# = 1 + max (루트의 왼쪽 서브트리의 높이, 루트의 오른쪽 서브트
# 리의 높이)
# • 1은 루트노드 자신을 계산에 반영
# • 왼쪽과 오른쪽 서브트리의 높이는 같은 재귀적 방식으로 계산
#
# 꿰매진 이진트리
# (Threaded Binary Tree)
# • 이진트리의 기본 연산들은 레벨순회를 제외하고 모두 스택 자료구조를 사
# 용: 메소드의 재귀호출은 시스템 스택을 사용하므로 스택 자료구조를 사용
# 한 것으로 간주
# • 스택에 사용되는 메모리 공간의 크기는 트리의 높이에 비례
# • 스택 없이 이진트리의 연산을 구현하는 2 가지 방법
# 1. Node 객체에 부모를 가리키는 레퍼런스를 추가로 선언하여 순회에
# 사용하는 방법
# 2.노드의 None 레퍼런스들을 활용하는 것 (스레드 이진트리
# (Threaded Binary Tree)
# • [정의] 꿰매진 (쓰레드) 이진트리는 각 노드의 오른쪽 non-레퍼런
# 스를 다음 방문할 노드를 참조하게 하고, 각 노드의 왼쪽 non-레퍼
# 런스를 직전 방문한 노드를 참조하게 한 이진트리이다.
# • 스레드 이진트리는 대부분의 경우 중위순회에 기반하여 구현되나, 전
# 위순회이나 후위순회에 기반하여 스레드 트리를 구현할 수도 있음
# • 스레드 이진트리는 스택을 사용하는 순회보다 빠르고 메모리 공간도
# 적게 차지한다는 장점을 갖지만 데이터의 삽입과 삭제가 잦은 경우
# 그 구현이 비교적 복잡한 편이므로 좋은 성능을 보여주지 못한다는
# 문제점
# • Node 객체에 2개의 boolean 필드를 사용하여 레퍼런스가 스레드
# (다음 방문할 노드를 가리키는)로 사용되는 것인지 아니면 left나
# right가 트리의 부모 자식 사이의 레퍼런스인지를 각각 True 와
# False로 표시해주어야 함
#
# 이진트리의 특성
# • N개의 노드가 있는 이진트리의 None 레퍼런스 필드 수 = (N+1)
# • 왜냐하면 각 노드마다 2개의 레퍼런스(left와 right)가 있으므로 총
# 2N개의 레퍼런스가 존재하고, 이 중에서 부모 자식을 연결하는 레
# 퍼런스는 N-1개이기 때문
# • 부모 자식을 연결하는 레퍼런스가 N-1개인 이유는 루트노드를 제
# 외한 각 노드가 1개의 부모를 갖기 때문
# • 따라서 (N+1) 개의 None 레퍼런스 필드의 남는 정보를 이용하여
# 스택을 대신할 수 있는 정보를 활용하게 함
#
# 이진힙 Binary Heap
# • 이진힙(Binary Heap)은 우선순위큐(Priority Queue)를 구현하는 가장 기
# 본적인 자료구조이다.
# • 우선순위큐(Priority Queue) - 가장 높은 우선순위를 가진 항목에 접근,
# 삭제와 임의의 우선순위를 가진 항목을 삽입을 지원하는 자료구조
# • 스택이나 큐도 일종의 우선순위큐
# • 스택: 가장 마지막으로 삽입된 항목이 가장 높은 우선순위를 가지므로,
# 최근 시간일수록 높은 우선순위를 부여
# • 큐: 먼저 삽입된 항목이 우선순위가 더 높다. 따라서 이른 시간일수록 더
# 높은 우선순위를 부여
#
# 우선순위큐
# • 스택에 삽입되는 항목의 우선순위는 스택에 있는 모든 항목들의 우
# 선순위보다 높음
# • 큐에 삽입되는 항목의 우선순위는 큐에 있는 모든 항목들의 우선수
# 위보다 낮음
# • 삽입되는 항목이 임의의 우선순위를 가지면 스택이나 큐는 새 항목
# 이 삽입될 때마다 저장되어 있는 항목들을 우선순위에 따라 정렬해
# 야 하는 문제점이 있음
#
# 이진힙
# • [정의] 이진힙(Binary Heap, 혹은 힙)은 완전이진트리로서 부모의
# 우선순위가 자식의 우선순위보다 높은 자료구조
# 힙
# • 정리
# • a[i]의 자식은 a[2i]와 a[2i+1]에 있고,
# • a[j]의 부모는 a[j//2]에 있다, j > 1
# 이진힙의 종류
# • 최소힙(Minimum Heap): 키 값이 작을수록 높은 우선순위
# • 최대힙(Maximum Heap): 키 값이 클수록 더 높은 우선순위
# 최소힙의 루트에는 항상 가장 작은 키가 저장됨
# • 부모에 저장된 키가 자식의 키보다 작다는 규칙 때문
# • 루트는 a[1]에 있으므로, O(1) 시간에 min 키를 가진 노드 접근
#
# 최소값 삭제 delete_min()
# • [1] 힙의 가장 마지막 노드, 즉, 리스트의 가장 마지막 항목을 루트
# 로 옮기고,
# • [2] 힙 크기를 1 감소시킨다.
# • [3] 루트로부터 자식들 중에서 작은 값을 가진 자식 (승자)과 키를
# 비교하여 힙속성이 만족될 때까지 키를 교환하며 이파리 방향으로
# 진행 (downheap())
#
# 힙 만들기 create_heap() + downheap()
# • 상향식 힙만들기(Bottom-up Heap Construction)
# • [핵심 아이디어]
# • 각 노드에 대해, 상향식 방식으로 힙속성을 만족하도록 부모와
# 자식을 서로 교환
# • N개의 항목이 리스트에 임의의 순서로 저장되어 있을 때, 힙을
# 만들기 위해선 a[N//2]부터 a[1]까지 차례로 downheap을 각각
# 수행하여 힙속성을 충족시킨다.
#
# 삽입 insert() + upheap()
# • [1] 힙의 마지막 노드(즉, 리스트의 마지막 항목)의 바로 다음 비어
# 있는 원소에 새로운 항목을 저장
# • [2] 루트 방향으로 올라가면서 부모의 키와 비교하여 힙속성이 만족
# 될 때까지 노드를 교환
# • [2]의 과정은 이파리로부터 위로 올라가며 수행되므로 upheap
# 이라 부름
#
# 수행시간
# • Insert 연산을 위한 upheap은 삽입된 노드로부터 최대 루트까지 올
# 라가며 부모와 자식노드를 교환
# • delete_min 연산에서는 힙의 마지막 노드를 루트로 이동한 후,
# downheap을 최하위 층의 노드까지 교환해야 하는 경우가 발생
# • 힙에서 각 연산의 수행시간은 힙의 높이에 비례
# • 힙은 완전이진트리이므로 힙에 N개의 노드가 있으면 그 높이는 [log(n+1)]
# • 각 힙 연산의 수행시간은 O(logN)
#
# 힙 만들기 수행시간
# • 노드 수가 N인 힙의 각 층에 있는 노드 수를 살펴보자. 단, 간단한 계산을 위하
# 여 N = 2^k − 1로 가정, k는 양의 상수
# • 최하위층 (h = 0)의 노드 수 = [N/2]
# • (h=1)의 노드 수= [N/2^2]
# • (h=2)의 노드 수 = [N/2^2]
# • h층의 노드 수 = [N/2^(h+1)]
# • 힙만들기는 h=1인 경우부터 시작하여 최상위층의 루트까지 각 노드에 대해
# downheap을 수행
#
# 힙 만들기 수행시간
# O(N)