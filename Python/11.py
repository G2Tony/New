a = []
n = int(input())
for i in range(0,n):
    el = str(input())
    a.append(el)
max_str = max(a, key=len)
print(max_str)