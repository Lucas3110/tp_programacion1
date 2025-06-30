"""
-----------------------------------------------------------------------------------------------
Título: Empresa de viajes
Fecha: 25/05/25
Autor: Maia Medina, Eugenia Alonso, Lucas Rodriguez, Juan Ciro Petrella y Caterina Turdo
Descripción: Sistema para gestion de paquetes de viajes

Pendientes:
Menu funcional e informes
-----------------------------------------------------------------------------------------------
"""

# MÓDULOS
#----------------------------------------------------------------------------------------------

import datetime  
import json

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

# ------------- FUNCIONES  PARA ARCHIVO JSON ---------------

def cargar_datos_json():
    """
    Carga los datos de turistas, paquetes y contratos desde el archivo 'data.json'.

    Intenta abrir y leer el archivo JSON que contiene los datos del sistema.
    Si el archivo no existe, lo crea automáticamente con estructuras vacías.
    Asegura que existan las claves necesarias ("turistas", "paquetes", "contratos") en el archivo.

    Parámetros:
    No recibe parámetros.

    Returns:
    turistas (diccionario): Datos de los turistas registrados.
    paquetes (diccionario): Datos de los paquetes turísticos cargados.
    contratos (diccionario): Datos de los contratos.
    """
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        # Control extra: si alguna clave falta, la agrega vacía
        if "turistas" not in data: data["turistas"] = {}
        if "paquetes" not in data: data["paquetes"] = {}
        if "contratos" not in data: data["contratos"] = {}
    except (FileNotFoundError, json.JSONDecodeError):
        # Si no existe el archivo o está corrupto, crea desde cero
        data = {"turistas": {}, "paquetes": {}, "contratos": {}}
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    return data["turistas"], data["paquetes"], data["contratos"]

def guardar_datos_json(turistas, paquetes, contratos):
    """
    Guarda en el archivo JSON los datos actuales del sistema.

    Escribe los diccionarios de turistas, paquetes y contratos en archivo 'data.json'.
    Si ocurre un error durante el proceso de guardado, se informa en pantalla.

    Parámetros:
    turistas (Diccionario): Diccionario con los datos de los turistas.
    paquetes (Diccionario): Diccionario con los paquetes turísticos cargados.
    contratos (Diccionario): Diccionario con los contratos. 

    Returns:
    None. 
    """
    try:
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(
                {"turistas": turistas, "paquetes": paquetes, "contratos": contratos},
                f,
                ensure_ascii=False,
                indent=4,
            )
    except Exception as e:
        print("ERROR al guardar datos en el archivo JSON:", e)

#----------------------------------------------------------------------------------------------
# FUNCIONES TURISTAS
#----------------------------------------------------------------------------------------------
def ingresarTurista(turistas, paquetes, contratos):
    """
    Permite ingresar un nuevo turista al sistema y registrar sus datos personales.

    Solicita al usuario el nombre, apellido, DNI, email y teléfonos de contacto.
    Valida que los teléfonos ingresados contengan solo números. Genera un nuevo ID y agrega el turista al diccionario. 
    Guarda los datos en el archivo correspondiente.

    Parámetros:
    turistas (diccionario): Diccionario con los turistas.
    paquetes (diccionario): Diccionario con los paquetes turísticos. 
    contratos (diccionario): Diccionario con los contratos. 

    Returns
    turistas (diccinario): Diccionario actualizado con el nuevo turista incorporado.
    """
    print("\n--- INGRESO DE NUEVO TURISTA ---")
    nuevo_id = generar_id(turistas)
    nombre = input("Ingrese nombre del turista: ").strip()
    apellido = input("Ingrese apellido: ").strip()
    dni = input("Ingrese DNI: ").strip()
    email = input("Ingrese email: ").strip()
    
    telefonos_del_nuevo_turista = {"telefono1": "", "telefono2": "", "telefono3": ""}

    print("\n--- Ingreso de Teléfonos ---")
    valTel1 = input("Tiene un primer teléfono de contacto? Ingrese S/N: ").strip().upper()
    if valTel1 == "S":
        telefono1_input = input("Ingrese su primer teléfono de contacto: ").strip()
        if telefono1_input.isdigit():
            telefonos_del_nuevo_turista["telefono1"] = telefono1_input
        else:
            print("Error: El teléfono 1 debe contener solo números. No se guardó.")
    
    valTel2 = input("Tiene un segundo telefono de contacto? Ingrese S/N: ").strip().upper()
    if valTel2 == "S":
        telefono2_input = input("Ingrese su segundo teléfono de contacto: ").strip()
        if telefono2_input.isdigit():
            telefonos_del_nuevo_turista["telefono2"] = telefono2_input
        else:
            print("Error: El teléfono 2 debe contener solo números. No se guardó.")

    valTel3 = input("Tiene un tercer teléfono de contacto? Ingrese S/N: ").strip().upper()
    if valTel3 == "S":
        telefono3_input = input("Ingrese su tercer teléfono de contacto: ").strip()
        if telefono3_input.isdigit():
            telefonos_del_nuevo_turista["telefono3"] = telefono3_input
        else:
            print("Error: El teléfono 3 debe contener solo números. No se guardó.")

    turistas[nuevo_id] = {
        "idTurista": nuevo_id,
        "activo": True,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "email": email,
        "telefonos": telefonos_del_nuevo_turista
    }
    guardar_datos_json(turistas, paquetes, contratos)
    print("\nTurista agregado con ID:", nuevo_id)
    return turistas

def generar_id(turistas):
    """
    Genera un nuevo ID para un turista basado en el ID numérico más alto registrado.

    Recorre las claves del diccionario de turistas, identifica el ID más alto y retorna
    un nuevo ID incrementado en una unidad.

    Parámetros:
    turistas (diccionario): Diccionario con los datos de los turistas registrados. 

    Returns:
    (str): Nuevo ID único para el próximo turista. 
    """
    if len(turistas) == 0:
        return "1"
    else:
        max_id = 0
        for key in turistas:
            if int(key) > max_id:
                max_id = int(key)
        return str(max_id + 1)

