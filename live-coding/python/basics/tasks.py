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

# Example usage 
greet("John") # Output: Hello, John! (printed 3 times)

# ======================== Task 2: class Store implementation ========================
# TASK: Implement the Store class so that the following syntax works:
# store = Store()
# store["a"] = 5
#
# The class should allow storing and retrieving values using square bracket notation,
# just like a dictionary.
# SOLUTION:
class Store:
    def __init__(self):
        # Use an internal dictionary to store key-value pairs
        self._data = {}

    def __setitem__(self, key, value):
        # Called when using store[key] = value
        self._data[key] = value

    def __getitem__(self, key):
        # Called when accessing store[key]
        return self._data[key]

# Example usage
store = Store()
store["a"] = 5         # Calls __setitem__("a", 5)
print(store["a"])      # Calls __getitem__("a"). Output: 5