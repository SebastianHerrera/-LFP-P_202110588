from os import system
import os
from movie import Movie
import graphviz

db = []

with open("C:/Users/sebas/OneDrive/Documentos/USAC/Primer Semestre 2024/Lab LFP/Practica/Archivos de Entrada/Entrada 1.txt") as archivo:
        for linea in archivo:
            ArrayLinea = linea.split(";")
            movie = ArrayLinea[0]
            actores = ArrayLinea[1]
            year = ArrayLinea[2]
            genero = ArrayLinea[3]
            newMovie = Movie(movie,actores,year,genero)
            db.append(newMovie)


file = open("grafica.dot","w")
file.write("digraph ejemplo{\n")
file.write('rankdir = LR\n')

for i in db:
    print(i.movie)
    file.write('"'+i.movie+'" -> "'+i.actores+'";\n')
file.write('}')

def dot_to_png(dot_file, output_dir):
    # Nombre del archivo PNG basado en el nombre del archivo DOT
    basename = os.path.basename(dot_file)
    png_file = os.path.splitext(basename)[0] + '.png'

    # Ruta completa para el archivo PNG de salida
    png_path = os.path.join(output_dir, png_file)

    # Comando para convertir DOT a PNG usando el comando 'dot'
    command = f'dot -Tpng {dot_file} -o {png_path}'

    # Ejecutar el comando en la línea de comandos
    os.system(command)

# Ejemplo de uso
dot_filename = 'grafica.dot'
output_directory = 'C:/Users/sebas/OneDrive/Documentos/USAC/Primer Semestre 2024/Lab LFP/Practica'

dot_to_png(dot_filename, output_directory)