def modificarTurista(turistas, paquetes, contratos):
    """
    Permite modificar los datos personales de un turista registrado.

    Solicita al usuario el ID del turista que desea modificar, verifica que exista
    y muestra un menú para editar su nombre, apellido o email. Los cambios se actualizan
    en el diccionario y se guardan en el archivo correspondiente.

    Parámetros:
    turistas (diccionario): Diccionario con los datos de los turistas registrados.
    paquetes (diccionario): Diccionario con los paquetes turísticos cargados.
    contratos (diccionario): Diccionario con los contratos. 

    Returns:
    turistas (diccionario): Diccionario actualizado con los cambios realizados en el turista seleccionado.
    """
    print("\n--- MODIFICAR INFORMACION DE TURISTA ---")
    idTurista = input("Ingresar ID de turista que desea modificar: ")

    if idTurista not in turistas:
        print("Id incorrecto, ingrese ID")
        return turistas
     
    turista = turistas[idTurista]

    while True:
        print("\n¿Qué desea modificar del turista?")
        print("[1] Nombre")
        print("[2] Apellido")
        print("[3] email")
        print("[0] Salir del modificador")

        opcion = input("Opcion: ")

        if opcion == "0":
            break

        elif opcion == "1":
            nuevo = input("Nuevo nombre: ").strip()
            if nuevo != "":
                turista["nombre"] = nuevo
                print("✔ Nombre actualizado.")
            else:
                print("No se ingresó un nuevo nombre. No se realizaron cambios.")

        elif opcion == "2":
            nuevo = input("Nuevo apellido: ").strip()
            if nuevo != "":
                turista["apellido"] = nuevo
                print("✔ Apellido actualizado.")
            else:
                print("No se ingresó un nuevo apellido. No se realizaron cambios.")

        elif opcion == "3":
            nuevo = input("Nuevo email: ").strip()
            if nuevo != "":
                turista["email"] = nuevo
                print("✔ Email actualizado.")
            else:
                print("No se ingresó un nuevo email. No se realizaron cambios.")

        else:
            print("Opción inválida. Intente de nuevo.")

    guardar_datos_json(turistas, paquetes, contratos)
    print(f"\nTurista '{idTurista}' modificado con éxito.")
    return turistas

def listarTuristasActivos(turistas, paquetes, contratos):
    """
    Muestra por pantalla todos los turistas activos registrados en el sistema.

    Recorre el diccionario de turistas y, por cada uno con estado activo, imprime sus datos.
    Si no hay turistas activos, informa en pantalla.

    Parámetros:
    turistas (diccionario): Diccionario con los datos de los turistas registrados.
    paquetes (diccionario): Diccionario con los paquetes turísticos cargados. 
    contratos (diccionario): Diccionario con los contratos. 

    Returns:
    None.
    """
    print("\nListado de turistas activos:")
    print("ID   Nombre         Apellido       DNI         Email                  Teléfonos")
    print("-" * 80)
    hubo_activos = False
    for t in turistas.values():
        try:
            if t.get("activo", False):
                tels = ", ".join(t.get("telefonos", {}).values())
                print(f'{t.get("idTurista", "-"):<4} {t.get("nombre", "-"):<14} {t.get("apellido", "-"):<14} {t.get("dni", "-"):<12} {t.get("email", "-"):<22} {tels}')
                hubo_activos = True
        except Exception as e:
            print(f"[ERROR]: Un turista tiene datos mal cargados. Detalle: {e}")
    if not hubo_activos:
        print("No hay turistas activos en el sistema.")
    print("-" * 80)

def eliminarTuristas(turistas, paquetes, contratos):
    """
    Elimina (desactiva) a un turista registrado en el sistema.

    Solicita al usuario el ID del turista a eliminar, verifica que exista y que esté activo,
    muestra sus datos y solicita confirmación. En caso afirmativo, lo marca como inactivo
    en el diccionario. Luego guarda los cambios en el archivo correspondiente.

    Parámetros:
    turistas (diccionario): Diccionario con los datos de los turistas registrados.
    paquetes (diccionario): Diccionario con los paquetes turísticos cargados.
    contratos (diccionario): Diccionario con los contratos.

    Returns:
    turistas (diccionario): Diccionario actualizado con el turista seleccionado marcado como inactivo.
    """
    print("\n--- ELIMINAR TURISTA ---")
    while True:
        id_turista_eliminar = input("Ingrese el ID del turista que desea eliminar: ").strip()
        if id_turista_eliminar not in turistas:
            print("Error: El ID del turista no existe. Intente de nuevo.")
            continue
        try:
            if not turistas[id_turista_eliminar].get("activo", False):
                print("Error: El turista ya se encuentra inactivo.")
                return turistas
            turista = turistas[id_turista_eliminar]
            print(f"\nDatos del turista a eliminar:")
            print(f"  ID: {turista.get('idTurista', '-')}")
            print(f"  Nombre: {turista.get('nombre', '-')} {turista.get('apellido', '-')}")
            print(f"  DNI: {turista.get('dni', '-')}")
            confirmacion = input(f"¿Está seguro que desea eliminar (desactivar) al turista '{turista.get('nombre', '-')} {turista.get('apellido', '-')}' (ID: {id_turista_eliminar})? (s/n): ").strip().lower()
            if confirmacion == "s":
                turistas[id_turista_eliminar]["activo"] = False
                print(f"Turista '{id_turista_eliminar}' desactivado correctamente.")
            else:
                print("Eliminación cancelada.")
            break
        except Exception as e:
            print(f"[ERROR]: El turista tiene datos mal cargados. Detalle: {e}")
            break
    guardar_datos_json(turistas, paquetes, contratos)
    return turistas

#----------------------------------------------------------------------------------------------
# FUNCIONES PARA CREAR PAQUETES
#----------------------------------------------------------------------------------------------

def cargarServicios():
    """
    Solicita al usuario los detalles de los servicios incluidos en un paquete turístico.

    Los servicios solicitados son: vuelo, alojamiento, actividad, seguro de viaje y traslado.
    El usuario puede dejar en blanco cualquier campo si el paquete no incluye ese servicio.

    Parámetros:
    Sin parámetros. 

    Returns:
    servicios (diccionario): Diccionario con los servicios ingresados. 
    """
    servicios = {}
    servicios["vuelo"] = input("Ingrese detalle del vuelo (o deje vacío si no tiene): ").strip()
    servicios["alojamiento"] = input("Ingrese detalle del alojamiento (o deje vacío si no tiene): ").strip()
    servicios["actividad"] = input("Ingrese detalle de la actividad (o deje vacío si no tiene): ").strip()
    servicios["seguro de viaje"] = input("Ingrese detalle del seguro de viaje (o deje vacío si no tiene): ").strip()
    servicios["traslado"] = input("Ingrese detalle del traslado (o deje vacío si no tiene): ").strip()
    return servicios

