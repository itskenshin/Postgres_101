import psycopg2  # libreria para conectarnos con postgresql
import os

conexion = psycopg2.connect(  # para conectarno a la base de datos guardo en un objeto la conexion
    user='postgres',
    password=os.getenv("POSTGRES-PASS"),  # pass
    host=os.getenv("POSTGRES-URL"),  # host
    port='5432',
    database='prueba'

)

def insertando_datos(valores):
    try:
        with conexion:  # va conectarse a la BD
            with conexion.cursor() as cursor:
                sentencia = 'insert into estudiantes(matricula,nombre,edad,sexo,cuatrimestre) ' \
                            'values (%s,%s,%s,%s,%s)'
                cursor.execute(sentencia, valores)
                print(f'{cursor.rowcount} cambio realizado')

    except Exception as e:
        print(f'ha ocurrido el siguiente error {e}')


def consultar_datos(query):
    try:
        with conexion:
            with conexion.cursor() as cursor:
                cursor.execute(query)
                registro = cursor.fetchall()
                print(f'''
            TABLA estudiantes
            
Matricula--Nombre--Edad-Sexo-Cuatrimestre ''')
                for x in range(len(registro)):
                    print(registro[x])


    except Exception as e:
        print(f'ha ocurrido el siguiente error {e}')


def actualizando_datos(update):
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia_update = 'update estudiantes set matricula = %s,nombre = %s, edad = %s, sexo = %s, cuatrimestre = %s where nombre = %s'
                cursor.execute(sentencia_update, update)
                print(f'{cursor.rowcount} cambio realizado')

    except Exception as e:
        print(f'ha ocurrido el siguiente error {e}')


def borrando_datos(borrando):
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia_delete = 'delete from estudiantes where nombre = %s'
                cursor.execute(sentencia_delete, borrando)
                print(f'{cursor.rowcount} cambio realizado')

    except Exception as e:
        print(f'ha ocurrido el siguiente error {e}')
