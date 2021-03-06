# import sys; input =sys.stdin.readline
# N, B = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(N)]
# C = [[0]*N for _ in range(N)]; dp = {1:A}
# def mul(a, b):
#     i, j = 0, 0
#     for m in range(N):
#         for k in range(N):
#             tmp = 0
#             for n in range(N):
#                 tmp += a[m][n] * b[n][k]
#             if j>N-1:
#                 i+=1;j=0
#             C[i][j] = tmp%1000
#             j+=1
#
# flag = True; i=1
# while True:
#     if flag:
#         if i*2 < B:
#             mul(dp[i], dp[i])
#             i *= 2
#             dp[i] = C # A^i를 DP에 삽입.
#             C = [[0] * N for _ in range(N)]
#         else:
#             flag = False
#             B -= i
#     else:
#         if B == i:
#             mul(dp[i],dp[max(dp.keys())]) # DP[i] * DP[-1] 값 출력.
#             break
#         i //= 2
#
# for c in C:
#     print(*c)

''' 시간 초과 발생 '''
import sys; input =sys.stdin.readline
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
def mul(a, b):
    C = [[0] * N for _ in range(N)]
    for m in range(N):
        for k in range(N):
            for n in range(N):
                C[m][k] += a[m][n] * b[n][k]
            C[m][k] %= 1000
    return C

def dev(mat, b):
    if b==1:
        return mat
    elif b==2:
        return mul(mat, mat)
    else:
        tmp = dev(mat, b//2)
        if b%2==0:
            return mul(tmp, tmp)
        else:
            return mul(mul(tmp, tmp), mat)

result = dev(A, B)
for r in result:
    print(*r)

'''

'''