def altaPaquete(turistas, paquetes, contratos):
    """
    Permite ingresar un nuevo paquete turístico al sistema.

    Solicita al usuario los datos principales del paquete (nombre, destino, duración, valor,
    descripción). Luego genera un nuevo ID de paquete, lo registra en el diccionario correspondiente y guarda la información.

    Parámetros:
    turistas (diccionario): Diccionario con los datos de los turistas registrados.
    paquetes (diccionario): Diccionario con los paquetes turísticos. 
    contratos (diccionario): Diccionario con los contratos. 

    Returns:
    paquetes (diccionario): Diccionario actualizado con el nuevo paquete agregado.
    """
    print("\n--- INGRESO DE NUEVO PAQUETE ---")
    nombre = str(input("Ingrese un nombre para el paquete: ")).strip()
    destino = str(input("Ingrese destino del paquete: ")).strip()
    duracion = str(input("Ingrese duración del paquete (ej. '7 días'): ")).strip()
    while True:
        valorString = input("Ingrese valor por persona: ").strip().replace(",", ".")
        try:
            valor = float(valorString)
            break
        except ValueError:
            print("ERROR!!! debe ingresar un número válido.")
    descripcion = input("Ingrese una breve descripción del paquete: ").strip()
    servicios = cargarServicios()
    id_paquete = str(len(paquetes) + 1)
    paquetes[id_paquete] = {
        "activo": True,
        "nombre": nombre,
        "destino": destino,
        "duracion": duracion,
        "valor": valor,
        "descripcion": descripcion,
        "servicios": servicios
    }
    guardar_datos_json(turistas, paquetes, contratos)
    print(f"\nPaquete '{id_paquete}' creado exitosamente.\n")
    return paquetes

def modificarPaquete(turistas, paquetes, contratos):
    """
    Permite modificar los datos de un paquete turístico existente.

    Solicita al usuario el ID del paquete activo que desea modificar, muestra sus datos actuales
    y permite editar campos como nombre, destino, duración, valor, descripción
    y servicios. Los cambios se guardan al finalizar el proceso.

    Parámetros:
    turistas (diccionario): Diccionario con los datos de los turistas registrados.
    paquetes (diccionario): Diccionario con los paquetes turísticos cargados.
    contratos (diccionario): Diccionario con los contratos. 

    Returns:
    paquetes (diccionario): Diccionario actualizado con los datos modificados del paquete seleccionado.
    """
    print("\n--- MODIFICAR PAQUETE ---")
    print("\nPaquetes activos disponibles:")
    for idPQT, datos in paquetes.items():
        if datos["activo"]:
            print(f"- {idPQT}: {datos['nombre']} | {datos['destino']} ({datos['duracion']}) - ${datos['valor']}")
    id_paquete = input("\nIngrese el ID del paquete a modificar: ").strip()
    if id_paquete not in paquetes:
        print("El paquete no existe.")
        return paquetes
    if not paquetes[id_paquete]["activo"]:
        print("El paquete está inactivo.")
        return paquetes
    paquete = paquetes[id_paquete]
    print(f"\nDatos actuales del paquete {id_paquete}:")
    for clave, valor in paquete.items():
        if clave != "servicios":
            print(f"- {clave}: {valor}")
    print("- servicios:")
    for tipo, detalles in paquete["servicios"].items():
        print(f"  {tipo}: {detalles}")
    while True:
        print("\n¿Qué desea modificar del paquete?")
        print("[1] Nombre")
        print("[2] Destino")
        print("[3] Duración")
        print("[4] Valor")
        print("[5] Descripción")
        print("[6] Servicios (reemplaza los existentes)")
        print("[0] Salir del modificador")
        opcion = input("Opción: ").strip()
        if opcion == "0":
            break
        elif opcion == "1":
            nuevo = input("Nuevo nombre: ").strip()
            if nuevo != "":
                paquete["nombre"] = nuevo
                print("Nombre actualizado.")
        elif opcion == "2":
            nuevo = input("Nuevo destino: ").strip()
            if nuevo != "":
                paquete["destino"] = nuevo
                print("Destino actualizado.")
        elif opcion == "3":
            nuevo = input("Nueva duración: ").strip()
            if nuevo != "":
                paquete["duracion"] = nuevo
                print("Duración actualizada.")
        elif opcion == "4":
            nuevo = input("Nuevo valor por persona: ").strip().replace(",", ".")
            try:
                paquete["valor"] = float(nuevo)
                print("Valor actualizado.")
            except ValueError:
                print("Valor inválido. No se modificó.")
        elif opcion == "5":
            nuevo = input("Nueva descripción: ").strip()
            if nuevo != "":
                paquete["descripcion"] = nuevo
                print("Descripción actualizada.")
        elif opcion == "6":
            nuevos_servicios = cargarServiciosParaModificar(paquete["servicios"])
            paquete["servicios"] = nuevos_servicios
            print("Servicios actualizados.")
        else:
            print("Opción inválida. Intente de nuevo.")
    guardar_datos_json(turistas, paquetes, contratos)
    print(f"\nPaquete '{id_paquete}' modificado con éxito.")
    return paquetes

def cargarServiciosParaModificar(servicios_anteriores):
    """
    Permite modificar los servicios de un paquete turístico.

    Muestra los servicios previamente cargados y permite al usuario modificar cada uno.
    Si el usuario no ingresa un nuevo valor, se conserva el dato actual.

    Parámetros:
    servicios_anteriores (diccionario): Diccionario con los servicios previamente cargados. 

    Returns:
    servicios(ddiccionario): Nuevo diccionario con los servicios actualizados según lo indicado por el usuario.
    """
    servicios = {}
    for tipo, anterior in servicios_anteriores.items():
        entrada = input(f"Ingrese detalle del {tipo} (actual: '{anterior}') (Enter para mantener): ").strip()
        servicios[tipo] = entrada if entrada else anterior
    return servicios

def eliminarPaquete(turistas, paquetes, contratos):
    """
    Elimina un paquete del sistema (se marca como inactivo).

    Parámetros:
    turistas (diccionario): Diccionario con los datos de los turistas registrados.
    paquetes (diccionario): Diccionario con los paquetes turísticos cargados. 
    contratos (diccionario): Diccionario con los contratos. 

    Returns:
    paquetes (diccionario): Diccionario actualizado con el paquete seleccionado marcado como inactivo.
    """
    print("\n--- ELIMINAR PAQUETE ---")
    print("\nPaquetes activos disponibles:")
    hay_activos = False
    for id_PQT, datos in paquetes.items():
        if datos["activo"]:
            hay_activos = True
            print(f"- {id_PQT}: {datos['nombre']} | {datos['destino']} ({datos['duracion']})")
    if not hay_activos:
        print("No hay paquetes activos para eliminar.")
        return paquetes
    id_paquete = input("\nIngrese el ID del paquete que desea eliminar: ").strip()
    if id_paquete not in paquetes:
        print("Ese paquete no existe.")
        return paquetes
    if not paquetes[id_paquete]["activo"]:
        print("Ese paquete ya está inactivo.")
        return paquetes
    confirmacion = input(f"¿Está seguro que desea eliminar el paquete '{id_paquete}'? (s/n): ").strip().lower()
    if confirmacion == "s":
        paquetes[id_paquete]["activo"] = False
        print("Paquete eliminado correctamente.")
    else:
        print("Eliminación cancelada.")
    guardar_datos_json(turistas, paquetes, contratos)
    return paquetes

