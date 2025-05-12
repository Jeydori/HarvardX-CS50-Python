from pyfiglet import Figlet
import sys

def main():
        if (len(sys.argv) == 3) and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
            f = sys.argv[2]
            print(f"Output: {convert(f)}")
        elif 0 < len(sys.argv) < 3:
            print(f"Output: {convert(0)}")
        else:
            sys.exit("Invalid usage")

def convert(f):
    figlet = Figlet()
    try:
        figlet.setFont(font=f)
        text = str(input("Input: "))
        if f == 0:
            return figlet.renderText(text)
        else:
            return figlet.renderText(text)
    except:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()
