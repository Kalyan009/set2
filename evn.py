a=int(input())
b=int(input())
if a%2==0:
  a=a+1
else:
  a=a
if b%2==0:
  b=b
else:
  b=b+1
for i in range(a,b):
  if i%2==0:
    print(i)
