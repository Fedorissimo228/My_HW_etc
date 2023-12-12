print("введите ЦЕЛОЕ число ЛЮБОЙ длины, и мы скажем, ПРОСТОЕ ли оно")
a = int(input())
i = 2
while i <= a:
  if a % i == 0 and i!=a:
      print("NO")
      break
  i += 1
  if i == a:
      print("YES")
