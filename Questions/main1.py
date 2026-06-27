# Print all coordinates [i, j, k]
# where 0 <= i <= x, 0 <= j <= y, 0 <= k <= z
# and i + j + k != n 
# using list comprehension 

x=2
y=3
z=2
n=3
result = [
  [i,j,k]
  for i in range(x+1)
  for j in range(y+1)
  for k in range(z+1)
  if i+j+k!=n
]
print(result)