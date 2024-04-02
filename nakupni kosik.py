zbozi = ["CPU","GPU", "RAM", "Motherboard","Zdroj", "Case"]
kosik = []

def vypis_pole(zbozi):
    for x in range(len(zbozi)):
        print(f"{x+1}: {zbozi[x]}")
        print(" ")


prvek_plus = input("Zadejte jaké zboží chcete přidat")
kosik.append(prvek_plus)

vypis_pole(kosik)

prvek_minus = int(input("Zadejte co chcete odstranit"))

zbozi.pop(prvek_minus)
vypis_pole(zbozi)

