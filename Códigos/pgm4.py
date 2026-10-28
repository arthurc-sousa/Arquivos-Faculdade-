a=input("Digite um numero ")
b=input("Digite outro numero ")
c=input("Digite outro numero " )

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b,c = c, b
print(a,b,c)