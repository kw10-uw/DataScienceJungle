#1. List Comprehension

a = [1,2,3,4]
res = [val ** 2 for val in a]
print(res)

# 1.1 Filtering

filtered = [val for val in a if val%2 == 0]
print(filtered)

# 1.2 Creating a list
b = [i for i in range(10)]
print(b)

# 1.3 Using nested loops 
c = [(x,y) for x in range(3) for y in range(3)]
print(c)

# 1.4 Flattening list of lists - unpacking smaller lists 
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result  = [val for row in mat for val in row]
print(result)