def listarPaquetesActivos(turistas, paquetes, contratos):
    """
    Muestra por pantalla todos los paquetes activos del sistema.

    Recorre el diccionario de paquetes y, por cada uno que tenga el atributo
    "activo" en True, muestra sus datos mediante la función mostrarPaquete().
    Si no hay ningún paquete activo, se informa por consola.

    Parámetros:
    turistas (diccionario): Diccionario con la información de los turistas registrados.
    paquetes (diccionario): Diccionario donde cada clave es un ID de paquete.
    contratos (diccionario): Diccionario con los contratos asociados a los paquetes y turistas.

    Returns:
    None.
    """
    print("\n--- LISTADO DE PAQUETES ACTIVOS ---\n")
    hay_activos = False
    for id_paquete, datos in paquetes.items():
        if datos["activo"]:
            hay_activos = True
            mostrarPaquete(id_paquete, datos)
            print("-" * 50)
    if not hay_activos:
        print("No hay paquetes activos cargados.")

def mostrarPaquete(id_paquete, datos):
    """
    Muestra por pantalla los datos completos de un paquete.
    
    Parámetros:
    id_paquete (str): ID del paquete a mostrar.
    datos (diccionario): Diccionario con la información del paquete.
    
    Returns:
    None
    """
    try:
        print("ID:", id_paquete)
        print("Nombre:", datos["nombre"])
        print("Destino:", datos["destino"])
        print("Duración:", datos["duracion"])
        print("Valor por persona: $", datos["valor"])
        print("Descripción:", datos["descripcion"])
        print("Servicios:")
        mostrarServicios(datos["servicios"])
    except KeyError as campoFaltante:
        print(f"ERROR!!! Falta el dato '{campoFaltante}' en el paquete. No se pudo mostrar completamente.")

def mostrarServicios(servicios):
    """
    Muestra por pantalla los servicios de un paquete.
    
    Parámetros:
    servicios (diccionario): Diccionario que contiene los tipos de servicios como claves.
    
    Returns:
    None
    """
    print("\nServicios:")
    for tipo, detalle in servicios.items():
        if detalle:
            print(f"- {tipo}: {detalle}")

# -------------------------------------
# Funciones Contrato
# -------------------------------------

def altaContrato(turistas, paquetes, contratos):
    """
    Permite crear un nuevo contrato de venta de paquete.
    
    Solicita los datos necesarios, valida y guarda el contrato en el archivo.
    Calcula el valor total del contrato.
    Registra la fecha y hora de alta del contrato.
    Genera un ID de contrato basado en la fecha y hora actual.
    Crea el contrato con los datos.
    Guarda el contrato en el archivo JSON.
    Muestra al usuario el valor total, la fecha de alta y el ID generado.
    
    Parámetros:
    Sin parámetros.
    
    Returns:
    None
    """
    mediosDePago = ["Efectivo", "Transferencia", "Tarjeta"]
    _idTurista = (input("Ingrese su ID de turista: "))
    _verificaNumeroDeTuristaBool, _verificaNumeroDeTuristaValor = verificaIDturista(turistas, _idTurista)
    while _verificaNumeroDeTuristaBool == False:
        _idTurista = (input("ID turista no válido. Ingrese su ID de turista: "))
        _verificaNumeroDeTuristaBool, _verificaNumeroDeTuristaValor = verificaIDturista(turistas, _idTurista)
    _idPaquete = (input("Ingrese el ID del paquete a abonar: "))
    _verificaNumeroDePaqueteBool, _verificaNumeroDePaqueteValor = verificaIDpaquete(_idPaquete, paquetes)
    while _verificaNumeroDePaqueteBool == False:
        _idPaquete = (input("Paquete no válido. Ingrese el ID del paquete a abonar: "))
        _verificaNumeroDePaqueteBool, _verificaNumeroDePaqueteValor = verificaIDpaquete(_idPaquete, paquetes)
    while True:
        entrada = input("Ingrese la cantidad de asistentes: ").strip()
        try:
            _cantidadDeViajeros = int(entrada)
            break
        except ValueError:
            print("ERROR. Ingrese un número entero válido.")
    cantidadAsistentesValidado = validaCantidadAsistentes(_cantidadDeViajeros)
    _medioDePago = (input("Ingrese medio de pago a utilizar (Efectivo, Transferencia, Tarjeta): ")).strip().capitalize()
    while _medioDePago not in mediosDePago:
        _medioDePago = input("Medio no válido. Ingrese uno de los siguientes (Efectivo, Transferencia, Tarjeta): ").strip().capitalize()
    try:
        _valorPaquete = paquetes[_verificaNumeroDePaqueteValor]["valor"]
    except KeyError:
        print("ERROR: el paquete seleccionado no tiene un valor definido.")
        return contratos
    _total = _valorPaquete * cantidadAsistentesValidado
    print("El valor total por",cantidadAsistentesValidado, "personas es de: " ,_total )
    _fechaDeContrato = datetime.datetime.now()
    print(_fechaDeContrato)
    _idContrato = _fechaDeContrato.strftime("%Y%m%d%H%M%S")
    print("ID del contrato: ", _idContrato)
    contratos[_idContrato] = {
        "activo": True,
        "fecha": _fechaDeContrato.strftime("%Y.%m.%d %H:%M:%S"),
        "idTurista": _idTurista,
        "idPaquete": _verificaNumeroDePaqueteValor,
        "cantidadDePersonas": cantidadAsistentesValidado,
        "Total": _total,
        "formaDePago": _medioDePago
    }
    guardar_datos_json(turistas, paquetes, contratos)
    print("Contrato agregado correctamente.")
    return contratos

def verificaIDpaquete(_idPaquete, _paquetes): 
    """
    Verifica si el ID de paquete existe en el sistema.
    
    Parámetros:
    _idPaquete (str): ID del paquete a verificar.
    _paquetes (dict): Diccionario que contiene todos los paquetes registrados, donde cada clave es un ID de paquete y su valor es un subdiccionario con los datos del paquete.

    Returns:
    bool: True si el paquete existe en el sistema, False si no existe.
    _idPaquete (str): El ID de paquete ingresado, para facilitar su reutilización posterior.
    """
    if _idPaquete in _paquetes:
        return True, _idPaquete
    else:
        return False, _idPaquete 
 
def validaCantidadAsistentes(ingreso): 
    """
    Valida que la cantidad de asistentes sea un número entre 0 y 100.
    Si no lo es, pide al usuario que ingrese un valor válido.
    
    Parámetros:
    ingreso (int): Valor inicial de cantidad de asistentes a validar.

    Returns:
    ingreso (int): Cantidad de asistentes validada, garantizando que sea un número entre 0 y 100.
    """ 
    while ingreso < 0 or ingreso > 100:
        ingreso= int(input("No válido. Ingrese la cantidad de asistentes: "))
    return ingreso

