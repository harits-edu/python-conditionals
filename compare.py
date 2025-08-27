# The first approach
""" 
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is the same as y")

"""

# The second approach (much faster)
""" 
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x == y:
    print("x is the same as y") 
"""

# The third approach, the perfect way, this approach is more efficient as seen from the flowchart
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is the same as y") 
