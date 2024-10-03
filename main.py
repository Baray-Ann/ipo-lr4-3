n=int(input("Введите число, до которого будут выводиться числа Фибоначчи: "))
print("Ваше число:", n)
fsum=0
f1=0
f2=1
while fsum<=n:
    print(fsum)
    fsum=f1+f2
    f1=f2
    f2=fsum