def verificaIDturista (_turistas, _idTurista): 
    """
    Verifica si el ID de turista existe y está activo.

    Parámetros:
    _turistas (diccionario): Diccionario que contiene todos los turistas registrados. 
    _idTurista (str): ID del turista a verificar.

    Retorna:
    bool: True si el turista existe y está activo, False si no existe o está inactivo.
    _idTurista(str): El ID de turista ingresado, para facilitar su reutilización posterior.

    
    """
    if _idTurista in _turistas and _turistas[_idTurista]["activo"] == True: 
        return True, _idTurista
    else:
        return False, _idTurista

def verificaIDcontrato(_idContrato, _contratos): 
    """
    Verifica si el ID de turista existe y está activo.
    Devuelve una tupla (True/False, ID).
    
    Parámetros:
    idContrato (str): ID del contrato a verificar.
    contratos (diccionario): Diccionario que contiene todos los contratos registrados.

    Returns:
    bool: True si el contrato existe y está activo, False si no existe o está inactivo.
    _idContrato(str): El ID de contrato ingresado, para facilitar su reutilización posterior.
    """ 
    if _idContrato in _contratos and _contratos[_idContrato]["activo"] == True:  
        return True, _idContrato
    elif _idContrato not in _contratos or _contratos[_idContrato]["activo"] == False: 
        return False, _idContrato

def bajaContrato(turistas, paquetes, contratos):
    """
    Permite dar de baja (desactivar) un contrato existente.
    Solicita el ID, valida y marca el contrato como inactivo.
    
    Si el contrato es válido:
    Registra la fecha y hora de la baja.
    Marca el contrato como inactivo. 
    Guarda los cambios en el archivo JSON. 
    Informa al usuario que el contrato ha sido dado de baja.
    
    Si el contrato no existe o está inactivo:
    Informa al usuario que no se ha encontrado el contrato y solicita intentar nuevamente.
    
    Parámetros:
    Sin parámetros.
    
    Returns:
    None
    """
    _idContrato = str(input("Ingrese el ID del contrato a dar de baja: "))
    _verificaNumeroDeContratoBool, _verificaNumeroDeContratoValor = verificaIDcontrato(_idContrato, contratos)
    
    if _verificaNumeroDeContratoBool == True: 
        _fechaDeBaja = datetime.datetime.now()
        print("Cancelado con éxito. Fecha de cancelación: ", _fechaDeBaja)
        contratos[_idContrato]["activo"] = False
        guardar_datos_json(turistas, paquetes, contratos)
        print("Contrato dado de baja correctamente.")
    else:
        print("Contrato no encontrado. Intente nuevamente.")
    return

def modificarContrato(turistas, paquetes, contratos):
    """
    Permite modificar los datos de un contrato existente.
    Solicita al usuario el ID del contrato a modificar y verifica su existencia y estado.
    Muestra opciones de modificación (1,2 Y 3).
    Registra la fecha y hora de la modificación en el contrato.
    Guarda los cambios en el archivo.
    
    Parámetros:
    Sin parámetros.
    
    Returns:
    None
    """
    _fechaDeModificacion = datetime.datetime.now()
    _idContrato = str(input("Ingrese el ID del contrato a modificar: "))
    idContratoVerificadoBool, idContratoVerificadoValor = verificaIDcontrato(_idContrato, contratos)
    
    if idContratoVerificadoBool == False:
        print("Contrato no encontrado o desactivado. Intente de nuevo.")
    else:
        contrato = contratos[idContratoVerificadoValor]
        print("Opciones a modificar: ")
        print('''
[1] Paquete
[2] Cantidad de personas 
[3] Forma de pago 
            ''')
        opcionAmodificar = str(input("Ingrese opción a modificar: "))
        while opcionAmodificar != "1" and opcionAmodificar != "2" and opcionAmodificar != "3":
            opcionAmodificar = str(input("Opción ingresada no válida. Ingrese opción a modificar: "))
        
        #Opción 1
        if opcionAmodificar == "1":
            nuevoPaquete = str(input("Ingrese el nuevo ID de paquete: ")).strip()
            idPaqueteValidadoBool, idPaqueteValidado = verificaIDpaquete(nuevoPaquete, paquetes)
            if idPaqueteValidadoBool == True:
                contrato["idPaquete"] = nuevoPaquete
                print("Cambio realizado con éxito.")
                contrato["fecha"] = _fechaDeModificacion.strftime("%Y.%m.%d %H:%M:%S")
                contrato["Total"] = paquetes[nuevoPaquete]["valor"] * contrato["cantidadDePersonas"]
            else:
                print("Paquete no encontrado. Intente de nuevo.")
        
        #Opción 2
        elif opcionAmodificar == "2":
            nuevaCantidadDePersonas = int(input("Ingrese la nueva cantidadDePersonas: "))
            nuevaCantidadDePersonaValidado = validaCantidadAsistentes(nuevaCantidadDePersonas)
            
            contrato["cantidadDePersonas"] = nuevaCantidadDePersonaValidado
            contrato["fecha"] = _fechaDeModificacion.strftime("%Y.%m.%d %H:%M:%S")
            contrato["Total"] = paquetes[contrato["idPaquete"]]["valor"] * contrato["cantidadDePersonas"]
            
            print("Cambio realizado con éxito.")
        
        #Opción 3
        elif opcionAmodificar == "3":
            print("Formas de pago disponibles: Efectivo, Transferencia, Tarjeta")
            nuevaFormaDePago = input("Ingrese la nueva forma de pago: ").strip().capitalize()
            if nuevaFormaDePago in ["Efectivo", "Transferencia", "Tarjeta"]:
                contrato["formaDePago"] = nuevaFormaDePago
                contrato["fecha"] = _fechaDeModificacion.strftime("%Y.%m.%d %H:%M:%S")
                print("Cambio realizado con éxito.")
            else:
                print("Forma de pago no válida. No se realizó el cambio.")
                return contratos
        guardar_datos_json(turistas, paquetes, contratos)
    return contratos

