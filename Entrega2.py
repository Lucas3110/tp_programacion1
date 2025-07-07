"""
-----------------------------------------------------------------------------------------------
Título: Empresa de viajes
Fecha: 25/05/2025
Autor: Maia Medina, Eugenia Alonso, Lucas Rodriguez, Juan Ciro Petrella y Caterina Turdo
Descripción: Sistema para gestión de paquetes de viajes con manejo de datos en JSON.
-----------------------------------------------------------------------------------------------
"""

# MÓDULOS
#----------------------------------------------------------------------------------------------
import datetime
import json
import re

#----------------------------------------------------------------------------------------------
# CONSTANTES DE ARCHIVOS
#----------------------------------------------------------------------------------------------
ARCHIVO_TURISTAS = "turistas.json"
ARCHIVO_PAQUETES = "paquetes.json"
ARCHIVO_CONTRATOS = "contratos.json"

#----------------------------------------------------------------------------------------------
# FUNCIONES DE ARCHIVOS
#----------------------------------------------------------------------------------------------

def leer_datos_json(ruta_archivo):
    """
    Lee datos desde un archivo JSON.

    Parámetros:
        ruta_archivo (str): La ruta al archivo JSON.

    Retorno:
        dict: Un diccionario con los datos, o un diccionario vacío si falla.
    """
    archivo = None
    try:
        archivo = open(ruta_archivo, 'r', encoding="utf-8")
        return json.load(archivo)
    except FileNotFoundError:
        print(f"No se encontró el archivo '{ruta_archivo}'. Se creará uno nuevo si es necesario.")
        return {}   
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return {}
    finally:
        if archivo:
            archivo.close()

