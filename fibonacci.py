def fibonacci(number: int) -> int:
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(5))



####listing 1.2
def fibonacci(number: int) -> int:
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    
    prev_1 = 0
    prev_2 = 1
    fib_n = 0
    
    for _ in range(2, number + 1):
        fib_n = prev_1 + prev_2
        prev_1, prev_2 = prev_2, fib_n
    
    return fib_n

if __name__ == "__main__":
    print(fibonacci(5))
    
    
    ####listing 1.3

def fibonacci2(n: int) -> int:
    if n < 2:  # base case
        return n
    return fibonacci2(n - 2) + fibonacci2(n - 1)  # recursive case

def fibonacci2(n: int) -> int:
    if n < 2:  # base case
        return n
    return fibonacci2(n - 2) + fibonacci2(n - 1)  # recursive case
def fibonacci2(n: int) -> int:
    if n < 2:  # base case
        return n
    return fibonacci2(n - 2) + fibonacci2(n - 1)  # recursive case

print(fibonacci2(0))

####listing 1.4
def fibonacci2(n: int) -> int:
    if n < 2:  # base case
        return n
    return fibonacci2(n - 2) + fibonacci2(n - 1)  # recursive case



if __name__ == "__main__":
    print(fibonacci2(5))  ### output is 5
    print(fibonacci2(10))  ### output is 10
    
    
    
    
    
##listing 1.5


from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}  # base cases

def fibonacci3(n: int) -> int:
    if n not in memo:
        memo[n] = fibonacci3(n - 1) + fibonacci3(n - 2)  # memoization
    return memo[n]
print(fibonacci3(5))  # Output: 5
print(fibonacci3(10))  # Output: 55




###listing 1.6
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}  # base cases

def fibonacci3(n: int) -> int:
    if n not in memo:
        memo[n] = fibonacci3(n - 1) + fibonacci3(n - 2)  # memoization
    return memo[n]

if __name__ == "__main__":
    print(fibonacci3(5))  # Output: 5
    print(fibonacci3(50))  # Output: 12586269025
    
##. listing 1.7

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci4(n: int) -> int:  # same definition as fib2()
    if n < 2:  # base case
        return n
    return fibonacci4(n - 2) + fibonacci4(n - 1)  # recursive case

if __name__ == "__main__":
    print(fibonacci4(5)) #output 5 
    print(fibonacci4(50)) # output 12586269025

    
 ##listing 1.8
def fibonacci5(n: int) -> int:
    if n == 0: return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

if __name__ == "__main__":
    print(fibonacci5(5)) # output5
    print(fibonacci5(50)) # output 12586269025
 

## listing 1.9


from typing import Generator

def fibonacci6(n: int) -> Generator[int, None, None]:
    yield 0  # special case
    if n > 0: yield 1  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next  # main generation step

if __name__ == "__main__":
    for i in fibonacci6(50):
        print(i)
