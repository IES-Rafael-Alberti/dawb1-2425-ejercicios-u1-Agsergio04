coste_pan = 3.49
pan_no_fresco = 3.49 * 0.6

cantidad_pan_no_fresco = int(input("Introduce la cantidad de panes no frescos vendidos en el dia: "))

precio_total_pan_malo = cantidad_pan_no_fresco * pan_no_fresco

print("El pan fresco esta a: ",coste_pan)
print("El pan que no es fresco esta a: ",pan_no_fresco)
print("La ganancia obtenida por el pan no fresco en el dia es de: ",round(precio_total_pan_malo,2))