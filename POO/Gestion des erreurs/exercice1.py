def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division par zéro !"
    

    print(safe_divide(2,0))
    