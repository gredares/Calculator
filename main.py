from module.calculator import calculate

if __name__ == "__main__":
    a = 5 # float(input("Enter the value for a: "))
    b = 10 # float(input("Enter the value for b: "))
    calculate(a, b, "<3")
    operators = ["+", "-", "*", "/"]
    for operator in operators:
        calculate(a, b, operator)

