import random as r
pkn={"paper":1,"rock":2,"scissors":3}
los=r.randint(1,3)
pkn2={1:"paper",2:"rock",3:"scissors"}
los_slowny=pkn2[los]

a=input("paper, rock or scissors: \n")

if a in pkn.keys():
    print(f"CPU: {los_slowny}")
    if pkn[a]==los:
        print(f"Tie.")
    if los == 1 and pkn[a] == 2:
        print(f"You Lost.")
    if los == 1 and pkn[a] == 3:
        print(f"You Won.")
    if los == 2 and pkn[a] == 1:
        print(f"You Won.")
    if los == 2 and pkn[a] == 3:
        print(f"You Lost.")
    if los == 3 and pkn[a] == 1:
        print(f"You Lost.")
    if los == 3 and pkn[a] == 2:
        print(f"You Won.")