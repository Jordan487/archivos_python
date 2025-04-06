# Escritura de Archivo de Texto
# Creamos el archivo y escribimos al menos tres notas personales

with open("my_notes.txt", "w") as archivo:
    archivo.write("Hoy aprendí a trabajar con archivos de texto en Python.\n")
    archivo.write("Es importante cerrar los archivos después de usarlos.\n")
    archivo.write("Leer línea por línea me ayuda a procesar el contenido fácilmente.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo y leemos línea por línea

with open("my_notes.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # Mostramos la línea en la consola eliminando el salto de línea

# El archivo se cierra automáticamente al salir del bloque 'with'
