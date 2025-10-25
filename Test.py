pais_capital = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasília', 'Colombia': 'Bogotá', 
                'Chile': 'Santiago', 'Perú': 'Lima'}

capital_pais = {}

for pais in pais_capital:
    capital = pais_capital[pais]
    capital_pais[capital] = pais

print(f"Diccionario original (país: capital):{pais_capital}")
print(f"Diccionario invertido (capital: país): {capital_pais}")