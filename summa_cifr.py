print ("введите ЛЮБОЕ НАТУРАЛЬНОЕ число")
a = int(input())
b = 0
while a//1!=0:
  b+=a%10
  a=a//10
print(b)
