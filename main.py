from Grid import Grid

try:
    xstr = input("Ingresa el numero de columnas: ")
    x = int(xstr)
except (TypeError, ValueError):
    print("That didn't look like an integer to me.")
    exit()

try:
    ystr = input("Ingresa el numero de filas: ")
    y = int(ystr)
except (TypeError, ValueError):
    print("That didn't look like an integer to me.")
    exit()


grid = Grid(x, y)

# Para mostrar el procedimiento comenta esta linea
grid.calculate(True, False)
# Y descomenta esta 
# grid.calculate(True, True)
