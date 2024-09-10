def do_smtg(x):
    if x < 0:
        return "Invalid input"
    elif x == 0 or x == 1:
        return x
    
    a, b = 0, 1
    for _ in range(2, x):
        a, b = b, a + b
    return b