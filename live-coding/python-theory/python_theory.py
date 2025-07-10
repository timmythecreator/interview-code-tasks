'''
File with Python theory concepts and examples.
Includes small tasks with explanations and expected outputs.
'''

# ======================== Example 1: MRO ========================
# TASK:
# What will be printed on the screen by the following code?
class A:
    def rk(self):
        print("In class A")

class B(A):
    def rk(self):
        print("In class B")

class C(A):
    def rk(self):
        print("In class C")

class D(B, C):
    # No rk() method defined here
    pass

# Create an instance of D and call rk()
d = D()
d.rk() # Output: In class B

# EXPLANATION:
# Class D inherits from both B and C: class D(B, C)
# Python uses the MRO (method resolution order) to determine which method to call.
# MRO for class D is: D → B → C → A
# So, Python looks for rk() in class D → not found
# Then in B → found: prints "In class B"

# ======================== Example 2: Walrus Operator ========================
# TASK:
# What will the following code print?
if i := 5 > 0:
    print(i) # Output: True

# SOLUTION:
# The expression is evaluated as: i := (5 > 0)
# 5 > 0 is True, so i = True
# The if-condition is True, so it prints True.

# To assign 5 to i and then compare: use parentheses:
if (i := 5) > 0:
    print(i) # Output: 5

# ======================== Example 3: class Store implementation ========================
# TASK:
# Implement the Store class so that the following syntax works:
# store = Store()
# store["a"] = 5
#
# The class should allow storing and retrieving values using square bracket notation,
# just like a dictionary.

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

# Example usage:
store = Store()
store["a"] = 5         # Calls __setitem__("a", 5)
print(store["a"])      # Calls __getitem__("a"). Output: 5

# ======================== Example 4: How set() works ========================
# TASK:
# What will be printed by the following code?

def add_num(i, s=set()):
    s.add(i)
    return s

print(add_num(23)) # Output: {23}
print(add_num(12, set([1, 2]))) # Output: {1, 2, 12}
print(add_num(78)) # Output: {23, 78}

# EXPLANATION:
# Default mutable arguments (like set()) are evaluated only once at function definition.
# So the first and third call share the same set() object!
#
# 1. add_num(23) → uses default set(), becomes {23}
# 2. add_num(12, set([1, 2])) → uses a NEW set, returns {1, 2, 12}
# 3. add_num(78) → uses the same default set as in (1), now becomes {23, 78}
