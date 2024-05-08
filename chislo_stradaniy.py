def satana(x, base):
    alpha = "0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZЫ"
    k = len(x)-1
    result = 0 
    for i in x:
        result+=alpha.index(i)*(base**k)
        k-=1
    return result



y = satana("105",8)+satana("5F",37)*satana("1011",3)**satana("BA",15)



def ne_satana(y, base):
    alpha = "0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZЫ"
    result = ""
    while y > 0:
        result += alpha[y % base]
        y //= base
    return result



print(ne_satana(y, 24))
