def div(a: float, b: float) -> None|str:
    if b == 0:
        return "Error ! Divide by 0"
    print(f"a divisé par b est égal à {a / b}")