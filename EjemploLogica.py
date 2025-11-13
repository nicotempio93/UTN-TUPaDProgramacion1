#Defino variables
tecla_espacio_presionada = True
esta_tocando_el_suelo = False

# Aca se evalua el valro de verdad de la expresion logica y se toma una decision
if tecla_espacio_presionada and esta_tocando_el_suelo:
  print(f"El valor de verdad de (tecla_espacio_presionada and esta_tocando_el_suelo) = {tecla_espacio_presionada and esta_tocando_el_suelo}")
  print("¡Saltando!")
else:
  print(f"El valor de verdad de (tecla_espacio_presionada and esta_tocando_el_suelo) = {tecla_espacio_presionada and esta_tocando_el_suelo}")
  print("No se puede saltar.")