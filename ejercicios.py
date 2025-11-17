empleados = 20
ventas = 18   
balance = 5   

MAXEMPLEADOSMICRO = 10
MAXVENTASMICRO = 2   
MAXBALANCEMICRO = 5  
microEmprexa = ((empleados <= MAXEMPLEADOSMICRO and ventas <= MAXVENTASMICRO) or balance <= MAXBALANCEMICRO)

print(microEmprexa)  
print(type(microEmprexa))  

chiqui = not microEmprexa and (ventas > 5 or balance < 0)
print(chiqui)
print(chiqui)


