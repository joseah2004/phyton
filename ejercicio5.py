# 1. Muestra cuántos usuarios hay en total.
# 2. Calcula la edad media de los usuarios.
# 3. Muestra el nombre del usuario más joven y su edad.
# 4. Muestra cuántos usuarios son de Madrid.
# 5. Crea una nueva lista con los nombres de los usuarios mayores de 20 años.
# 6. Crea una lista con las ciudades sin repetir (puedes usar un set o un truco con una lista).
# 7. Muestra todos los usuarios con formato legible, por ejemplo:

usuarios = [
    {"nombre": "Ana", "edad": 21, "ciudad": "Madrid"},
    {"nombre": "Luis", "edad": 19, "ciudad": "Madrid"},
    {"nombre": "Sara", "edad": 23, "ciudad": "Sevilla"},
    {"nombre": "Mario", "edad": 20, "ciudad": "Valencia"},
    {"nombre": "Lucia", "edad": 22, "ciudad": "Madrid"}

]



totalusuarios = len(usuarios)

print("Total de usuarios", totalusuarios)


total = 0

for usuario in usuarios:
    total += usuario["edad"]
edadMedia = total / len(usuarios)
print(edadMedia)



usuariomasjoven = usuarios[0]

for usuario in usuarios:
    if usuario["edad"]<usuariomasjoven["edad"]:
        usuariomasjoven =usuario


pri

