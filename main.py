# 16
class PrimeCheck:
    def __init__(self, n):
        self.n = n
    def solve(self):
        if self.n < 2:
            return False
        for i in range(2, int(self.n**0.5)+1):
            if self.n % i == 0:
                return False
        return True

print(PrimeCheck(int(input())).solve())

# 17
class Divisors:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return [i for i in range(1, self.n+1) if self.n % i == 0]

print(Divisors(int(input())).solve())

# 18
class BasicOps:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def solve(self):
        return self.a + self.b, self.a - self.b, self.a * self.b

a, b = map(int, input().split())
print(*BasicOps(a, b).solve())

# 19
class ArraySum:
    def __init__(self, arr):
        self.arr = arr
    def solve(self):
        return sum(self.arr)

n = int(input())
arr = list(map(int, input().split()))
print(ArraySum(arr).solve())

# 20
class ArrayMax:
    def __init__(self, arr):
        self.arr = arr
    def solve(self):
        return max(self.arr)

n = int(input())
arr = list(map(int, input().split()))
print(ArrayMax(arr).solve())
