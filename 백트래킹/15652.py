from itertools import combinations_with_replacement
n, m = map(int, input().split())
for x in combinations_with_replacement(range(1, n+1), m):
    print(*x)