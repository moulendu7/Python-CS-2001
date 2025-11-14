import random
import math
num = random.randint(1, 100)
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
print(num)
if is_prime:
    print("Prime")
else:
    print("Not Prime")
