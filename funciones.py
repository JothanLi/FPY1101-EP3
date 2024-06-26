libros = []
Sku = []
autores = []
años = []
prestamos = []

def registrar_libro():
    name_libro = input('Ingrese el título del libro: ').upper()
    autor = input('Ingrese el autor del libro: ').upper()
    año = input('Ingrese el año de publicación del libro: ')
    sku = input('Ingrese el SKU del libro: ').upper()
    libro = {'titulo':name_libro, 
             'autor':autor, 
             'año':año, 
             'sku':sku
             }
    libros.append(name_libro)
    autores.append(autor)
    años.append(año)
    Sku.append(sku)
    print(libros, sep= '\n')
    print(libro)
def prestar_libro():
    user = input('Ingrese el nombre del usuario: ').upper()
    libro_prestar = input('Ingrese el SKU del libro que se requiere: ').upper()
    fecha = input('Ingrese la fecha de préstamo: ')
    if libro_prestar in Sku:
        print('Libro encontrado con éxito.')
        libros.remove(libro_prestar)
        prestamos.append(user,libro_prestar, fecha)
    else:
        print('Libro no encontrado.')
def listar_libros():
    print('TÍTULO\t\tAUTOR\t\tAÑO DE PUBLICACIÓN\tSKU')
    print(f'{libros}{autores}{años}{Sku}', sep=' ')
def imprimir_prestamo():
    with open ('Préstamos.txt', 'w') as file:
        file.write(f'USUARIO\t\tTÍTULO\t\tFECHA DEL PRÉSTAMO')
        file.write(f'{prestamos}')
        print('Creando archivo...')
def salir():
    print('Programa finalizado...\nDesarrollado por Jonathan Lillo\nRUN: 21.602.653-5')
def main():
    while True:
        print('Menú\n1. Registrar libro\n2. Prestar libro\n3. Listar todos los libros\n4. Imprimir reporte de préstamos\n5. Salir del programa')
        op = int(input('Ingrese una opción: '))
        try:
            if op == 1:
                registrar_libro()
            elif op == 2:
                prestar_libro()
            elif op == 3:
                listar_libros()
            elif op == 4:
                imprimir_prestamo()
            elif op == 5:
                salir()
                break
            else:
                print('Opción incorrecta, vuelve a intentarlo.')
        except ValueError:
            print('Valor ingresado incorrecto.')
if __name__ == '__main__':
    main()