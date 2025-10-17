import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multipy(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multipy,
    "/":divide
}
def calculator():
    print(art.logo)
    go_again = True
    value1 = float(input("Please type your first number: "))

    while go_again:

        sign = input("\n+\n-\n*\n/\nPlease type your desired operation: ")
        value2 = float(input("Please type your second number: "))
        calculation = operations[sign](value1, value2)

        print(f"{value1} {sign} {value2} = {calculation}")

        reuse_value = input(f"Would you like to perform another operation using {calculation}? y/n\n")

        if reuse_value == "y":
            value1 = calculation
        else:
            go_again = False
            print("\n" * 20)
            calculator()

calculator()



