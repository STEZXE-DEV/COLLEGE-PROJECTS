import pyinputplus as p
inp = p.inputStr(prompt="Podaj znak: ", blockRegexes=[r'^..+$']) #limitacja inputa do jednego znaku
if inp.isidentifier() and inp!='_': #czy znak jest identyfikatorem
    if inp.islower(): #czy znak w lowercase
        print(f"'{inp}' - Mała litera.")
    elif inp.isupper(): #czy znak w uppercase
        print(f"'{inp}' - Duża litera.")
elif inp.isdigit(): #czy znak jest cyfra
    print(f"'{inp}' - Cyfra")
else:
    print(f"'{inp}' - Znak specjalny.")