eq = input().strip()
eq.replace(" + ", "OR")
eq.replace(" ", ", " AND ")
eq.replace("~ ", "NOT ")
eq.replace("OR", " OR ")

print(eq)