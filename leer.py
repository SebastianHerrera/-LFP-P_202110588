from movie import Movie

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
ActsIn = []
yearcito = input()
for amigo in db:
      if yearcito in amigo.year:
            print("Yo actue en "+amigo.movie)