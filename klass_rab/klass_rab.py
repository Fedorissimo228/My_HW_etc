#1
year = int(input())
if year%4==0:
  print("yes")
else:
  print("no")
#2
x = int(input())
y = int(input())
xx = int(input())
yy = int(input())
xxx = int(input())
yyy = int(input())
b = y
c = x
if y==yy:
  b=yyy
if yyy==y:
  b=yy
if x==xx:
  c=xxx
if xxx==x:
  c=xx
print("x =",c,"y =",b)
#3
a = 4
while a!=84:
  a+=10
  print(a, a, a, a)
