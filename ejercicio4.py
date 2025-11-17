# "Implementa un programa modularizado que, leyendo la nota obtenida por tres alumnos en una asignatura, "
# "muestre por pantalla la media de las notas."


#Un array como di fuera java
#lo para que pide lso 3 alumnos mas simple




def leer_notas():
    notas = [] 
    for i in range(3):
        nota = float(input("Introduce la nota del choclo {i + 1}: "))
        notas.append(nota)
    return notas


