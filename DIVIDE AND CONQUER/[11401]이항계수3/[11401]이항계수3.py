def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans % 10000000007

def b_fact(n, r):
    return factorial(n) // factorial(n-r) // factorial(r)

n, r = map(int, input().split())
print(b_fact(n, r))

'''

'''