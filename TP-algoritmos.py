def ordenar_alumnos(lista):
    x = len(lista)
    print(f"Iniciando ordenamiento por burbujeo. Lista original: {lista}")

    for i in range (x-1):
        cambio=False
        for y in range(0, x-i-1):
            if lista[y] > lista[y+1]:
                lista[y], lista[y+1]=lista[y+1], lista[y]
                cambio=True
        
        if not cambio:
            break
    
    print(f"Lista ordenada: {lista}")

def busqueda_binaria_alumno(lista_ordenada, nombre_objetivo):
    print(f"Buscando alumno: {nombre_objetivo}")

    inicio=0
    fin=len(lista_ordenada)-1
    paso=0

    while inicio <= fin:
        paso+=1
        medio=(inicio+fin)//2
        nombre_medio=lista_ordenada[medio]

        print(f"Paso {paso}: chequeando índice {medio} por {nombre_medio}")

        if nombre_medio == nombre_objetivo:
            print(f"{nombre_objetivo} encontrado en el índice {medio}. Busqueda finalizada en {paso} pasos")
            return nombre_medio, medio
        elif nombre_medio<nombre_objetivo:
            print(f"{nombre_objetivo} es alfabéticamente posterior a {nombre_medio}")
            inicio=medio+1
        else:
            print(f"{nombre_objetivo} es alfabéticamente anterior a {nombre_medio}")
            fin=medio-1
    print(f"{nombre_objetivo} no se encontro en la lista.")
    return None, -1


lista_nombres=["Agustin", "Sebastian", "Camila", "Diego", "Fabian", "Carla", "Lucas", "Juan", "Roman", "Tatiana", "Hugo", "Eugenia", "Daiana"]

print(f"Lista de alumnos sin ordenar: {lista_nombres}")

lista_ordenada=lista_nombres[:]
ordenar_alumnos(lista_ordenada)

buscar_alumno="Juan"

nombre_encontrado, indice_encontrado=busqueda_binaria_alumno(lista_ordenada, buscar_alumno)

if indice_encontrado !=-1:
    print(f"El nombre {nombre_encontrado} se encuentra en el archivo bajo el índice {indice_encontrado}.")
else:
    print(f"{buscar_alumno} no se encuentra en el archivero")

print("Ahora, ingrese un nombre para buscar en el archivero.")

nombre_buscado = input("Ingrese el nombre a buscar: ").strip()

nombre_encontrado_original, indice_encontrado = busqueda_binaria_alumno(lista_ordenada, nombre_buscado)

if indice_encontrado != -1:
    print(f"El alumno {nombre_encontrado_original} se encuentra en el archivo en el índice {indice_encontrado}.")
else:
    print(f"{nombre_buscado} no se encuentra en el archivero.")