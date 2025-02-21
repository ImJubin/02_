import copy
import itertools  # 조합을 사용하기 위한 itertools 모듈 import
from collections import deque  # BFS(너비 우선 탐색) 구현을 위한 deque import

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(lab, virus_positions):
    queue = deque(virus_positions)  # 바이러스가 있는 위치를 큐에 삽입
    n, m = len(lab), len(lab[0])  # 연구소 크기 저장
    temp_lab = copy.deepcopy(lab)  # 연구소 맵을 복사하여 사용 (원본 유지)
   
    while queue:
        x, y = queue.popleft()  # 현재 바이러스 위치
        for i in range(4):  # 상하좌우로 이동
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp_lab[nx][ny] == 0:  # 빈 칸이면 확산
                temp_lab[nx][ny] = 2  # 바이러스 확산
                queue.append((nx, ny))  # 큐에 추가하여 계속 확산 진행
   
    return sum(row.count(0) for row in temp_lab)  # 안전 영역(0의 개수) 반환

def solve():
    n, m = map(int, input().split())  # 연구소 크기 입력
    lab = []  # 연구소 지도 저장
    empty_positions = []  # 빈 칸(0)의 위치 리스트
    virus_positions = []  # 바이러스(2)의 위치 리스트
   
    for i in range(n):
        row = list(map(int, input().split()))  # 연구소 지도 입력
        lab.append(row)  # 지도 저장
        for j in range(m):
            if row[j] == 0:
                empty_positions.append((i, j))  # 빈 칸 좌표 저장
            elif row[j] == 2:
                virus_positions.append((i, j))  # 바이러스 좌표 저장
   
    max_safe_area = 0  # 최대 안전 영역 크기 저장 변수
   
    # 벽을 세울 3개의 위치 선택 (조합 사용)
    for walls in itertools.combinations(empty_positions, 3):
        temp_lab = copy.deepcopy(lab)  # 연구소 맵 복사 (원본 보존)
       
        for x, y in walls:
            temp_lab[x][y] = 1  # 벽(1) 세우기
       
        # 바이러스 확산 후 안전 영역 계산
        safe_area = bfs(temp_lab, virus_positions)
        max_safe_area = max(max_safe_area, safe_area)  # 최대값 갱신
   
    print(max_safe_area)  # 최대 안전 영역 출력

solve()  # 메인 실행 함수 호출