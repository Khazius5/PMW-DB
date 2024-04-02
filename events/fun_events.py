import mysql.connector

con = mysql.connector.connect(
    host="localhost", user="Khazius", password="Khazius22!", database="PaletoMotorWorks")

def agregar_empleado():

    print("{:>60}".format("-->> Agregar Registro de Empleado <<--"))
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    rol = input("Ingrese el rol del empleado: ")
    telefono = input("Ingrese el número de teléfono del empleado (Si no se conoce, ingrese 0): ")
    horas = 0
    horas_semana = 0

    cursor = con.cursor()
    # Inserción de los datos del empleado en la tabla EMPLEADO
    sql = "INSERT INTO EMPLEADO (Nombre, Apellido, Rol, Telefono, Horas, Horas_Semanales) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (nombre, apellido, rol, telefono, horas, horas_semana)
    cursor.execute(sql, values)
    con.commit()
    print("¡Registro de empleado agregado exitosamente!")
    input("Presione cualquier tecla para continuar...")
    menu()

def mostrar_empleados():
    print("{:>60}".format("-->> Mostrar Registros de Empleados <<--"))
    cursor = con.cursor()
    cursor.execute("SELECT * FROM EMPLEADO")
    empleados = cursor.fetchall()
    for empleado in empleados:
        print("Nombre: ", empleado[0])
        print("Apellido: ", empleado[1])
        print("Rol: ", empleado[2])
        print("Número de Teléfono: ", empleado[3])
        print("Horas: ", empleado[4])
        print("Horas Semanales: ", empleado[5])
        print()
    input("Presione cualquier tecla para continuar...")
    menu()

