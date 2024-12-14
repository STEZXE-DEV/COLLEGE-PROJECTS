
def silnia(s):
    s2=s-1
    if s<=1:
        return 1
    else:
        return s*silnia(s2)
def main():
    metody={1:'default', 2:'funkcja'}
    for k,v in metody.items():
        print(f"{k} - {v}")
    wybor=int(input("Podaj numer metody: "))

    if wybor in metody.keys():
        match wybor:
            case 1:
                x=int(input("Podaj liczbe: "))
                a=x
                for i in range(1, x+1):
                    if i == a:
                        print(x)
                    else:
                        x*=i
            case 2:
                s=int(input("Podaj liczbe: "))
                wynik = silnia(s)
                print(wynik)

if __name__=='__main__':
    main()