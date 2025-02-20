import pyinputplus as p

def collect_data():
    inp1 = p.inputInt(prompt="Type a binary number! (only 0s and 1s are accepted)\n: ", blockRegexes=[r'[2-9\-]'])
    return inp1

def main():
    a = collect_data()
    dec = int(str(a), 2)
    print(f"Decimal representation: {dec}")

if __name__=="__main__":
    main()