# Función para mostrar el registro de un empleado
def mostrar_registro_empleado():
    print("{:>60}".format("-->> Mostrar Registro de Empleado <<--"))
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    apellido_empleado = input("Ingrese el apellido del empleado: ")

    cursor = con.cursor()
    # Consulta para obtener el registro del empleado
    sql_select = "SELECT * FROM EMPLEADO WHERE Nombre = %s AND Apellido = %s"
    cursor.execute(sql_select, (nombre_empleado, apellido_empleado))
    resultado = cursor.fetchone()

    if resultado:
        print("{:>60}".format("-->> Registro de Empleado <<--"))
        print("{:>20} {:>20} {:>20} {:>20} {:>20} {:>20}".format("-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20))
        print("{:>20} {:>20} {:>20} {:>20} {:>20} {:>20}".format("Nombre", "Apellido", "Rol", "Número de Teléfono", "Horas", "Horas_Semanales"))
        print("{:>20} {:>20} {:>20} {:>20} {:>20} {:>20}".format("-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20, "-" * 20))
        print("{:>20} {:>20} {:>20} {:>20} {:>20} {:>20}".format(*resultado))
    else:
        print("No se encontró ningún empleado con ese nombre y apellido.")

    input("Presione cualquier tecla para continuar...")
    menu()



# Función para actualizar un registro de empleado
def actualizar_empleado():
    print("{:>60}".format("-->> Actualizar Registro de Empleado <<--"))
    nombre = input("Ingrese el nombre del empleado que desea actualizar: ")
    apellido = input("Ingrese el apellido del empleado que desea actualizar: ")
    rol = input("Ingrese el nuevo rol del empleado: ")
    telefono = input("Ingrese el nuevo número de teléfono del empleado: ")
    horas = input("Ingrese las nuevas horas del empleado: ")

    cursor = con.cursor()
    # Actualización de los datos del empleado en la tabla EMPLEADO
    sql = "UPDATE EMPLEADO SET Rol=%s, Telefono=%s, Horas=%s WHERE Nombre=%s AND Apellido=%s"
    values = (rol, telefono, horas, nombre, apellido)
    cursor.execute(sql, values)
    con.commit()
    print("¡Registro de empleado actualizado exitosamente!")
    input("Presione cualquier tecla para continuar...")
    menu()

# Función para eliminar un registro de empleado
def eliminar_empleado():
    print("{:>60}".format("-->> Eliminar Registro de Empleado <<--"))
    nombre = input("Ingrese el nombre del empleado que desea eliminar: ")
    apellido = input("Ingrese el apellido del empleado que desea eliminar: ")
    cursor = con.cursor()
    # Eliminación del registro de empleado de la tabla EMPLEADO
    sql = "DELETE FROM EMPLEADO WHERE Nombre=%s AND Apellido=%s"
    values = (nombre, apellido)
    cursor.execute(sql, values)
    con.commit()
    print("¡Registro de empleado eliminado exitosamente!")
    input("Presione cualquier tecla para continuar...")
    menu()

# Función para reemplazar las horas de un empleado
def reemplazar_horas():
    print("{:>60}".format("-->> Reemplazar Horas de Empleado <<--"))
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    apellido_empleado = input("Ingrese el apellido del empleado: ")
    nuevas_horas = int(input("Ingrese las nuevas horas: "))

    cursor = con.cursor()
    # Consulta para obtener las horas actuales del empleado
    sql_select = "SELECT Horas FROM EMPLEADO WHERE Nombre = %s AND Apellido = %s"
    cursor.execute(sql_select, (nombre_empleado, apellido_empleado))
    resultado = cursor.fetchone()

    if resultado:
        horas_actuales = resultado[0]
        horas_agregadas = nuevas_horas - horas_actuales
        # Actualización de las horas del empleado en la base de datos
        sql_update = "UPDATE EMPLEADO SET Horas = %s WHERE Nombre = %s AND Apellido = %s"
        cursor.execute(sql_update, (nuevas_horas, nombre_empleado, apellido_empleado))
        sql_update_semana = "UPDATE EMPLEADO SET Horas_Semanales = Horas_Semanales + %s WHERE Nombre = %s AND Apellido = %s"
        cursor.execute(sql_update_semana, (horas_agregadas, nombre_empleado, apellido_empleado))
        con.commit()
        print(f"Se han reemplazado las horas del empleado {nombre_empleado} {apellido_empleado}.")
        print(f"Horas anteriores: {horas_actuales}")
        print(f"Nuevas horas: {nuevas_horas}")
        print(f"Horas agregadas/reemplazadas: {abs(horas_agregadas)}")
    else:
        print("No se encontró ningún empleado con ese nombre y apellido.")

    input("Presione cualquier tecla para continuar...")
    menu()

def reiniciar_semana():
    print("{:>60}".format("-->> Reiniciar la Semana <<--"))
    cursor = con.cursor()
    # Actualización de las horas de todos los empleados a 0
    sql = "UPDATE EMPLEADO SET Horas_Semanales = 0"
    cursor.execute(sql)
    con.commit()
    print("¡Se han reiniciado las horas de todos los empleados!")
    input("Presione cualquier tecla para continuar...")
    menu()

# Menú principal
def menu():
    print("{:>60}".format("********************************************************"))
    print("{:>60}".format("-->> Sistema de Gestión de Empleados de Paleto MotorWorks <<--"))
    print("{:>60}".format("********************************************************"))
    print("1. Agregar Empleado")
    print("2. Mostrar Registros de Empleados")
    print("3. Mostrar Registro de Empleado")
    print("4. Actualizar Registro de Empleado")
    print("5. Agregar Horas a Empleado")
    print("6. Eliminar Registro de Empleado")
    print("7. Reiniciar la semana")
    print("8. Salir\n")
    print("{:>60}".format("-->> Seleccione una opción: [1/2/3/4/5/6/7] <<--"))

    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        agregar_empleado()
    elif opcion == 2:
        mostrar_empleados()
    elif opcion == 3:
        mostrar_registro_empleado()
    elif opcion == 4:
        actualizar_empleado()
    elif opcion == 5:
        reemplazar_horas()
    elif opcion == 6:
        eliminar_empleado()
    elif opcion == 7:
        reiniciar_semana()
    elif opcion == 8:
        print("¡Gracias por utilizar el sistema de gestión de empleados de Paleto MotorWorks!")
        con.close()
        exit()
