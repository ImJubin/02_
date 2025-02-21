# import copy
# import itertools
# from collections import deque

# def virus_bfs(temp_lab, virus_positions):
#     queue = deque(virus_positions)
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nr, nc = x + dr[i], y + dc[i]
#             if 0 <= nr < n and 0 <= nc < m and temp_lab[nr][nc] == 0:
#                 temp_lab[nr][nc] = 2
#                 queue.append((nr, nc))

#     return sum(row.count(0) for row in temp_lab)

# #######################################################################

# def solve():
#     global max_safe_area
#     for walls in itertools.combinations(empty_positions, 3):
#         temp_lab = copy.deepcopy(lab)

#         for r, c in walls:
#             temp_lab[r][c] = 1

#         safe_area = virus_bfs(temp_lab, virus_positions)
#         max_safe_area = max(max_safe_area, safe_area)
    
#     print(max_safe_area)

# #######################################################################

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# lab = []
# empty_positions = []
# virus_positions = []
# max_safe_area = 0

# n, m = map(int, input().split())
# for i in range(n):
#     row = list(map(int, input().split()))
#     lab.append(row)
#     for j in range(m):
#         if row[j] == 0:
#             empty_positions.append((i, j))
#         elif row[j] == 2:
#             virus_positions.append((i, j))

# solve()
