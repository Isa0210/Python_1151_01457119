from functools import wraps

def memoize_decorator(func):
    cache = {}  # 用來儲存已計算過的結果
    @wraps(func)  # 將原函式 func 的屬性複製給 wrapper
    def wrapper(*args, **kwargs):
        if args in cache:
            for arg in args:
                print(f"Cache hit for fibonacci({arg})")
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        for arg in args:
            print(f"Computed fibonacci({arg}) = {result}")
        return result

    return wrapper

@memoize_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
result = fibonacci(n)
print(f"Final Result: {result}")