#----------------------------------------------------------------------------------------------
# FUNCIONES DE INFORMES
#----------------------------------------------------------------------------------------------
def listar_operaciones_mes():
    """
    Muestra un listado de todas las operaciones (contratos) realizadas en el mes actual.

    Carga los datos desde el archivo 'data.json' y recorre los contratos activos,
    filtrando aquellos cuya fecha coincida con el mes y año actual.
    Por cada contrato, imprime la fecha, nombre del cliente, nombre del paquete turístico, cantidad de personas,
    valor unitario y total de la operación. Si no hay operaciones en el mes, informa por pantalla.
    En caso de datos mal cargados, los omite e informa el error.

    Parámetros:
    No recibe parámetros.

    Returns:
    None. 
    """
    try:
        turistas, paquetes, contratos = cargar_datos_json()
        print()
        print("-" * 95)
        print("LISTADO DE OPERACIONES DEL MES EN CURSO")
        print("-" * 95)
        print(f"{'Fecha/Hora':<18}{'Cliente':<20}{'Producto':<25}{'Cant.':>6}{'Unit.':>10}{'Total':>12}")
        print("-" * 95)
        hoy = datetime.datetime.now()
        año_actual = hoy.year
        mes_actual = hoy.month
        hubo_datos = 0
        for id_contrato in contratos:
            try:
                contrato = contratos[id_contrato]
                if contrato.get("activo", False):
                    fecha_str = contrato.get("fecha", "")
                    partes_fecha = fecha_str.split(" ")
                    partes_fecha_simple = partes_fecha[0].split(".")
                    if len(partes_fecha_simple) == 3:
                        año = int(partes_fecha_simple[0])
                        mes = int(partes_fecha_simple[1])
                        if año == año_actual and mes == mes_actual:
                            id_turista = contrato.get("idTurista", "")
                            if id_turista in turistas:
                                cliente = turistas[id_turista].get("nombre", "") + " " + turistas[id_turista].get("apellido", "")
                            else:
                                cliente = "(desconocido)"
                            id_paquete = contrato.get("idPaquete", "")
                            if id_paquete in paquetes:
                                producto = paquetes[id_paquete].get("nombre", "")
                                unit = paquetes[id_paquete].get("valor", 0)
                            else:
                                producto = "(desconocido)"                       
                                unit = 0
                            cant = contrato.get("cantidadDePersonas", 0)
                            total = contrato.get("Total", 0)
                            print(f"{contrato.get('fecha', ''):<18}{cliente:<20}{producto:<25}{cant:>6}{unit:>10,.0f}{total:>12,.0f}")
                            hubo_datos += 1
            except Exception as e:
                print(f"[ERROR]: Se encontró un contrato mal cargado ({id_contrato}). Detalle: {e}")
        if hubo_datos == 0:
            print("No se registraron operaciones este mes.")
        print("-" * 95)
    except Exception as e:
        print("No hay información suficiente para generar el informe. Detalle:", e)

def resumen_cantidad_contratos_por_mes():
    """
    Muestra un resumen anual de la cantidad de contratos realizados por paquete y por mes.

    Carga los datos desde el archivo 'data.json' y recorre los contratos activos,
    agrupando por paquete y contando la cantidad de contratos por cada mes del año actual.
    Presenta la información (nombres de los paquetes y cantidades de contratos mensuales).

    Parámetros:
    No recibe parámetros.

    Returns:
    None. 
    """
    try:
        turistas, paquetes, contratos = cargar_datos_json()
        print()
        print("-" * 140)
        print("CANTIDADES TOTALES POR MES")
        print("-" * 140)
        meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
        año_actual = datetime.datetime.now().year
        print(f"{'Producto':<25}", end="")
        for i in range(12):
            nombre_mes = meses[i] + "." + str(año_actual)[-2:]
            print(f"{nombre_mes:>9}", end="")
        print()
        print("-" * 140)
        hay_paquetes = False
        for id_paquete in paquetes:
            try:
                if paquetes[id_paquete].get("activo", False):
                    hay_paquetes = True
                    nombre = paquetes[id_paquete].get("nombre", "")
                    cantidad_por_mes = [0] * 12
                    for id_contrato in contratos:
                        contrato = contratos[id_contrato]
                        if contrato.get("activo", False) and contrato.get("idPaquete") == id_paquete:
                            fecha_str = contrato.get("fecha", "")
                            partes_fecha = fecha_str.split(" ")
                            partes_fecha_simple = partes_fecha[0].split(".")
                            if len(partes_fecha_simple) == 3:
                                año = int(partes_fecha_simple[0])
                                mes = int(partes_fecha_simple[1])
                                if año == año_actual:
                                    cantidad_por_mes[mes-1] += 1
                    print(f"{nombre:<25}", end="")
                    for i in range(12):
                        print(f"{cantidad_por_mes[i]:>9}", end="")
                    print()
            except Exception as e:
                print(f"[ERROR]: Problema al procesar paquete {id_paquete}. Detalle: {e}")
        if not hay_paquetes:
            print("No hay paquetes activos para mostrar en el informe.")
        print("-" * 140)
    except Exception as e:
        print("No hay información suficiente para generar el informe. Detalle:", e)


