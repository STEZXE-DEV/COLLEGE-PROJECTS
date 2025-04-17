def wstawianie_sort(a):
    for i in range(1, len(a)):
        c=a[i]
        pos=i
        while pos>0 and a[pos-1]>c:
            a[pos]=a[pos-1]
            pos-=1
        a[pos]=c
    return a



lista = [1,2,333,444,5,5,6,67,7,1,88]
wstawianie_sort(lista)
print(lista)