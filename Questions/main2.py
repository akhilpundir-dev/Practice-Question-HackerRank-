# Find runner-up score
import random
arr=[]

def random_score(n):
  for i in range(n):
    arr.append(random.randint(1,20))

random_score(5)

arr.sort()
max_score = arr[-1]
print(arr)
for x in reversed(arr):
  if x != max_score:
    print(x)
    break

