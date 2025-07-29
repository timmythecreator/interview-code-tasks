"""
File with Python tasks and their solutions.
Includes small tasks with explanations and expected outputs.
"""

# ======================== Task 1: Decorator with Arguments ========================
# TASK: Write a decorator that takes an argument `n` and repeats the execution of the decorated function `n` times.
# The decorator should return a list of results from each execution.
# SOLUTION:
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(n):
                r = func(*args, **kwargs)
                result.append(r)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
    return 1

greet("John") # Output: Hello, John! (printed 3 times)