def reporteResumenMontosPorMes():
    """
    Genera un informe con los montos totales de contratos agrupados por paquete, mes y año (últimos 12 meses).

    Carga los datos desde el archivo 'data.json' y recorre los contratos activos,
    Presenta la información, mostrando los montos mes a mes para cada paquete activo en los últimos 12 meses.

    Parámetros:
    No recibe parámetros.

    Returns:
    None.
    """
    try:
        turistas, paquetes, contratos = cargar_datos_json()
        print("\n--- GENERANDO INFORME DE RESUMEN DE MONTOS POR MES Y AÑO (ÚLTIMOS 12 MESES) ---")
        datos_agrupados = {}
        for id_contrato, contrato_info in contratos.items(): 
            try:
                if contrato_info.get("activo", False):
                    fecha_contrato_str = contrato_info.get("fecha", "")
                    if fecha_contrato_str:
                        fecha_contrato_obj = datetime.datetime.strptime(fecha_contrato_str, "%Y.%m.%d %H:%M:%S")
                        año_contrato = fecha_contrato_obj.year
                        mes_contrato = fecha_contrato_obj.month
                        id_paquete = contrato_info.get("idPaquete", "")
                        total_str = contrato_info.get("Total", 0)
                        monto = float(total_str) 
                        datos_agrupados.setdefault(año_contrato, {}).setdefault(id_paquete, {})
                        datos_agrupados[año_contrato][id_paquete].setdefault(mes_contrato, 0.0)
                        datos_agrupados[año_contrato][id_paquete][mes_contrato] += monto
            except (ValueError, TypeError) as e:
                print(f"[ERROR]: Se encontró un contrato con fecha o monto mal formateado ({id_contrato}). Detalle: {e}")
            except Exception as e:
                print(f"[ERROR]: Problema al procesar contrato {id_contrato}. Detalle: {e}")
                
        if not datos_agrupados:
            print("No hay datos de contratos activos para generar el informe.")
            return
        hoy = datetime.datetime.now()
        año_actual_num = hoy.year
        mes_actual_num = hoy.month
        año_inicio_rango = año_actual_num
        mes_inicio_rango = mes_actual_num - 11 
        if mes_inicio_rango <= 0:
            mes_inicio_rango += 12
            año_inicio_rango -= 1
        nombres_meses_abreviados = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
        ancho_col_producto = 25
        ancho_col_mes = 11 
        años_con_datos_en_diccionario = set(datos_agrupados.keys())
        años_del_informe_potenciales = set()
        años_del_informe_potenciales.add(año_inicio_rango)
        años_del_informe_potenciales.add(año_actual_num)
        sorted_años_a_mostrar = sorted(list(años_con_datos_en_diccionario.intersection(años_del_informe_potenciales)))
        if not sorted_años_a_mostrar:
            print(f"No hay datos de contratos en los últimos 12 meses (desde {nombres_meses_abreviados[mes_inicio_rango-1]}.{str(año_inicio_rango)[-2:]} hasta {nombres_meses_abreviados[mes_actual_num-1]}.{str(año_actual_num)[-2:]}) que coincidan con los años procesados.")
            return
        hubo_datos_en_rango_visible = False
        for año_actual_informe in sorted_años_a_mostrar:
            longitud_linea = ancho_col_producto + 1 + (ancho_col_mes * 12)
            print() 
            print("-" * longitud_linea)
            print("PESOS TOTALES POR MES")
            print("-" * longitud_linea)
            linea_encabezado = f"{'Producto':<{ancho_col_producto}} "
            for i in range(12):
                mes_año_str = f"{nombres_meses_abreviados[i]}.{str(año_actual_informe)[-2:]}"
                linea_encabezado += f"{mes_año_str:^{ancho_col_mes}}"
            print(linea_encabezado)
            print("-" * longitud_linea)
            paquetes_activos_ordenados = sorted(
                [(id_pqt, info) for id_pqt, info in paquetes.items() if info.get("activo", False)],
                key=lambda item: item[1].get("nombre", item[0])
            )
            for id_pqt, info_paquete in paquetes_activos_ordenados:
                nombre_paquete_display = info_paquete.get("nombre", f"Paquete ID {id_pqt}")
                if len(nombre_paquete_display) > ancho_col_producto -3: 
                     nombre_paquete_truncado = nombre_paquete_display[:ancho_col_producto-4] + "..."
                else:
                     nombre_paquete_truncado = nombre_paquete_display
                linea_paquete = f"{nombre_paquete_truncado:<{ancho_col_producto}} "
                montos_paquete_este_año = datos_agrupados.get(año_actual_informe, {}).get(id_pqt, {})
                for mes_num in range(1, 13):
                    monto_del_mes_original = montos_paquete_este_año.get(mes_num, 0.0)
                    monto_a_mostrar = 0.0
                    es_mes_valido_en_rango = False
                    if año_actual_informe == año_inicio_rango:
                        if año_actual_informe == año_actual_num: 
                            if mes_num >= mes_inicio_rango and mes_num <= mes_actual_num:
                                es_mes_valido_en_rango = True
                        else: 
                            if mes_num >= mes_inicio_rango:
                                es_mes_valido_en_rango = True
                    elif año_actual_informe == año_actual_num: 
                        if mes_num <= mes_actual_num:
                            es_mes_valido_en_rango = True
                    if es_mes_valido_en_rango:
                        monto_a_mostrar = monto_del_mes_original
                        if monto_a_mostrar > 0: hubo_datos_en_rango_visible = True
                    linea_paquete += f"{monto_a_mostrar:>{ancho_col_mes-1}.2f} " 
                print(linea_paquete)
            print("-" * longitud_linea)
        if not hubo_datos_en_rango_visible and sorted_años_a_mostrar:
            print(f"No se encontraron operaciones con montos en los últimos 12 meses (desde {nombres_meses_abreviados[mes_inicio_rango-1]}.{str(año_inicio_rango)[-2:]} hasta {nombres_meses_abreviados[mes_actual_num-1]}.{str(año_actual_num)[-2:]}).")
        print("\n--- FIN DEL INFORME ---")
    except Exception as e:
        print("No hay información suficiente para generar el informe. Detalle:", e)

