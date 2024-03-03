from colorama import Fore
from tkinter import filedialog,Tk
from movie import Movie

root = Tk()
root.withdraw()
i=0
db=[]

def AbrirArchivo():
    file = str(filedialog.askopenfilename())
    with open(file) as archivo:
        for linea in archivo:
            ArrayLinea = linea.split(";")
            movie = ArrayLinea[0]
            actores = ArrayLinea[1]
            year = ArrayLinea[2]
            genero = ArrayLinea[3]
            newMovie = Movie(movie,actores,year,genero)
            db.append(newMovie)
    print(Fore.WHITE+'Archivo seleccionado: '+Fore.CYAN+file+'\n'+'\n')
    input(Fore.RED+'Presione enter para continuar...')  
    MenuPrincipal()
    print('\n'+'\n')

def GestionarPeliculas():
    print("1. Mostrar peliculas")
    print("2. Mostrar actores \n")
    try:
        selection = int(input('Seleccione una opcion'))
        if selection == 1:
            for pelicula in db:
                print(pelicula.movie)
            input(Fore.RED+'Presione enter para continuar...')  
            MenuPrincipal()
        elif selection == 2:
            i = 1
            for pelicula in db:
                print(str(i)+'. '+pelicula.movie)
                i = i+1
            selection = int(input('Seleccione una pelicula para mostrar sus actores'))
            print('\n'+'Actores:  '+db[selection-1].actores+'\n')
            input(Fore.RED+'Presione enter para continuar...')  
            MenuPrincipal()
        else:
            print('Opcion no existente')
            GestionarPeliculas()
    except:
        print(Fore.RED+'\n'+'Valor no reconocido'+'\n'+Fore.CYAN)
        GestionarPeliculas()

def Filtrado():
    print('\n\n')
    print('1. Filtrar por actor')
    print('2. Filtrar por año')
    print('3. Filtrar por genero')
    try:
        selection = int(input('Ingrese una opcion para filtrar'))
        if selection ==1:
            actor = input('\nIngrese el nombre del actor: ')
            print(actor+' actua en: \n')
            for act in db:
                if actor in act.actores:
                        print(act.movie)
            MenuPrincipal()
        elif selection ==2:
            year = input('\nIngrese el año de estreno: \n')
            print('Las peliculas estrenadas en el año '+year+' son:'+'\n')
            for ye in db:
                if year in ye.year:
                        print(ye.movie+', '+ye.genero)
            MenuPrincipal()
        elif selection ==3:
            genero = input('\nIngrese el genero a filtrar: \n')
            print('Las peliculas del genero '+genero+' son:'+'\n')
            for gen in db:
                if genero in gen.genero:
                        print(gen.movie)
            MenuPrincipal()
    except:
        print('Opcion no establecida')
        MenuPrincipal()


def PantallaInicial():
    print(Fore.WHITE+'===================================================================================')
    print(Fore.YELLOW+"Lenguajes Formales y de Programacion")
    print(Fore.RED+"Seccion B+")
    print(Fore.WHITE+"Carne:"+Fore.CYAN+" 202110588")
    print(Fore.WHITE+"Nombre:"+Fore.CYAN+" Geovanny Sebastian Herrera Claudio")
    print(Fore.WHITE+'===================================================================================')
    input()

def Selection():
    print('\n\n')
    selected = int(input())
    print('\n')
    if selected==1:
        AbrirArchivo()
    elif selected == 2:
        GestionarPeliculas()
    elif selected==3:
        Filtrado()

def MenuPrincipal ():
    print(Fore.WHITE+'===================================================================================')
    print(Fore.YELLOW+"                            MENU PRINCIPAL                            ")
    print(Fore.WHITE+'===================================================================================')
    print(Fore.WHITE+"1"+Fore.CYAN+" Cargar archivo de entrada")
    print(Fore.WHITE+"2"+Fore.CYAN+" Gestionar peliculas")
    print(Fore.WHITE+"3"+Fore.CYAN+" Filtrado")
    print(Fore.WHITE+"4"+Fore.CYAN+" Grafica")
    Selection()



PantallaInicial()
MenuPrincipal()
