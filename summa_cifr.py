print ("введите ЛЮБОЕ НАТУРАЛЬНОЕ число")
a = int(input())
b = 0
while a%10!=0:
  b+=a%10
  a/=10
print(b)
