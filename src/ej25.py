fecha_nacimiento_pregunta = input("Introduce tu fecha de nacimiento separada en barras (dia/mes/anio): ")

fecha_nacimiento = fecha_nacimiento_pregunta.split('/')
dia = fecha_nacimiento[0]
mes = fecha_nacimiento[1]
anio = fecha_nacimiento[2]

print("El dia del año es",dia,",junto a su mes",mes,"del año",anio)