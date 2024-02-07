a = int(input())
b = int(input())
f=0
e=0
g=0
h=0
while b != 0:
  f += 1
  d = b // (10 ** f)
  e += d
  b = b // 10
mumu=e
mumumu=b
mu=0
while a!=0:
  a-=1
  c = int(input())
  while c!=0:
    h+=1
    d = c//(10**h)
    g+=d
    c=c//10
  if g>mumu:
    mumu=g
    mumumu=c
  if g==mumu:
    mu=c
print(mumumu)
  