def escribir_datos_json(ruta_archivo, datos):
    """
    Escribe un diccionario de datos en un archivo JSON.

    Parámetros:
        ruta_archivo (str): La ruta al archivo JSON donde se escribirá.
        datos (dict): El diccionario de datos a escribir.
    """
    archivo = None
    try:
        archivo = open(ruta_archivo, 'w', encoding="utf-8")
        json.dump(datos, archivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error inesperado al escribir en el archivo: {e}")
    finally:
        if archivo:
            archivo.close()

#----------------------------------------------------------------------------------------------
# FUNCIONES DE VALIDACIÓN
#----------------------------------------------------------------------------------------------

def validar_email(email):
    """
    Valida si un formato de email es correcto usando expresiones regulares.

    Parámetros:
        email (str): La cadena a validar.

    Retorno:
        bool: True si es válido, False si no.
    """
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(patron, email):
        return True
    else:
        return False

def validar_solo_letras(texto):
    """
    Valida que una cadena contenga solo letras y espacios.
    
    Parámetros:
        texto (str): Cadena de texto a validar.

    Retorno:
        bool: True si la cadena contiene solo letras y espacios, False en caso contrario.
    """
    for caracter in texto:
        if not (caracter.isalpha() or caracter.isspace()):
            return False
    return True

def validar_dni(texto):
    """
    Valida que una cadena contenga solo números y opcionalmente puntos.

    Parámetros:
        texto (str): Cadena de texto a validar como DNI.

    Retorno:
        bool: True si la cadena contiene solo dígitos y/o puntos, False en caso contrario.
    """
    for caracter in texto:
        if not (caracter.isdigit() or caracter == '.'):
            return False
    return True

def generar_id(diccionario):
    """
    Genera un nuevo ID numérico autoincremental como string.
    
    Parámetros:
        diccionario (dict): Diccionario cuyas claves son IDs numéricos como strings.

    Retorno:
        str: Nuevo ID numérico como cadena.
    """
    if not diccionario:
        return "1"
    max_id = 0
    for key in diccionario.keys():
        try:
            if int(key) > max_id:
                max_id = int(key)
        except (ValueError, TypeError):            
            pass
    return str(max_id + 1)

def solicitar_numero(mensaje, tipo_dato=int):
    """
    Solicita un número al usuario y lo valida.
    
    Parámetros:
        mensaje (str): Mensaje para solicitar el valor.
        tipo_dato (type, optional): Tipo al que se convierte el valor (defecto: int).

    Retorno:
        tipo_dato: Valor ingresado convertido al tipo de dato especificado.
    """
    while True:
        try:
            valor = tipo_dato(input(mensaje))
            return valor
        except ValueError:
            print(f"Error: Debe ingresar un número válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")

#----------------------------------------------------------------------------------------------
# FUNCIONES DE GESTIÓN DE TURISTAS
#----------------------------------------------------------------------------------------------

def ingresar_turista(turistas):
    """
    Registra un nuevo turista y lo agrega al diccionario.
    
    Parámetros:
        turistas (dict): El diccionario de turistas.
        
    Retorno:
        dict: El diccionario de turistas actualizado.
    """
    print("\n--- Alta de Nuevo Turista ---")
    while True:
        nombre = input("Ingrese nombre: ").strip().title()
        if nombre and validar_solo_letras(nombre):
            break
        print("Error: El nombre es obligatorio y solo debe contener letras.")

    while True:
        apellido = input("Ingrese apellido: ").strip().title()
        if apellido and validar_solo_letras(apellido):
            break
        print("Error: El apellido es obligatorio y solo debe contener letras.")

    while True:
        dni = input("Ingrese DNI: ").strip()
        if dni and validar_dni(dni):
            break
        print("Error: El DNI es obligatorio y solo debe contener números y puntos.")

    while True:
        email = input("Ingrese email: ").strip()
        if validar_email(email):
            break
        else:
            print("Error: Formato de email inválido. Ejemplo: 'nombre@dominio.com'.")

    telefonos_nuevos = {}
    for i in range(1, 4):
        telefono = input(f"Ingrese el teléfono {i} (o presione ENTER para omitir): ").strip()
        telefonos_nuevos[f"telefono{i}"] = telefono

    nuevo_id = generar_id(turistas)
    turistas[nuevo_id] = {
        "idTurista": nuevo_id, "activo": True, "nombre": nombre,
        "apellido": apellido, "dni": dni, "email": email,
        "telefonos": telefonos_nuevos
    }
    escribir_datos_json(ARCHIVO_TURISTAS, turistas)
    print("\nTurista agregado con éxito.")
    return turistas

def modificar_turista(turistas):
    """
    Permite modificar los datos de un turista existente.
    
    Parámetros:
        turistas (dict): El diccionario de turistas.
        
    Retorno:
        dict: El diccionario de turistas actualizado.
    """
    print("\n--- Modificar Turista ---")
    id_modificar = input("Ingrese el ID del turista a modificar: ").strip()

    if id_modificar in turistas and turistas[id_modificar].get("activo", False):
        turista_a_modificar = turistas[id_modificar]
        
        while True:         
            print("\n¿Qué desea modificar? [1] Nombre [2] Apellido [3] Email [0] Guardar y salir")
            opcion = input("Seleccione: ").strip()

            if opcion == '1':
                nuevo_nombre = input("Nuevo nombre: ").strip().title()
                if nuevo_nombre and validar_solo_letras(nuevo_nombre):
                    turista_a_modificar['nombre'] = nuevo_nombre
                elif nuevo_nombre:
                    print("Error: el nombre solo puede contener letras.")
            elif opcion == '2':
                nuevo_apellido = input("Nuevo apellido: ").strip().title()
                if nuevo_apellido and validar_solo_letras(nuevo_apellido):
                    turista_a_modificar['apellido'] = nuevo_apellido
                elif nuevo_apellido:
                    print("Error: el apellido solo puede contener letras.")
            elif opcion == '3':
                while True:
                    nuevo_email = input("Nuevo email: ").strip()
                    if not nuevo_email:
                        break
                    if validar_email(nuevo_email):
                        turista_a_modificar['email'] = nuevo_email
                        break
                    else:
                        print("Error: Formato de email inválido.")
            elif opcion == '0':
                break
            else:
                print("Opción no válida.")

        escribir_datos_json(ARCHIVO_TURISTAS, turistas)
        print("\nTurista modificado con éxito.")
    else:
        print("Error: No se encontró un turista activo con ese ID.")
    return turistas

def eliminar_turista(turistas):
    """
    Realiza la baja lógica de un turista.
    
    Parámetros:
        turistas (dict): El diccionario de turistas.
        
    Retorno:
        dict: El diccionario de turistas actualizado.
    """
    print("\n--- Eliminar Turista ---")
    id_eliminar = input("Ingrese el ID del turista a eliminar: ").strip()
    
    if id_eliminar in turistas and turistas[id_eliminar].get("activo", False):    
        confirmacion = input(f"¿Seguro que desea eliminar al turista? (S/N): ").strip().upper()
        if confirmacion == 'S':
            turistas[id_eliminar]['activo'] = False
            escribir_datos_json(ARCHIVO_TURISTAS, turistas)
            print("\nTurista eliminado con éxito.")
        else:
            print("Operación cancelada.")
    else:
        print("Error: No se encontró un turista activo con ese ID.")
    return turistas

def listar_turistas_activos(turistas):
    """
    Muestra un listado de todos los turistas activos.

    Parámetros:
        turistas (dict): El diccionario de turistas.
    """
    print("\n--- Listado de Turistas Activos ---")
    if not turistas:
        print("No hay turistas registrados.")
        return

    print(f"\n{'ID':<5}{'Nombre':<15}{'Apellido':<15}{'DNI':<12}{'Email':<30}{'Teléfonos'}")
    print("-" * 100)

    encontrados = False
    for datos in turistas.values():
        if datos.get("activo", False):
            encontrados = True
            telefonos = datos.get("telefonos", {})

            
            telefonos_validos = []
            for tel in telefonos.values():
                if tel:
                    telefonos_validos.append(tel)
            telefonos_str = ", ".join(telefonos_validos)
    

            print(f"{datos['idTurista']:<5}{datos['nombre']:<15}{datos['apellido']:<15}{datos['dni']:<12}{datos['email']:<30}{telefonos_str}")

    if not encontrados:
        print("No hay turistas activos para mostrar.".center(100))
    print("-" * 100)
    
#----------------------------------------------------------------------------------------------
# FUNCIONES DE PAQUETES
#----------------------------------------------------------------------------------------------

def cargar_paquete(paquetes):
    """
    Registra un nuevo paquete.
    
    Parámetros:
        paquetes (dict): El diccionario de paquetes.
        
    Retorno:
        dict: El diccionario de paquetes actualizado.
    """
    print("\n--- Alta de Nuevo Paquete ---")
    
    while True:
        nombre = input("Nombre del paquete: ").strip()
        if nombre:
            break
        print("Error: El nombre del paquete es obligatorio.")
        
    destino = input("Destino: ").strip()
    duracion = input("Duración: ").strip()
    valor = solicitar_numero("Valor por persona: ", float)
    descripcion = input("Descripción: ").strip()
    
    servicios_nuevos = {
        "vuelo": input("Vuelo (o presione ENTER): ").strip(),
        "alojamiento": input("Alojamiento (o presione ENTER): ").strip(),
        "actividad": input("Actividad (o presione ENTER): ").strip(),
        "seguro de viaje": input("Seguro de viaje (o presione ENTER): ").strip(),
        "traslado": input("Traslado (o presione ENTER): ").strip()
    }
    
    nuevo_id = generar_id(paquetes)
    paquetes[nuevo_id] = {
        "idPaquete": nuevo_id, "activo": True, "nombre": nombre,
        "destino": destino, "duracion": duracion, "valor": valor,
        "descripcion": descripcion, "servicios": servicios_nuevos
    }
    escribir_datos_json(ARCHIVO_PAQUETES, paquetes)
    print("\nPaquete agregado con éxito.")
    return paquetes

def modificar_paquete(paquetes):
    """
    Permite modificar los datos de un paquete existente.
    
    Parámetros:
        paquetes (dict): El diccionario de paquetes.
        
    Retorno:
        dict: El diccionario de paquetes actualizado.
    """
    print("\n--- Modificar Paquete ---")
    id_modificar = input("Ingrese el ID del paquete a modificar: ").strip()

    if id_modificar in paquetes and paquetes[id_modificar].get("activo", False):
        paquete_a_modificar = paquetes[id_modificar]
        while True:
            print("\n¿Qué desea modificar? [1] Datos generales [2] Servicios [0] Guardar y salir")
            opcion = input("Seleccione: ").strip()

            if opcion == '1':
                nuevo_nombre = input("Nuevo nombre: ").strip()
                if nuevo_nombre: paquete_a_modificar['nombre'] = nuevo_nombre
                nuevo_destino = input("Nuevo destino: ").strip()
                if nuevo_destino: paquete_a_modificar['destino'] = nuevo_destino
                nueva_duracion = input("Nueva duración: ").strip()
                if nueva_duracion: paquete_a_modificar['duracion'] = nueva_duracion
                try:
                    nuevo_valor_str = input("Nuevo valor: ").strip()
                    if nuevo_valor_str:
                        paquete_a_modificar['valor'] = float(nuevo_valor_str)
                except ValueError:
                    print("Error: Valor inválido. Se mantendrá el anterior.")
                nueva_desc = input("Nueva descripción: ").strip()
                if nueva_desc: paquete_a_modificar['descripcion'] = nueva_desc
            elif opcion == '2':
                for servicio in paquete_a_modificar['servicios']:
                    nuevo_detalle = input(f"Nuevo detalle para {servicio}: ").strip()
                    if nuevo_detalle:
                        paquete_a_modificar['servicios'][servicio] = nuevo_detalle
            elif opcion == '0':
                break
            else:
                print("Opción no válida.")
        escribir_datos_json(ARCHIVO_PAQUETES, paquetes)
        print("\nPaquete modificado con éxito.")
    else:
        print("Error: No se encontró un paquete activo con ese ID.")
    return paquetes

def eliminar_paquete(paquetes):
    """
    Realiza la baja lógica de un paquete.
    
    Parámetros:
        paquetes (dict): El diccionario de paquetes.
        
    Retorno:
        dict: El diccionario de paquetes actualizado.
    """
    print("\n--- Eliminar Paquete ---")
    id_eliminar = input("Ingrese el ID del paquete a eliminar: ").strip()
    
    if id_eliminar in paquetes and paquetes[id_eliminar].get("activo", False):      
        confirmacion = input(f"¿Seguro que desea eliminar el paquete? (S/N): ").strip().upper()
        if confirmacion == 'S':
            paquetes[id_eliminar]['activo'] = False
            escribir_datos_json(ARCHIVO_PAQUETES, paquetes)
            print("\nPaquete desactivado con éxito.")
        else:
            print("Operación cancelada.")
    else:
        print("Error: No se encontró un paquete activo con ese ID.")
    return paquetes

def listar_paquetes_activos(paquetes):
    """
    Muestra un listado de todos los paquetes activos.

    Parámetros:
        paquetes (dict): El diccionario de paquetes.
    """
    print("\n--- Listado de Paquetes Activos ---")
    if not paquetes:
        print("No hay paquetes registrados.")
        return

    encontrados = False
    for datos in paquetes.values():
        if datos.get("activo", False):
            if not encontrados:
                print("-" * 75)
            encontrados = True
            print(f"ID: {datos['idPaquete']} | Nombre: {datos['nombre']}")
            print(f"  Destino: {datos['destino']} | Duración: {datos['duracion']} | Valor: ${datos['valor']:,.2f}")
            print(f"  Descripción: {datos['descripcion']}")
            servicios = datos.get("servicios", {})
        
            hay_servicios = False
            for detalle_servicio in servicios.values():
                if detalle_servicio:
                    hay_servicios = True
                    break 

            if hay_servicios:
                print("  Servicios Incluidos:")
                for tipo, detalle in servicios.items():
                    if detalle:
                        print(f"    - {tipo.capitalize()}: {detalle}")         

            print("-" * 75)

    if not encontrados:
        print("No hay paquetes activos para mostrar.")
        
#----------------------------------------------------------------------------------------------
# FUNCIONES DE CONTRATOS
#----------------------------------------------------------------------------------------------

def alta_contrato(contratos, turistas, paquetes):
    """
    Genera un nuevo contrato y lo guarda.
    
    Parámetros:
        contratos (dict): El diccionario de contratos.
        turistas (dict): El diccionario de turistas.
        paquetes (dict): El diccionario de paquetes.
        
    Retorno:
        dict: El diccionario de contratos actualizado.
    """
    print("\n--- Alta de Nuevo Contrato ---")
    id_turista = input("Ingrese ID del turista: ").strip()
    if not (id_turista in turistas and turistas[id_turista].get("activo", False)):
        print("Error: ID de turista no válido o inactivo.")
        return contratos

    id_paquete = input("Ingrese ID del paquete: ").strip()
    if not (id_paquete in paquetes and paquetes[id_paquete].get("activo", False)):
        print("Error: ID de paquete no válido o inactivo.")
        return contratos
    
    cantidad = solicitar_numero("Ingrese cantidad de viajeros: ", int)
    forma_pago = input("Ingrese medio de pago (Efectivo, Transferencia, Tarjeta): ").strip()

    total = paquetes[id_paquete]["valor"] * cantidad
    fecha_contrato = datetime.datetime.now()
    id_contrato = fecha_contrato.strftime("%Y%m%d%H%M%S")

    contratos[id_contrato] = {
        "idContrato": id_contrato, "activo": True, 
        "fecha": fecha_contrato.strftime("%Y.%m.%d %H:%M:%S"),
        "idTurista": id_turista, "idPaquete": id_paquete,
        "cantidadDePersonas": cantidad, "Total": total,
        "formaDePago": forma_pago
    }
    escribir_datos_json(ARCHIVO_CONTRATOS, contratos)
    print(f"\nContrato generado con éxito.")
    return contratos

def baja_contrato(contratos):
    """
    Realiza la baja lógica de un contrato.
    
    Parámetros:
        contratos (dict): El diccionario de contratos.
        
    Retorno:
        dict: El diccionario de contratos actualizado.
    """
    print("\n--- Baja de Contrato ---")
    id_contrato = input("Ingrese el ID del contrato a dar de baja: ").strip()

    if id_contrato in contratos and contratos[id_contrato].get("activo", False):
        confirmacion = input(f"¿Está seguro que desea cancelar el contrato? (S/N): ").strip().upper()
        if confirmacion == 'S':
            contratos[id_contrato]["activo"] = False          
            escribir_datos_json(ARCHIVO_CONTRATOS, contratos)
            print("\nContrato cancelado con éxito.")
        else:
            print("Operación cancelada.")
    else:
        print("Error: ID de contrato no encontrado o ya está inactivo.")
    return contratos

def modificar_contrato(contratos, paquetes):
    """
    Permite modificar un contrato existente.
    
    Parámetros:
        contratos (dict): El diccionario de contratos.
        paquetes (dict): El diccionario de paquetes.
        
    Retorno:
        dict: El diccionario de contratos actualizado.
    """
    print("\n--- Modificar Contrato ---")
    id_contrato = input("Ingrese el ID del contrato a modificar: ").strip()

    if id_contrato in contratos and contratos[id_contrato].get("activo", False):
        contrato_a_modificar = contratos[id_contrato]
        
        while True:
            print("\n¿Qué desea modificar? [1] Cantidad de personas [2] Forma de pago [0] Guardar y salir")
            opcion = input("Seleccione: ").strip()
            
            if opcion == '1':
                nueva_cantidad = solicitar_numero("Nueva cantidad de personas: ", int)
                contrato_a_modificar["cantidadDePersonas"] = nueva_cantidad
                id_paquete = contrato_a_modificar["idPaquete"]
                contrato_a_modificar["Total"] = paquetes[id_paquete]["valor"] * nueva_cantidad
                print(f"Total actualizado: ${contrato_a_modificar['Total']:,.2f}")
            elif opcion == '2':
                nueva_forma_pago = input("Nueva forma de pago: ").strip()
                if nueva_forma_pago:
                    contrato_a_modificar['formaDePago'] = nueva_forma_pago
            elif opcion == '0':
                break
            else:
                print("Opción no válida.")

        escribir_datos_json(ARCHIVO_CONTRATOS, contratos)
        print("\nContrato modificado con éxito.")
    else:
        print("Error: ID de contrato no encontrado o está inactivo.")
    return contratos
        
#----------------------------------------------------------------------------------------------
# FUNCIONES DE INFORMES
#----------------------------------------------------------------------------------------------

def listar_operaciones_del_mes(contratos, turistas, paquetes):
    """
    Muestra los contratos activos del mes y año actual.
    
    Parámetros:
        contratos (dict): El diccionario de contratos.
        turistas (dict): El diccionario de turistas.
        paquetes (dict): El diccionario de paquetes.
    """
    print("\n--- Listado de Operaciones del Mes en Curso ---")
    if not all([turistas, paquetes, contratos]):
        print("Faltan datos para generar el informe.")
        return

    hoy = datetime.datetime.now()
    print(f"\n{'Fecha':<12}{'Cliente':<25}{'Paquete Contratado':<30}{'Total':>15}")
    print("-" * 82)

    se_encontraron_operaciones = False
    for id_contrato, datos_contrato in contratos.items():
        if datos_contrato.get("activo", False):
            try:
                fecha_contrato = datetime.datetime.strptime(datos_contrato["fecha"], "%Y.%m.%d %H:%M:%S")
                if fecha_contrato.month == hoy.month and fecha_contrato.year == hoy.year:
                    se_encontraron_operaciones = True
                    id_turista = datos_contrato.get('idTurista')
                    id_paquete = datos_contrato.get('idPaquete')
                    nombre_cliente = ""
                    nombre_paquete = ""
                    if id_turista in turistas:
                        info_turista = turistas[id_turista]
                        nombre_cliente = f"{info_turista.get('nombre')} {info_turista.get('apellido')}"                    
                    if id_paquete in paquetes:
                        info_paquete = paquetes[id_paquete]
                        nombre_paquete = info_paquete.get('nombre')
                    total_formateado = f"${datos_contrato.get('Total', 0):,.2f}"
                    fecha_display = fecha_contrato.strftime("%d/%m/%Y")
                    print(f"{fecha_display:<12}{nombre_cliente:<25}{nombre_paquete:<30}{total_formateado:>15}")
            except (KeyError, ValueError):
                pass

    if not se_encontraron_operaciones:
        print("No se encontraron operaciones en el mes actual.".center(82))
    print("-" * 82)


def resumen_cantidad_contratos_por_mes(contratos, paquetes):
    """
    Muestra un resumen anual de la cantidad de contratos por paquete y mes.

    Parámetros:
        contratos (dict): El diccionario de contratos.
        paquetes (dict): El diccionario de paquetes.
    """
    print("\n--- Resumen Anual de Cantidad de Contratos por Paquete ---")
    if not paquetes:
        print("No hay paquetes registrados para generar el informe.")
        return
    
    año_actual = datetime.datetime.now().year
    meses_nombres = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
    
    print(f"\n{'Producto':<25}", end="")
    for mes in meses_nombres:
        print(f"{mes:>9}", end="")
    print(f"\n" + "-" * 135)

    for id_paquete, datos_paquete in paquetes.items():
        if datos_paquete.get("activo", False):
            cantidad_por_mes = [0] * 12
            if contratos:
                for datos_contrato in contratos.values():
                    if datos_contrato.get("activo", False) and datos_contrato.get("idPaquete") == id_paquete:
                        try:
                            fecha_contrato = datetime.datetime.strptime(datos_contrato["fecha"], "%Y.%m.%d %H:%M:%S")
                            if fecha_contrato.year == año_actual:
                                mes_index = fecha_contrato.month - 1
                                cantidad_por_mes[mes_index] += 1
                        except (KeyError, ValueError):
                            pass
            
            nombre_paquete = datos_paquete.get('nombre')
            print(f"{nombre_paquete:<25}", end="")
            for cantidad in cantidad_por_mes:
                print(f"{cantidad:>9}", end="")
            print()
    print("-" * 135)


def reporte_resumen_montos_por_mes(contratos, paquetes):
    """
    Muestra un informe de los montos totales de contratos por paquete y mes.
    
    Parámetros:
        contratos (dict): El diccionario de contratos.
        paquetes (dict): El diccionario de paquetes.
    """
    print("\n--- Resumen Anual de Montos Totales por Paquete ---")
    if not paquetes:
        print("No hay paquetes registrados para generar el informe.")
        return

    año_actual = datetime.datetime.now().year
    meses_nombres = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

    print(f"\n{'Producto':<25}", end="")
    for mes in meses_nombres:
        print(f"{mes:>11}", end="")
    print(f"\n" + "-" * 160)

    for id_paquete, datos_paquete in paquetes.items():
        if datos_paquete.get("activo", False):
            monto_por_mes = [0.0] * 12
            if contratos:
                for datos_contrato in contratos.values():
                    if datos_contrato.get("activo", False) and datos_contrato.get("idPaquete") == id_paquete:
                        try:
                            fecha_contrato = datetime.datetime.strptime(datos_contrato["fecha"], "%Y.%m.%d %H:%M:%S")
                            if fecha_contrato.year == año_actual:
                                mes_index = fecha_contrato.month - 1
                                monto_por_mes[mes_index] += datos_contrato.get("Total", 0.0)
                        except (KeyError, ValueError):
                            pass

            nombre_paquete = datos_paquete.get('nombre')
            print(f"{nombre_paquete:<25}", end="")
            for monto in monto_por_mes:
                monto_str = f"${monto:,.2f}"
                print(f"{monto_str:>11}", end="")
            print()
    print("-" * 160)

def informe_paquetes_menos_vendidos(contratos, paquetes):
    """
    Muestra un informe de los 5 paquetes activos menos vendidos.
    
    Parámetros:
        contratos (dict): El diccionario de contratos.
        paquetes (dict): El diccionario de paquetes.
    """
    print("\n--- Informe de los 5 Paquetes Menos Vendidos ---")
    ventas_por_paquete = {}
    for id_paquete, datos_paquete in paquetes.items():
        if datos_paquete.get("activo", False):
            ventas_por_paquete[id_paquete] = {
                "nombre": datos_paquete.get("nombre"),
                "ventas": 0
            }

    if not ventas_por_paquete:
        print("No hay paquetes activos para generar el informe.")
        return

    if contratos:
        for datos_contrato in contratos.values():
            if datos_contrato.get("activo", False):
                id_paquete_contratado = datos_contrato.get("idPaquete")
                if id_paquete_contratado in ventas_por_paquete:
                    ventas_por_paquete[id_paquete_contratado]["ventas"] += 1
 
    lista_paquetes_ventas = []
    for id_p, datos_p in ventas_por_paquete.items():
        lista_paquetes_ventas.append(datos_p)    
    
    n = len(lista_paquetes_ventas)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_paquetes_ventas[j]["ventas"] > lista_paquetes_ventas[j+1]["ventas"]:               
                temp = lista_paquetes_ventas[j]
                lista_paquetes_ventas[j] = lista_paquetes_ventas[j+1]
                lista_paquetes_ventas[j+1] = temp

    print(f"\n{'Posición':<10}{'Nombre del Paquete':<40}{'Cantidad de Ventas':<20}")
    print("-" * 75)    
  
    cantidad_a_mostrar = 5
    if len(lista_paquetes_ventas) < 5:
        cantidad_a_mostrar = len(lista_paquetes_ventas)

    for i in range(cantidad_a_mostrar):
        paquete = lista_paquetes_ventas[i]
        posicion = f"{i + 1}."
        print(f"{posicion:<10}{paquete['nombre']:<40}{paquete['ventas']:<20}")

    print("-" * 75)
    
#----------------------------------------------------------------------------------------------
# MAIN
#----------------------------------------------------------------------------------------------
def main():
    """
    Función principal que carga datos y ejecuta el menú del programa.
    """
    # Se cargan datos desde los archivos al iniciar
    turistas = leer_datos_json(ARCHIVO_TURISTAS)
    paquetes = leer_datos_json(ARCHIVO_PAQUETES)
    contratos = leer_datos_json(ARCHIVO_CONTRATOS)

    """
    # --------------------- DICCIONARIO TURISTAS ------------------------#
    turistas = {
         "1": {
        "idTurista": "1",
        "activo": True,
        "nombre": "Virginia",
        "apellido": "Griego",
        "dni": "14.309.227",
        "email": "griegomavi@hotmail.com",
        "telefonos": {
            "telefono1": "5491144902357",
            "telefono2": "43132662",
            "telefono3": "43034562"
        }
    },

    "2": {
        "idTurista": "2",
        "activo": True,
        "nombre": "Agostina",
        "apellido": "Griego",
        "dni": "36.314.353",
        "email": "griegoagos@hotmail.com",
        "telefonos": {
            "telefono1": "5491144905848",
            "telefono2": "43132662",
            "telefono3": ""
        }
    },

    "3": {
        "idTurista": "3",
        "activo": True,
        "nombre": "Fernando",
        "apellido": "Lopez",
        "dni": "3.699.227",
        "email": "lopezfernando@hotmail.com",
        "telefonos": {
            "telefono1": "5491144927437",
            "telefono2": "43136662",
            "telefono3": "43132662"
        }
    },

    "4": {
        "idTurista": "4",
        "activo": True,
        "nombre": "Daniel",
        "apellido": "Lopez",
        "dni": "14.456.697",
        "email": "danielopez@hotmail.com",
        "telefonos": {
            "telefono1": "5491199657842",
            "telefono2": "43132662",
            "telefono3": "43132662"
        }
    },

    "5": {
        "idTurista": "5",
        "activo": True,
        "nombre": "Martina",
        "apellido": "Sanchez",
        "dni": "40.536.846",
        "email": "martinasanchez@hotmail.com",
        "telefonos": {
            "telefono1": "54911996084737",
            "telefono2": "43032662",
            "telefono3": ""
        }
    },

    "6": {
        "idTurista": "6",
        "activo": True,
        "nombre": "Valentina",
        "apellido": "Dominguez",
        "dni": "40.589.659",
        "email": "valendominguez@hotmail.com",
        "telefonos": {
            "telefono1": "5491159608477",
            "telefono2": "43014810",
            "telefono3": "43189756"
        }
    },

    "7": {
        "idTurista": "7",
        "activo": True,
        "nombre": "Milagros",
        "apellido": "Pliego",
        "dni": "41.587.986",
        "email": "milipliego@hotmail.com",
        "telefonos": {
            "telefono1": "5491156978562",
            "telefono2": "43732662",
            "telefono3": "43874562"
        }
    },

    "8": {
        "idTurista": "8",
        "activo": True,
        "nombre": "Camila",
        "apellido": "Gennaro",
        "dni": "41.897.988",
        "email": "camigennaro@hotmail.com",
        "telefonos": {
            "telefono1": "5491156978562",
            "telefono2": "43874562",
            "telefono3": "43874562"
        }
    },

    "9": {
        "idTurista": "9",
        "activo": True,
        "nombre": "Daniela",
        "apellido": "Savino",
        "dni": "40.589.698",
        "email": "danisavino@hotmail.com",
        "telefonos": {
            "telefono1": "5491159608765",
            "telefono2": "43014896",
            "telefono3": ""
        }
    },

    "10": {
        "idTurista": "10",
        "activo": True,
        "nombre": "Agustina",
        "apellido": "Yarussi",
        "dni": "40.986.689",
        "email": "agusyarussi@hotmail.com",
        "telefonos": {
            "telefono1": "5491159608477",
            "telefono2": "43014810",
            "telefono3": ""
        }
    }
    }    
    # --------------------- DICCIONARIO PAQUETES ------------------------#
    paquetes = {
     "1": {
        "idPaquete": "1",
        "activo": True,
        "nombre": "Aventura en Salta",
        "destino": "Salta",
        "duracion": "5 días",
        "valor": 210000.0,
        "descripcion": "Excursiones y paisajes del norte argentino",
        "servicios": {
            "alojamiento": "Hotel Solar del Cerro",
            "actividad": "City tour y Visita a Cafayate",
            "vuelo": "JetSmart"
        }
    },

    "2": {
        "idPaquete": "2",
        "activo": True,
        "nombre": "Mendoza Full Wine",
        "destino": "Mendoza",
        "duracion": "4 días",
        "valor": 265000.0,
        "descripcion": "Degustaciones y hotel boutique en la montaña",
        "servicios": {
            "alojamiento": "Cavas Wine Lodge",
            "actividad": "Bodega Norton y Spa vinoterapia",
            "vuelo": "Aerolíneas Argentinas"
        }
    },

    "3": {
        "idPaquete": "3",
        "activo": True,
        "nombre": "Relax en Iguazú",
        "destino": "Misiones",
        "duracion": "6 días",
        "valor": 295000.0,
        "descripcion": "Naturaleza, hotel con pileta y parque temático",
        "servicios": {
            "alojamiento": "Hotel La Cantera Jungle Lodge",
            "actividad": "Cataratas y Parque de las Aves",
            "traslado": "Aeropuerto - Hotel"
        }
    },

    "4": {
        "idPaquete": "4",
        "activo": True,
        "nombre": "Bariloche Aventura",
        "destino": "Bariloche",
        "duracion": "7 días",
        "valor": 310000.0,
        "descripcion": "Trekking, kayak y nieve en la Patagonia",
        "servicios": {
            "alojamiento": "Refugio Piedras Blancas",
            "actividad": "Trekking al cerro y Rafting en el río",
            "vuelo": "Flybondi"
        }
    },

    "5": {
        "idPaquete": "5",
        "activo": True,
        "nombre": "Buenos Aires Clásico",
        "destino": "CABA",
        "duracion": "3 días",
        "valor": 180000.0,
        "descripcion": "Hotel céntrico y city tour cultural",
        "servicios": {
            "alojamiento": "Hotel NH Tango",
            "actividad": "City Tour y Cena Tango Show"
        }
    },

    "6": {
        "idPaquete": "6",
        "activo": True,
        "nombre": "Costa Atlántica",
        "destino": "Mar del Plata",
        "duracion": "5 días",
        "valor": 155000.0,
        "descripcion": "Playa, paseo costero y hotel con desayuno",
        "servicios": {
            "alojamiento": "Hotel Dos Reyes",
            "traslado": "Bus desde Buenos Aires",
            "actividad": "Acuario y puerto"
        }
    },

    "7": {
        "idPaquete": "7",
        "activo": True,
        "nombre": "Tucumán Colonial",
        "destino": "Tucumán",
        "duracion": "4 días",
        "valor": 198000.0,
        "descripcion": "Ruta de la independencia y cerros del NOA",
        "servicios": {
            "alojamiento": "Hotel Carlos V",
            "actividad": "Casa de Tucumán y Excursión a Tafí del Valle"
        }
    },

    "8": {
        "idPaquete": "8",
        "activo": True,
        "nombre": "Sur Glaciar Express",
        "destino": "El Calafate",
        "duracion": "4 días",
        "valor": 320000.0,
        "descripcion": "Perito Moreno y navegación",
        "servicios": {
            "alojamiento": "Hotel Kosten Aike",
            "actividad": "Glaciar Perito Moreno y Navegación por Lago Argentino",
            "vuelo": "Aerolíneas Argentinas"
        }
    },

    "9": {
        "idPaquete": "9",
        "activo": True,
        "nombre": "Córdoba Sierras y Relax",
        "destino": "Córdoba",
        "duracion": "5 días",
        "valor": 230000.0,
        "descripcion": "Villa General Belgrano, caminatas y spa",
        "servicios": {
            "alojamiento": "Cabañas Alpinas",
            "actividad": "Spa y senderismo y Villa General Belgrano",
            "traslado": "Auto alquilado"
        }
    },

    "10": {
        "idPaquete": "10",
        "activo": True,
        "nombre": "San Juan y Valle de la Luna",
        "destino": "San Juan",
        "duracion": "6 días",
        "valor": 245000.0,
        "descripcion": "Naturaleza, fósiles y aventura paleontológica",
        "servicios": {
            "alojamiento": "Hostería del Sol",
            "actividad": "Valle de la Luna y Museo de Dinosaurios",
            "traslado": "Minivan desde aeropuerto"
        }
    }
    }
    # --------------------- DICCIONARIO CONTRATOS ------------------------#
    contratos = {"20000000000000": {
        "activo": True,
        "fecha": "2025.06.30 00:00:00",
        "idTurista": "1",
        "idPaquete": "2",
        "cantidadDePersonas": 1,
        "Total": paquetes["2"]["valor"],
        "formaDePago": "Efectivo"
    },

    "20000023456789": {
        "activo": True,
        "fecha": "2025.01.12 14:15:00",
        "idTurista": "1",
        "idPaquete": "1",
        "cantidadDePersonas": 3,
        "Total": paquetes["1"]["valor"] * 3,
        "formaDePago": "Transferencia"
    },

    "20000034567890": {
        "activo": True,
        "fecha": "2025.01.20 09:00:00",
        "idTurista": "2",
        "idPaquete": "2",
        "cantidadDePersonas": 1,
        "Total": paquetes["2"]["valor"],
        "formaDePago": "Tarjeta"
    },

    "20000045678901": {
        "activo": True,
        "fecha": "2025.02.01 08:00:00",
        "idTurista": "3",
        "idPaquete": "3",
        "cantidadDePersonas": 6,
        "Total": paquetes["3"]["valor"] * 6,
        "formaDePago": "Transferencia"
    },

    "20000056789012": {
        "activo": True,
        "fecha": "2025.03.10 12:00:00",
        "idTurista": "4",
        "idPaquete": "4",
        "cantidadDePersonas": 5,
        "Total": paquetes["4"]["valor"] * 5,
        "formaDePago": "Efectivo"
    },

    "20000067890123": {
        "activo": True,
        "fecha": "2025.04.05 16:45:00",
        "idTurista": "5",
        "idPaquete": "5",
        "cantidadDePersonas": 10,
        "Total": paquetes["5"]["valor"] * 10,
        "formaDePago": "Tarjeta"
    },

    "20000078901234": {
        "activo": True,
        "fecha": "2025.04.18 09:15:00",
        "idTurista": "6",
        "idPaquete": "6",
        "cantidadDePersonas": 4,
        "Total": paquetes["6"]["valor"] * 4,
        "formaDePago": "Transferencia"
    },

    "20000089012345": {
        "activo": True,
        "fecha": "2025.05.30 11:00:00",
        "idTurista": "7",
        "idPaquete": "7",
        "cantidadDePersonas": 8,
        "Total": paquetes["7"]["valor"] * 8,
        "formaDePago": "Efectivo"
    },

    "20000090123456": {
        "activo": True,
        "fecha": "2025.04.01 13:20:00",
        "idTurista": "8",
        "idPaquete": "10",
        "cantidadDePersonas": 1,
        "Total": paquetes["10"]["valor"],
        "formaDePago": "Efectivo"
    },

    "20000001234567": {
        "activo": True,
        "fecha": "2025.03.22 15:10:00",
        "idTurista": "9",
        "idPaquete": "9",
        "cantidadDePersonas": 7,
        "Total": paquetes["9"]["valor"] * 7,
        "formaDePago": "Tarjeta"
    }
    }
    """

    while True:
        print("\n" + "="*30)
        print("MENÚ PRINCIPAL")
        print("="*30)
        print("[1] Gestión de Turistas")
        print("[2] Gestión de Paquetes")
        print("[3] Gestión de Contratos")
        print("[4] Reportes")
        print("[0] Salir del programa")
        print("="*30)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            while True:
                print("\n" + "-"*30)
                print("MENÚ DE TURISTAS")
                print("-"*30)
                print("[1] Alta de turista")
                print("[2] Modificar turista")
                print("[3] Eliminar turista")
                print("[4] Listado de turistas activos")
                print("[0] Volver al menú principal")
                sub_opcion = input("Seleccione: ").strip()

                if sub_opcion == "1": turistas = ingresar_turista(turistas)
                elif sub_opcion == "2": turistas = modificar_turista(turistas)
                elif sub_opcion == "3": turistas = eliminar_turista(turistas)
                elif sub_opcion == "4": listar_turistas_activos(turistas)
                elif sub_opcion == "0": break
                else: print("Opción no válida.")
                input("\nPresione ENTER para continuar")

        elif opcion == "2":
            while True:
                print("\n" + "-"*30)
                print("MENÚ DE PAQUETES")
                print("-"*30)
                print("[1] Alta de paquete")
                print("[2] Modificar paquete")
                print("[3] Eliminar paquete")
                print("[4] Listado de paquetes activos")
                print("[0] Volver al menú principal")
                sub_opcion = input("Seleccione: ").strip()

                if sub_opcion == "1": paquetes = cargar_paquete(paquetes)
                elif sub_opcion == "2": paquetes = modificar_paquete(paquetes)
                elif sub_opcion == "3": paquetes = eliminar_paquete(paquetes)
                elif sub_opcion == "4": listar_paquetes_activos(paquetes)
                elif sub_opcion == "0": break
                else: print("Opción no válida.")
                input("\nPresione ENTER para continuar")

        elif opcion == "3":
             while True:
                print("\n" + "-"*30)
                print("MENÚ DE CONTRATOS ")
                print("-"*30)
                print("[1] Alta de contrato")
                print("[2] Baja de contrato")
                print("[3] Modificar contrato")
                print("[0] Volver al menú principal")
                sub_opcion = input("Seleccione: ").strip()

                if sub_opcion == "1": contratos = alta_contrato(contratos, turistas, paquetes)
                elif sub_opcion == "2": contratos = baja_contrato(contratos)
                elif sub_opcion == "3": contratos = modificar_contrato(contratos, paquetes)
                elif sub_opcion == "0": break
                else: print("Opción no válida.")
                input("\nPresione ENTER para continuar")

        elif opcion == "4":
            while True:
                print("\n" + "-"*30 + "\nMENÚ DE REPORTES\n" + "-"*30)
                print("[1] Listar operaciones del Mes en curso")
                print("[2] Resumen Anual de Cantidad de Contratos")
                print("[3] Resumen Anual de Montos de Contratos")                
                print("[4] Listar los 5 paquetes menos vendidos")
                print("[0] Volver")
                sub_opcion = input("Seleccione una opción: ").strip()

                if sub_opcion == "1": listar_operaciones_del_mes(contratos, turistas, paquetes)
                elif sub_opcion == "2": resumen_cantidad_contratos_por_mes(contratos, paquetes)
                elif sub_opcion == "3": reporte_resumen_montos_por_mes(contratos, paquetes)
                elif sub_opcion == "4": informe_paquetes_menos_vendidos(contratos, paquetes)
                elif sub_opcion == "0": break
                else: print("Opción no válida.")
                input("\nPresione ENTER para continuar...")

        elif opcion == "0":           
            break
        else:
            print("Opción inválida.")
            input("\nPresione ENTER para continuar")

if __name__ == "__main__":
    main()