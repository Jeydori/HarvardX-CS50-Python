#Problemset0 of jeoydori (Jyd Rey Mercado)

lowercase = ""

def convert(uppercase):
    lowercase = uppercase.strip().lower()
    return lowercase

def main():
    uppercase = input("Type a string: ")
    result = convert(uppercase)
    print(f"{result}")
    
main()
