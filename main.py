import confi

###################################################################

print('Bienvenido al gestor de base de datos con python\n')
print('########## Tabla estudiantes #############')
print(''' Por favor elija unas de las siguientes opciones:

(1) Para insertar datos en la Base de datos
(2) Para consultas en la Base de datos
(3) Para actualizar datos en la Base de datos
(4) Para eliminar datos en la Base de datos
(5) Para salir del programa
                     
''')


def run():
    prendido = True
    while prendido:  # mientras sea true se ejecuta
        opcion = int(input("Digite su Opcion: "))
        if opcion == 1:
            print(f'''Haz  selecionado la opcion para insertar datos acontinuacion digite
                  los valores correspondiente en este orden separado por coma
                  matricula nombre edad sexo cuatrimestre''')

            valores = tuple(input('Digite sus Valores------>  ').split(','))
            confi.insertando_datos(valores)
            confi.consultar_datos('select * from estudiantes')

        elif opcion == 2:
            print('Haz selecionado la opcion para consultas digite su query o consulta deseada')
            consulta = input('consulta ----->')
            print('********query***********\n')
            confi.consultar_datos(consulta)

        if opcion == 3:
            print(f'''Haz selecionado la opcion para actualizar datos por nombre acontinuacion digite los 
    nuevos valores correspondiente en este orden separado por coma
    matricula nombre edad sexo cuatrimestre y digite el nombre para actualizar''')

            confi.consultar_datos('select * from estudiantes')
            actualizacion = tuple(input('digite sus valores------>  ').split(','))
            confi.actualizando_datos(actualizacion)
            confi.consultar_datos('select * from estudiantes')

        if opcion == 4:
            print(f'''Haz selecionado la opcion para borrar registros por nombre 
    digite el nombre de la persona  para eliminar todo lo relacionado con ese nombre aqui 
    estan todos los registros de la base de dato:''')

            confi.consultar_datos('select * from estudiantes')
            borrador = input('digite el nombre------>')
            cambio = (borrador,)
            confi.borrando_datos(cambio)
            confi.consultar_datos('select * from estudiantes')

        elif opcion == 5:
            print('Hasta la proxima')
            confi.conexion.close()
            prendido = False


if __name__ == '__main__':
    run()
