# OOPS and turtle
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Raichu", "Bulbazor"])
table.add_column("Type", ["Electric", "Electric", "Leaf"])
table.align = "c"
print(table)
