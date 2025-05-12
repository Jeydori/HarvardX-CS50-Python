def calculate(mass):
    energy = mass*(300000000)**2
    return energy

def main():
    mass = int(input("Input mass in kg to calculate Energy in Joule: "))
    result = calculate(mass)
    print(f"{result}")

main()
