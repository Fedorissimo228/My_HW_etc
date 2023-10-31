print("введите ЦЕЛОЕ число ЛЮБОЙ длины, и мы скажем ВСЕ его делители")
a = int(input())
i=1
while i<a:
  if a%i==0:
    print(i)
  i+=1
  print(a)
