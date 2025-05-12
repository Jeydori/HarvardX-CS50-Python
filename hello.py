emoticon = "T_T"

def main():
    greet = input("find me! ")
    said = say(greet)
    print(f"{said} {emoticon}")

def say(input):
    if "hello" in input:
        return "hi, there"
    else:
        return "I'm not sure what u r talking about"

main()
