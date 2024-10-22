from module.addition import add
from module.substract import sub
from module.multiplication import mult
from module.division import div

def calculate(a: float, b: float, operator: str) -> None:

    if operator not in ("+", "-", "*", "/"):
        print("ERROR - Operator not defined")
    elif operator == "+":
        add(a, b)
    elif operator == "-":
        sub(a, b)
    elif operator == "*":
        mult(a, b)
    else:
        div(a, b)
    return None

