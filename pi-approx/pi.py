import random

inside_square = 0
inside_circle = 0

for i in range(100001):
    x = random.uniform(1,0)
    y = random.uniform(1,0)
    inside_square += 1
    if( x * x + y * y < 1):
        inside_circle += 1

pi = 4 * (inside_circle / inside_square)
print("Aproximate pi value after "+ str(i) +" Iterations is = "+ str(pi))