def informePaquetesPorVentas():
    """
    Genera un informe con los 5 paquetes turísticos activos que registraron menor cantidad de ventas.

    Carga los datos desde el archivo 'data.json' y recorre los contratos activos.
    Ordena los paquetes activos de menor a mayor según su cantidad de ventas y muestra un listado con los 5
    menos vendidos, incluyendo su nombre, posición en el ranking y número total de ventas.

    Parámetros:
    No recibe parámetros.

    Returns:
    None.
    """
    try:
        turistas, paquetes, contratos = cargar_datos_json()
        print("\n--- INFORME DE LOS 5 PAQUETES MENOS VENDIDOS ---")

        ventas_por_paquete = {}

        for id_pqt, paquete_info in paquetes.items():
            try:
                if paquete_info.get("activo", False):
                    ventas_por_paquete[id_pqt] = {
                        "nombre": paquete_info.get("nombre", f"Paquete ID {id_pqt}"),
                        "ventas": 0
                    }
            except Exception as e:
                print(f"[ERROR]: Problema al procesar paquete {id_pqt}. Detalle: {e}")

        if not ventas_por_paquete:
            print("No hay paquetes activos para generar el informe.")
            return

        for contrato_info in contratos.values():
            try:
                if contrato_info.get("activo", False):
                    id_paquete_contratado = contrato_info.get("idPaquete")
                    if id_paquete_contratado in ventas_por_paquete:
                        ventas_por_paquete[id_paquete_contratado]["ventas"] += 1
            except Exception as e:
                print(f"[ERROR]: Se encontró un contrato mal cargado. Detalle: {e}")
        
        lista_paquetes_ventas = []
        for id_pqt, datos_paquete in ventas_por_paquete.items():
            lista_paquetes_ventas.append({
                "id": id_pqt,
                "nombre": datos_paquete["nombre"],
                "ventas": datos_paquete["ventas"]
            })
        
        lista_paquetes_ventas_ordenada = sorted(
            lista_paquetes_ventas, 
            key=lambda x: (x["ventas"], x["nombre"])
        )

        if not lista_paquetes_ventas_ordenada:
            print("No se encontraron datos de ventas para los paquetes activos.")
            return

        # Tomar solo los primeros 5 paquetes menos vendidos
        top_5_menos_vendidos = lista_paquetes_ventas_ordenada[:5]

        ancho_col_posicion = 5
        ancho_col_nombre = 35 
        ancho_col_ventas = 10
        longitud_total_linea = ancho_col_posicion + ancho_col_nombre + ancho_col_ventas + 3 

        print("\n{:<{rw}} {:<{nw}} {:<{vw}}".format(
            "Posición", "Nombre del Paquete", "Ventas",
            rw=ancho_col_posicion, nw=ancho_col_nombre, vw=ancho_col_ventas)
        )
        print("-" * longitud_total_linea)
        for i, datos_paquete_iter in enumerate(top_5_menos_vendidos):
            posicion = i + 1
            nombre_a_mostrar = datos_paquete_iter["nombre"]
            if len(nombre_a_mostrar) > ancho_col_nombre - 2: 
                nombre_a_mostrar = nombre_a_mostrar[:ancho_col_nombre - 3] + "..."
            
            print("{:<{rw}} {:<{nw}} {:<{vw}}".format(
                posicion,
                nombre_a_mostrar,
                datos_paquete_iter["ventas"],
                rw=ancho_col_posicion, nw=ancho_col_nombre, vw=ancho_col_ventas)
            )
        print("-" * longitud_total_linea)
        print("\n--- FIN DEL INFORME DE LOS 5 PAQUETES MENOS VENDIDOS ---")
    except Exception as e:
        print("No hay información suficiente para generar el informe. Detalle:", e)

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    """
    Función principal del sistema de gestión de paquetes turísticos.

    Presenta el menú principal y permite acceder a los distintos módulos del sistema:
    Gestión de turistas (alta, modificación, baja, listado)
    Gestión de paquetes turísticos (alta, modificación, baja, listado)
    Gestión de contratos (alta, baja, modificación)
    Reportes e informes (operaciones del mes, resumen anual de contratos y montos, paquetes menos vendidos)

    Valida las entradas y mantiene el programa en ejecución hasta que se seleccione la opción de salida.

    Parámetros:
    No recibe parámetros.

    Returns:
    None.
    """
    while True:
        print()
        print("---------------------------")
        print("MENÚ PRINCIPAL")
        print("---------------------------")
        print("[1] Gestión de turistas")
        print("[2] Gestión de paquetes")
        print("[3] Gestión de contratos")
        print("[4] Reportes")        
        print("---------------------------")
        print("[0] Salir del programa")
        print("---------------------------")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion not in [str(i) for i in range(0,5)]:
            input("Opción inválida. Presione ENTER para volver.")
            continue
        print()
        if opcion == "0":
            exit()
        if opcion == "1":
            while True:
                print()
                print("---------------------------")
                print("MENÚ DE TURISTAS")
                print("---------------------------")
                print("[1] Alta turista")
                print("[2] Modificar turista")
                print("[3] Eliminar turista")
                print("[4] Listado de Turistas activos")
                print("---------------------------")
                print("[0] Volver al menú principal")
                print("---------------------------")
                print()
                sub = input("Seleccione una opción: ")
                if sub not in [str(i) for i in range(0,5)]:
                    input("Opción inválida. Presione ENTER para volver.")
                    continue
                print()
                if sub == "0": break
                if sub == "1":
                    turistas, paquetes, contratos = cargar_datos_json()
                    turistas = ingresarTurista(turistas, paquetes, contratos)
                elif sub == "2":
                    turistas, paquetes, contratos = cargar_datos_json()
                    turistas = modificarTurista(turistas, paquetes, contratos)
                elif sub == "3":
                    turistas, paquetes, contratos = cargar_datos_json()
                    turistas = eliminarTuristas(turistas, paquetes, contratos)
                elif sub == "4":
                    turistas, paquetes, contratos = cargar_datos_json()
                    listarTuristasActivos(turistas, paquetes, contratos)
                input("\nENTER para continuar.")
        elif opcion == "2":
            while True:
                opciones = 4
                print()
                print("---------------------------")
                print("MENÚ DEL PROGRAMA           ")
                print("---------------------------")
                print("[1] Ingresar paquete")
                print("[2] Modificar paquete")
                print("[3] Eliminar paquete")
                print("[4] Listar paquetes activos")
                print("---------------------------")
                print("[0] Volver al menú anterior")
                print("---------------------------")
                print()
                sub = input("Seleccione una opción: ")
                if sub not in [str(i) for i in range(0, opciones + 1)]:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                    continue
                print()
                if sub == "0":
                    break
                elif sub == "1":
                    turistas, paquetes, contratos = cargar_datos_json()
                    paquetes = altaPaquete(turistas, paquetes, contratos)
                elif sub == "2":
                    turistas, paquetes, contratos = cargar_datos_json()
                    paquetes = modificarPaquete(turistas, paquetes, contratos)
                elif sub == "3":
                    turistas, paquetes, contratos = cargar_datos_json()
                    paquetes = eliminarPaquete(turistas, paquetes, contratos)
                elif sub == "4":
                    turistas, paquetes, contratos = cargar_datos_json()
                    listarPaquetesActivos(turistas, paquetes, contratos)
                input("\nENTER para continuar.")
        elif opcion == "3":
            while True:
                print()
                print("---------------------------")
                print("MENÚ DE CONTRATOS")
                print("---------------------------")
                print("[1] Alta contrato")
                print("[2] Baja contrato")
                print("[3] Modificar contrato")
                print("---------------------------")
                print("[0] Volver al menú principal")
                print("---------------------------")
                print()
                sub = input("Seleccione una opción: ")
                if sub not in [str(i) for i in range(0,4)]:
                    input("Opción inválida. Presione ENTER para volver.")
                    continue
                print()
                if sub == "0": break
                if sub == "1":
                    turistas, paquetes, contratos = cargar_datos_json()
                    contratos = altaContrato(turistas, paquetes, contratos)
                elif sub == "2":
                    turistas, paquetes, contratos = cargar_datos_json()
                    contratos = bajaContrato(turistas, paquetes, contratos)
                elif sub == "3":
                    turistas, paquetes, contratos = cargar_datos_json()
                    contratos = modificarContrato(turistas, paquetes, contratos)
                input("\nENTER para continuar.")
        elif opcion == "4":
            while True:
                print()
                print("---------------------------")
                print("MENÚ DE REPORTES")
                print("---------------------------")
                print("[1] Listar operaciones del Mes en curso")
                print("[2] Resumen Anual de Cantidad de Contratos por Paquete")
                print("[3] Resumen Anual de Montos de Contratos por Paquete")
                print("[4] Listar los 5 paquetes menos vendidos anualmente")
                print("---------------------------")
                print("[0] Volver al menú principal")
                print("---------------------------")
                print()
                sub = input("Seleccione una opción: ")
                if sub not in [str(i) for i in range(0,5)]:
                    input("Opción inválida. Presione ENTER para volver.")
                    continue
                print()
                if sub == "0": break
                if sub == "1":
                    listar_operaciones_mes()
                elif sub == "2":
                    resumen_cantidad_contratos_por_mes()
                elif sub == "3":
                    reporteResumenMontosPorMes()
                elif sub == "4":
                    informePaquetesPorVentas()
                input("\nENTER para continuar.")

if __name__ == "__main__":
    main()