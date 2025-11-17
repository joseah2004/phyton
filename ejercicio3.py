# Una industria mantiene una flota de camiones  para repartir productos . En cada
# viaje , el conductor anota la distancia recorrida en kilometros, los litros degasoil utilizados , el coste del gasoil
# y los demas costes de mantenimiento del camion. Como aprte del proceso de contabilidad, 
# el controlador necesita calcular, para cada camion y para cada viaje , los kilometros recorridos por litro , el coste 
# tortal del viaje y el coste pro kilometro 
# Diseña un programa sencillo que lleve a cabo estos calculos  para un camion en un viaje

kilometros = float(input("kilometros: "))
litrosss = float(input("litros: "))
costeGasolina = float(input("coste gasoil: "))
costeMantenimiento = float(input("coste mantenimiento: "))

kilPorLitro = kilometros / litrosss
costeTotal = costeGasolina + costeMantenimiento
costePorKm = costeTotal / kilometros

print("kilometros por litro ", kilPorLitro)
print("coste por kilometro ", costePorKm)
print("coste total del viaje ", costeTotal)

