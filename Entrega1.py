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

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# FUNCIONES TURISTAS
#----------------------------------------------------------------------------------------------
def ingresarTurista(turistas):
    ##Funcion que permite ingresar los datos de un nuevo turista##
    print("\n--- INGRESO DE NUEVO TURISTA ---")
    nuevo_id = generar_id(turistas) # Asumo que generar_id funciona bien
    nombre = input("Ingrese nombre del turista: ").strip()
    apellido = input("Ingrese apellido: ").strip()
    dni = input("Ingrese DNI: ").strip()
    email = input("Ingrese email: ").strip()
    
    # Diccionario para almacenar los teléfonos del nuevo turista
    telefonos_del_nuevo_turista = {"telefono1": "", "telefono2": "", "telefono3": ""}

    print("\n--- Ingreso de Teléfonos ---")
    # Teléfono 1
    valTel1 = input("Tiene un primer teléfono de contacto? Ingrese S/N: ").strip().upper()
    if valTel1 == "S":
        telefono1_input = input("Ingrese su primer teléfono de contacto: ").strip()
        if telefono1_input.isdigit():
            telefonos_del_nuevo_turista["telefono1"] = telefono1_input
        else:
            print("Error: El teléfono 1 debe contener solo números. No se guardó.")
    
    # Teléfono 2
    valTel2 = input("Tiene un segundo telefono de contacto? Ingrese S/N: ").strip().upper()
    if valTel2 == "S":
        telefono2_input = input("Ingrese su segundo teléfono de contacto: ").strip()
        if telefono2_input.isdigit():
            telefonos_del_nuevo_turista["telefono2"] = telefono2_input
        else:
            print("Error: El teléfono 2 debe contener solo números. No se guardó.")

    # Teléfono 3
    valTel3 = input("Tiene un tercer teléfono de contacto? Ingrese S/N: ").strip().upper()
    if valTel3 == "S":
        telefono3_input = input("Ingrese su tercer teléfono de contacto: ").strip()
        if telefono3_input.isdigit():
            telefonos_del_nuevo_turista["telefono3"] = telefono3_input
        else:
            print("Error: El teléfono 3 debe contener solo números. No se guardó.")

    ### Guardamos la informacion del nuevo turista###
    turistas[nuevo_id] = {
        "idTurista": nuevo_id,
        "activo": True,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "email": email,
        "telefonos": telefonos_del_nuevo_turista # Usar el diccionario poblado
    }
    print("\nTurista agregado con ID:", nuevo_id)
    return turistas # Asegurarse de retornar el diccionario de turistas actualizado

def generar_id(turistas):
    """mediante esta funcion, creamos un nuevo id para el nuevo turista"""
    if len(turistas) == 0:
        return "1"
    else:
        max_id = 0
        for key in turistas:
            if int(key) > max_id:
                max_id = int(key)
        return str(max_id + 1)
    
    return turistas

def modificarTurista(turistas): #Da error
     """Con esta funcion, modificamos la informacion del turista, primero preguntando que dato desea modificar y luego con el menu, para que pueda seleccionar y modificar"""
     print("\n--- MODIFICAR INFORMACION DE TURISTA ---")
     idTurista=input("Ingresar ID de turista que desea modificar: ")

     if idTurista not in turistas:
         print("Id incorrecto, ingrese ID")    ###En caso de que el ID ingresado no sea correcto, volvemos a preguntar###
         return turistas
     
     turista = turistas [idTurista]

     while True:

        print("\n¿Qué desea modificar del turista?")
        print("[1] Nombre")
        print("[2] Apellido")
        print("[3] email")
        print("[0] Salir del modificador")

        opcion = input("Opcion: ")

        if opcion == "0":
            print(f"\nTurista '{idTurista}' modificado con éxito.")
            break

        elif opcion == "1":
            nuevo = input("Nuevo nombre: ").strip()
            if nuevo != "":
                turista["nombre"] = nuevo
                print("✔ Nombre actualizado.")

        elif opcion == "2":
            nuevo = input("Nuevo apellido: ").strip()
            if nuevo != "":
                turista["apellido"] = nuevo
                print("✔ apellido actualizado.")

        elif opcion == "3":
            nuevo = input("Nuevo email: ").strip()
            if nuevo != "":
                turista["email"] = nuevo
                print("✔ email actualizada.")

        print(f"\nTurista '{idTurista}' modificado con éxito.")
        return turistas 


def listarTuristasActivos(turistas): #Da error luego de eliminar un turista
    
    """Creamos una lista de turistas activos"""

    print("\nListado de turistas activos:")
    print("ID   Nombre         Apellido       DNI         Email                  Teléfonos")
    print("-"*80)
    for t in turistas.values():
        if t["activo"]:
            tels = ", ".join(t["telefonos"].values())
            print(f'{t["idTurista"]:<4} {t["nombre"]:<14} {t["apellido"]:<14} {t["dni"]:<12} {t["email"]:<22} {tels}')
    print("-"*80)

def eliminarTuristas(turistas):
    """permite eliminar el turista deseado en base al ID."""
    turistaEliminado = input("Ingrese ID de turista que desea eliminar: ")
    
    if turistaEliminado in turistas:
        turistas = {t for t in turistas if t != turistaEliminado}
        print(f"Todos los turistas con ID {turistaEliminado} han sido eliminados.")
    else:
        print("El ID ingresado no existe en la lista.")
    
    return turistas

#----------------------------------------------------------------------------------------------
# FUNCIONES PARA CREAR PAQUETES
#----------------------------------------------------------------------------------------------

def cargarServicios():
    """
    Pide al usuario los detalles de los servicios de un paquete turístico.
    Los servicios son: vuelo, alojamiento, actividad, seguro de viaje y traslado.

    parametros: ninguno

    Return:
    Diccionario con los detalles cargados para cada servicio.
4
    """
    servicios = {}
    servicios["vuelo"] = input("Ingrese detalle del vuelo (o deje vacío si no tiene): ").strip()
    servicios["alojamiento"] = input("Ingrese detalle del alojamiento (o deje vacío si no tiene): ").strip()
    servicios["actividad"] = input("Ingrese detalle de la actividad (o deje vacío si no tiene): ").strip()
    servicios["seguro de viaje"] = input("Ingrese detalle del seguro de viaje (o deje vacío si no tiene): ").strip()
    servicios["traslado"] = input("Ingrese detalle del traslado (o deje vacío si no tiene): ").strip()
    return servicios


def esFloatValido(texto):
    """
    Verifica si un texto representa un número flotante válido.
    Reemplaza comas por puntos y valida el formato numérico.

    parametros:
        texto(str): Texto ingresado por el usuario.

    Return:
        True si el texto representa un número flotante válido, False en caso contrario.
    """
    texto = texto.replace(",", ".")
    if texto.count(".") > 1:
        return False
    #usamos replace para en caso que ponga algun numero con punto reemplace por nada para que isdigit evalue que sean solo numeros los ingresados.
    return texto.replace(".", "").isdigit()

def altaPaquete(paquetes):
    """
    Carga un nuevo paquete turístico con datos ingresados por el usuario.
    Incluye nombre, destino, duración, valor, descripción y servicios fijos.

    parametros:
        paquetes: Diccionario de paquetes turísticos.

    Return:
        paquetes: Diccionario actualizado con el nuevo paquete agregado.
    """
    print("\n--- INGRESO DE NUEVO PAQUETE ---")
    nombre = str(input("Ingrese un nombre para el paquete: ")).strip()
    destino = str(input("Ingrese destino del paquete: ")).strip()
    duracion = str(input("Ingrese duración del paquete (ej. '7 días'): ")).strip()


    valorString = input("Ingrese valor por persona: ").strip().replace(",", ".")
    while not esFloatValido(valorString):
        print("ERROR!!! debe ingresar un número válido.")
        valorString = input("Ingrese valor por persona: ").strip().replace(",", ".")
    valor = float(valorString)

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

    print(f"\nPaquete '{id_paquete}' creado exitosamente.\n")
    return paquetes



# FUNCIONES PARA MODIFICAR PAQUETES
#----------------------------------------------------------------------------------------------
def modificarPaquete(paquetes): #Imprime dos veces 'modificado' luego de una modificación
    """
    Permite modificar los datos de un paquete turístico activo.
    Se puede editar nombre, destino, duración, valor, descripción o servicios.

    Parametros:
        paquetes: Diccionario de paquetes turísticos.

    Returns:
        Diccionario actualizado con las modificaciones realizadas.
    """

    print("\n--- MODIFICAR PAQUETE ---")

    # Mostrar paquetes activos disponibles
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
            print(f"\nPaquete '{id_paquete}' modificado con éxito.")
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
            if esFloatValido(nuevo):
                paquete["valor"] = float(nuevo)
                print("Valor actualizado.")
            else:
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

    print(f"\nPaquete '{id_paquete}' modificado con éxito.")
    return paquetes

def cargarServiciosParaModificar(servicios_anteriores):
    """
    Pide al usuario los detalles de los servicios de un paquete turístico.
    Si se deja un campo vacío, conserva el valor anterior.

    Parámetros:
        servicios_anteriores: Servicios ya existentes del paquete.

    Return:
        Diccionario actualizado con los nuevos valores o los anteriores si no se modificaron.
    """
    servicios = {}

    for tipo, anterior in servicios_anteriores.items():
        entrada = input(f"Ingrese detalle del {tipo} (actual: '{anterior}') (Enter para mantener): ").strip()
        servicios[tipo] = entrada if entrada else anterior

    return servicios

# FUNCIONES PARA ELIMINAR PAQUETES
#----------------------------------------------------------------------------------------------
def eliminarPaquete(paquetes):
    """
    Realiza la baja lógica de un paquete turístico, marcándolo como inactivo.
    No elimina el paquete del sistema, solo cambia su estado.

    Parametros:
        paquetes: Diccionario de paquetes turísticos.

    Returns:
        Diccionario actualizado con el estado del paquete modificado.
    """

    print("\n--- ELIMINAR PAQUETE ---")

    # Mostrar paquetes activos
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

    return paquetes


# FUNCIONES PARA VISUALIZAR PAQUETES
#----------------------------------------------------------------------------------------------
def listarPaquetesActivos(paquetes):
    """
    Muestra por pantalla todos los paquetes turísticos que estén activos.
    
    Parametros:
        Diccionario con todos los paquetes cargados.
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
    Imprime los datos completos de un paquete turístico, incluyendo servicios detallados.

    Parametros:
        id_paquete: ID del paquete.
        datos: Diccionario con los datos del paquete.
    """    
    print("ID:", id_paquete)
    print("Nombre:", datos["nombre"])
    print("Destino:", datos["destino"])
    print("Duración:", datos["duracion"])
    print("Valor por persona: $", datos["valor"])
    print("Descripción:", datos["descripcion"])
    print("Servicios:")
    mostrarServicios(datos["servicios"])


def mostrarServicios(servicios):
    """
    Imprime los servicios de un paquete turístico, uno por uno.
    
    Parametros:
        servicios: Diccionario con detalle de los servicios.
    """
    print("\nServicios:")
    for tipo, detalle in servicios.items():
        if detalle:  # Evita mostrar servicios vacíos
            print(f"- {tipo}: {detalle}")

# -------------------------------------
# Funciones Contrato
# -------------------------------------

def altaContrato(_paquetes, _contratos, _turistas):
    """
    Da de alta un nuevo contrato.
    Solicita el ID del turista, el ID del paquete (validado contra el diccionario de paquetes), 
    la cantidad de viajeros (validada), el medio de pago y genera la fecha y hora del contrato.
    También calcula el monto total a pagar y genera automáticamente un ID único de contrato.
    El contrato se guarda en el diccionario de contratos con el estado 'activo'.

    Parámetros:
    _paquetes: diccionario de paquetes. 
    _contratos: diccionario de contratos. 

    Returns:
    ID del turista (str)
    ID del paquete (str)
    Cantidad de viajeros (int)
    Medio de pago ingresado por el usuario (str)
    Total por persona (int)
    Fecha y hora de creación del contrato (datetime)
    ID del contrato generado (str)
    """
    #Ingreso idTurista
    _idTurista= str(input("Ingrese su ID de turista: "))
    
    #Valida que el ingreso de ID turista se encuentre activo y exista
    _verificaNumeroDeTuristaBool, _verificaNumeroDeTuristaValor= verificaIDturista(_turistas, _idTurista)
    
    #Validación por si el ingreso no es correcto
    while _verificaNumeroDeTuristaBool == False:
        _idTurista= str(input("ID turista no válido. Ingrese su ID de turista: "))
        _verificaNumeroDeTuristaBool, _verificaNumeroDeTuristaValor= verificaIDturista(_turistas, _idTurista)
        
    #Ingreso idPaquete
    _idPaquete= str(input("Ingrese el ID del paquete a abonar: "))
    
    _verificaNumeroDePaqueteBool, _verificaNumeroDePaqueteValor= verificaIDpaquete(_idPaquete, _paquetes)
    
    #Validación en bucle por si ingresa mal el número de paquete. 
    while _verificaNumeroDePaqueteBool == False:
        _idPaquete= str(input("Paquete no válido. Ingrese el ID del paquete a abonar: "))
        _verificaNumeroDePaqueteBool, _verificaNumeroDePaqueteValor= verificaIDpaquete(_idPaquete, _paquetes)
    
    #Ingreso cantidadDePersonas 
    _cantidadDeViajeros= int(input("Ingrese la cantidad de asistentes: "))
    #Valida cantidadDePersonas
    cantidadAsistentesValidado= validaCantidadAsistentes(_cantidadDeViajeros)
    
    #Ingreso medio de pago 
    _medioDePago= str(input("Ingrese medio de pago a utilizar (Efectivo, Transferencia, Tarjeta): ")) #validar
    
    #Trae el valor del paquete ingresado
    _valorPaquete= _paquetes[_verificaNumeroDePaqueteValor]["valor"]
    
    #Calcula el valor total del contrato
    _total= _valorPaquete * cantidadAsistentesValidado
    print("El valor total por",cantidadAsistentesValidado, "personas es de: " ,_total )
    
    #Fecha del contrato 
    _fechaDeContrato= datetime.datetime.now()
    print(_fechaDeContrato)
    
    #Crea ID del contrato
    _idContrato= _fechaDeContrato.strftime("%Y%m%d%H%M%S") #Limpia el formato 
    print("ID del contrato: ", _idContrato)
    
    #Agrega el nuevo contrato al diccionario de contratos
    _contratos[_idContrato] = {
        "activo": True,
        "fecha": _fechaDeContrato.strftime("%Y.%m.%d %H:%M:%S"), # Formato AAAA.MM.DD HH:MM:SS
        "idTurista": _idTurista,
        "idPaquete": _verificaNumeroDePaqueteValor,
        "cantidadDePersonas": cantidadAsistentesValidado,
        "Total": _total,
        "formaDePago": {
            "Elegido por usuario": [_medioDePago] ####Revisar 
        }
    }
    
    print(_contratos) #Eliminar - Solo verifica que se agregó el nuevo contrato al diccionario.

    return _idTurista, _idPaquete, cantidadAsistentesValidado, _medioDePago, _total, _fechaDeContrato, _idContrato


def verificaIDpaquete(_idPaquete, _paquetes): 
    """
    Verifica si un ID de paquete ingresado es válido, comprobando 
    si el ID existe dentro del diccionario de paquetes.

    Parámetros:
    _idPaquete(str): ID del paquete a verificar.
    _paquetes: diccionario de paquetes. 

    Retorna:
    bool: True si el ID existe en el diccionario de paquetes, False en caso contrario.
    str: El ID del paquete ingresado.
    """
    if _idPaquete in _paquetes:
        return True, _idPaquete
    
    else:
        return False, _idPaquete 
 
 
def validaCantidadAsistentes(ingreso): 
    """
    Valida que la cantidad de asistentes ingresada sea un número válido.

    Verifica que el número de asistentes sea mayor a 0 y menor o igual a 100.
    Si el valor ingresado no está en ese rango, solicita al usuario que vuelva a ingresar
    un valor hasta que sea válido.

    Parámetros:
    ingreso(int): Cantidad inicial de asistentes ingresada por el usuario.
        
    Returns:
    ingreso(int): Cantidad de asistentes validada, un número entero entre 1 y 100.
    """
    while ingreso < 0 or ingreso > 100:
        ingreso= int(input("No válido. Ingrese la cantidad de asistentes: "))
    
    return ingreso

def verificaIDturista (_turistas, _idTurista): 
    """
    Verifica si el ID de un turista es válido y activo.

    Parámetros:
    _turistas (diccionario): Diccionario de turistas. 
    _idTurista (str): ID del turista a verificar. 

    Returns:
    bool: True si el turista existe y está activo, False en caso contrario.
    _idTurista(str): El ID del turista verificado.
    """
    if _idTurista in _turistas and _turistas[_idTurista]["activo"] == True: 
        return True, _idTurista
    
    else:
        return False, _idTurista


def verificaIDcontrato(_idContrato, _contratos): 
    """
    Verifica si un ID de contrato es válido y está activo.

    Comprueba si el ID de contrato existe en el diccionario de contratos y si se encuentra activado.
    Retorna una tupla con el resultado de la verificación y el ID ingresado.

    Parámetros:
    _idContrato(str): ID del contrato a verificar.
    _contratos: Diccionario de contratos. 
        

    Returns:
    bool: True si el contrato existe y está activo, False en caso contrario.
    _idContrato(str): El ID del contrato ingresado.
    """
    if _idContrato in _contratos and _contratos[_idContrato]["activo"] == True:  
        return True, _idContrato
    
    elif _idContrato not in _contratos or _contratos[_idContrato]["activo"] == False: 
        return False, _idContrato

def bajaContrato(_paquetes, _contratos, _turistas): 
    """
    Da de baja un contrato de viaje existente, utilizando su ID.

    Solicita al usuario el ID del turista y el ID del contrato. Verifica si el contrato
    existe y se encuentra activo. Si es válido, actualiza su estado a inactivo 
    (sin eliminarlo del diccionario) y registra la fecha y hora de la baja.
    
    Parámetros:
    _paquetes: Diccionario que contiene los paquetes turísticos (no se usa en esta función, pero se recibe como parámetro).
    _contratos: Diccionario de contratos (activos e inactivos).

    Returns:
    _idTurista(str): ID del turista.
    _fechaDeBaja (datetime): Fecha y hora de la baja del contrato.
    _contratos (diccionario): Diccionario de contratos actualizado.

    None:
        Si el ID del contrato no es válido o el contrato ya está inactivo.
    """
    #Ingreso ID turista
    _idTurista= str(input("Ingrese su ID de turista: "))
    
    #Valida que el ingreso de ID turista se encuentre activo y exista
    _verificaNumeroDeTuristaBool, _verificaNumeroDeTuristaValor= verificaIDturista(_turistas, _idTurista)
    
    #Validación por si el ingreso no es correcto
    while _verificaNumeroDeTuristaBool == False:
        _idTurista= str(input("ID turista no válido. Ingrese su ID de turista: "))
        _verificaNumeroDeTuristaBool, _verificaNumeroDeTuristaValor= verificaIDturista(_turistas, _idTurista)

    #Ingreso ID contrato
    _idContrato= str(input("Ingrese el ID del contrato a dar de baja: "))

    #Validación ID contrato
    _verificaNumeroDeContratoBool, _verificaNumeroDeContratoValor= verificaIDcontrato(_idContrato, _contratos)
    
    if _verificaNumeroDeContratoBool == True: 
        _fechaDeBaja= datetime.datetime.now()
        print("Cancelado con éxito. Fecha de cancelación: ", _fechaDeBaja)
        
        #contratoAeliminar= _contratos.pop(_verificaNumeroDeContratoValor) #Esto lo elimina, no lo desactiva. 
        
        _contratos[_idContrato]["activo"]= False
        
        print(_contratos) ##Elimar. Solo verifico que se haya eliminado del diccionario de contratos. 
        
        return _idTurista, _fechaDeBaja, _contratos
    
    else:
        print("Contrato no encontrado. Intente nuevamente.")
        
        return 


def modificarContrato(_paquetes, _contratos, _turistas):
    """
    Modifica un contrato de viaje.
    Solicita el ID del turista y el ID del paquete,para realizar los cambios. 
    Registra la fecha y hora en que se realiza la modificación.

    Returns:
    ID del turista (str)
    ID del paquete (str)
    Fecha y hora de la modificación del contrato
    """
    _fechaDeModificacion= datetime.datetime.now()
    
    #Ingreso ID turista
    _idTurista= str(input("Ingrese su ID de turista: "))
    
    #Valida que el ingreso de ID turista se encuentre activo y exista
    _verificaNumeroDeTuristaBool, _verificaNumeroDeTuristaValor= verificaIDturista(_turistas, _idTurista)
    
    #Validación por si el ingreso no es correcto
    while _verificaNumeroDeTuristaBool == False:
        _idTurista= str(input("ID turista no válido. Ingrese su ID de turista: "))
        _verificaNumeroDeTuristaBool, _verificaNumeroDeTuristaValor= verificaIDturista(_turistas, _idTurista)

    
    _idContrato= str(input("Ingrese el ID del contrato a modificar: "))
 
    #Verifica ID contrato
    idContratoVerificadoBool, idContratoVerificadoValor= verificaIDcontrato(_idContrato, _contratos)
    
    #Si el ingreso no es válido, sale de la función. 
    if idContratoVerificadoBool == False:
        print("Contrato no encontrado o desactivado. Intente de nuevo.")
    
    else:
        contrato = _contratos[idContratoVerificadoValor]
        print("Opciones a modificar: ")
        print('''
[1] Paquete
[2] Cantidad de personas 
[3] Forma de pago 
            ''')
        
        #Input de opción a modificar dentro del contrato
        opcionAmodificar= str(input("Ingrese opción a modificar: "))
        
        #Valida que sea un número de las opciones
        while opcionAmodificar != "1" and opcionAmodificar != "2" and opcionAmodificar != "3":
            opcionAmodificar= str(input("Opción ingresada no válida. Ingrese opción a modificar: "))
            
        #Opción 1 - Cambio de paquete
        if opcionAmodificar == "1":
            nuevoPaquete = str(input("Ingrese el nuevo ID de paquete: ")).strip()
            
            #Valida que el paquete exista
            idPaqueteValidadoBool, idPaqueteValidado= verificaIDpaquete(nuevoPaquete, _paquetes)
            
            if idPaqueteValidadoBool == True:
                contrato["idPaquete"] = nuevoPaquete
                print("Cambio realizado con éxito.")
                contrato["fecha"] = _fechaDeModificacion
                contrato["Total"] = _paquetes[nuevoPaquete]["valor"] * contrato["cantidadDePersonas"]
                
            else:
                print("Paquete no encontrado. Intente de nuevo.")
                
        #Opción 2 - cantidadDePersonas
        elif opcionAmodificar == "2":
            nuevaCantidadDePersonas = int(input("Ingrese la nueva cantidadDePersonas: "))
            
            #Valida el ingreso de cantidadDePersonas
            nuevaCantidadDePersonaValidado= validaCantidadAsistentes(nuevaCantidadDePersonas)
            
            contrato["cantidadDePersonas"] = nuevaCantidadDePersonaValidado
            contrato["fecha"] = _fechaDeModificacion
            contrato["Total"] = _paquetes[nuevoPaquete]["valor"] * contrato["cantidadDePersonas"]
            
            print("Cambio realizado con éxito.")
          
        #Opción 3 - formaDePago
        elif opcionAmodificar == "3":
            print("Formas de pago disponibles: Efectivo, Transferencia, Tarjeta")
            nuevaFormaDePago = input("Ingrese la nueva forma de pago: ").strip().capitalize()

        #Valida que la forma de pago ingresada sea correcta
        if nuevaFormaDePago in ["Efectivo", "Transferencia", "Tarjeta"]:
            contrato["formaDePago"] = nuevaFormaDePago
            contrato["fecha"] = _fechaDeModificacion
            print("Cambio realizado con éxito.")
            
        else:
            print("Forma de pago no válida. No se realizó el cambio.")
            return None
            
    return (_idTurista, idContratoVerificadoValor, _fechaDeModificacion)

#----------------------------------------------------------------------------------------------
# FUNCIONES DE INFORMES
#----------------------------------------------------------------------------------------------

def reporteResumenMontosPorMes(contratos, paquetes):
    """
    Genera y muestra un listado de resumen de montos de operaciones por año y por mes,
    desglosado por paquete, para los últimos 12 meses hasta la fecha actual.
    """
    print("\n--- GENERANDO INFORME DE RESUMEN DE MONTOS POR MES Y AÑO (ÚLTIMOS 12 MESES) ---")

    datos_agrupados = {}  # Estructura: {año: {idPaquete: {mes: total_monto}}}

    for id_contrato, contrato_info in contratos.items(): 
        if contrato_info.get("activo", False):
            fecha_contrato_str = contrato_info["fecha"]
            fecha_contrato_obj = datetime.datetime.strptime(fecha_contrato_str, "%Y.%m.%d %H:%M:%S")

            año_contrato = fecha_contrato_obj.year
            mes_contrato = fecha_contrato_obj.month
            id_paquete = contrato_info["idPaquete"]
            monto = float(contrato_info["Total"]) 

            datos_agrupados.setdefault(año_contrato, {}).setdefault(id_paquete, {})
            datos_agrupados[año_contrato][id_paquete].setdefault(mes_contrato, 0.0)
            datos_agrupados[año_contrato][id_paquete][mes_contrato] += monto

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


def informePaquetesPorVentas(contratos, paquetes):
    """
    Genera y muestra un informe de los paquetes activos ordenados por la cantidad de veces
    que han sido contratados (de menos a más vendidos).
    """
    print("\n--- INFORME DE PAQUETES POR CANTIDAD DE VENTAS (DE MENOS A MÁS) ---")

    ventas_por_paquete = {}

    for id_pqt, paquete_info in paquetes.items():
        if paquete_info.get("activo", False):
            ventas_por_paquete[id_pqt] = {
                "nombre": paquete_info.get("nombre", f"Paquete ID {id_pqt}"),
                "ventas": 0
            }

    if not ventas_por_paquete:
        print("No hay paquetes activos para generar el informe.")
        return

    for contrato_info in contratos.values():
        if contrato_info.get("activo", False):
            id_paquete_contratado = contrato_info.get("idPaquete")
            if id_paquete_contratado in ventas_por_paquete:
                ventas_por_paquete[id_paquete_contratado]["ventas"] += 1
    
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

    ancho_col_posicion = 5
    ancho_col_nombre = 35 
    ancho_col_ventas = 10
    longitud_total_linea = ancho_col_posicion + ancho_col_nombre + ancho_col_ventas + 3 

    print("\n{:<{rw}} {:<{nw}} {:<{vw}}".format(
        "Posición", "Nombre del Paquete", "Ventas",
        rw=ancho_col_posicion, nw=ancho_col_nombre, vw=ancho_col_ventas)
    )
    print("-" * longitud_total_linea)
    for i, datos_paquete_iter in enumerate(lista_paquetes_ventas_ordenada):
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
    print("\n--- FIN DEL INFORME DE PAQUETES POR VENTAS ---")

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    # Inicialización de variables
    ##Diccionario de turistas##
    # --------------------- DICCIONARIO TURISTAS ------------------------#
    turistas = {
        "1": {
            "idTurista": "1", "activo": True, "nombre": "Virginia", "apellido": "Griego", "dni": "14.309.227",
            "email": "griegomavi@hotmail.com",
            "telefonos": {"telefono1": "5491144902357", "telefono2": "43132662", "telefono3": "43034562"}
        },
        "2": {
            "idTurista": "2", "activo": True, "nombre": "Agostina", "apellido": "Griego", "dni": "36.314.353",
            "email": "griegoagos@hotmail.com",
            "telefonos": {"telefono1": "5491144905848", "telefono2": "43132662", "telefono3": ""}
        },
        "3": {
            "idTurista": "3", "activo": True, "nombre": "Fernando", "apellido": "Lopez", "dni": "3.699.227",
            "email": "lopezfernando@hotmail.com",
            "telefonos": {"telefono1": "5491144927437", "telefono2": "43136662", "telefono3": "43132662"}
        },
        "4": {
            "idTurista": "4", "activo": True, "nombre": "Daniel", "apellido": "Lopez", "dni": "14.456.697",
            "email": "danielopez@hotmail.com",
            "telefonos": {"telefono1": "5491199657842", "telefono2": "43132662", "telefono3": "43132662"}
        },
        "5": {
            "idTurista": "5", "activo": True, "nombre": "Martina", "apellido": "Sanchez", "dni": "40.536.846",
            "email": "martinasanchez@hotmail.com",
            "telefonos": {"telefono1": "54911996084737", "telefono2": "43032662", "telefono3": ""}
        },
        "6": {
            "idTurista": "6", "activo": True, "nombre": "Valentina", "apellido": "Dominguez", "dni": "40.589.659",
            "email": "valendominguez@hotmail.com",
            "telefonos": {"telefono1": "5491159608477", "telefono2": "43014810", "telefono3": "43189756"}
        },
        "7": {
            "idTurista": "7", "activo": True, "nombre": "Milagros", "apellido": "Pliego", "dni": "41.587.986",
            "email": "milipliego@hotmail.com",
            "telefonos": {"telefono1": "5491156978562", "telefono2": "43732662", "telefono3": "43874562"}
        },
        "8": {
            "idTurista": "8", "activo": True, "nombre": "Camila", "apellido": "Gennaro", "dni": "41.897.988",
            "email": "camigennaro@hotmail.com",
            "telefonos": {"telefono1": "5491156978562", "telefono2": "43874562", "telefono3": "43874562"}
        },
        "9": {
            "idTurista": "9", "activo": True, "nombre": "Daniela", "apellido": "Savino", "dni": "40.589.698",
            "email": "danisavino@hotmail.com",
            "telefonos": {"telefono1": "5491159608765", "telefono2": "43014896", "telefono3": ""}
        },
        "10": {
            "idTurista": "10", "activo": True, "nombre": "Agustina", "apellido": "Yarussi", "dni": "40.986.689",
            "email": "agusyarussi@hotmail.com",
            "telefonos": {"telefono1": "5491159608477", "telefono2": "43014810", "telefono3": ""}
        }
    }
    ##Diccionario de paquetes##
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
##Diccionario de contratos##
# --------------------- DICCIONARIO CONTRATOS ------------------------#
    contratos = { "20000000000000": {
        "activo": True,
        "fecha": "2999.12.31 00:00:00", # Ajustado a YYYY.MM.DD HH:MM:SS
        "idTurista": "0", 
        "idPaquete": "2",
        "cantidadDePersonas": 1,
        "Total": paquetes["2"]["valor"] ,  
        "formaDePago":"Efectivo"
    },
                  
    "20000023456789": {
        "activo": True,
        "fecha": "2025.01.12 14:15:00", # Ajustado
        "idTurista": "1",
        "idPaquete": "1",
        "cantidadDePersonas": 3,
        "Total": paquetes["1"]["valor"] * 3,
        "formaDePago":"Transferencia"
    },
    "20000034567890": {
        "activo": True,
        "fecha": "2024.11.20 09:00:00", # Ajustado
        "idTurista": "2",
        "idPaquete": "2",
        "cantidadDePersonas": 1,
        "Total": paquetes["2"]["valor"],
        "formaDePago":"Tarjeta"    
    },
    "20000045678901": {
        "activo":True,
        "fecha": "2024.12.01 08:00:00", # Ajustado
        "idTurista": "3",
        "idPaquete": "3",
        "cantidadDePersonas": 6,
        "Total": paquetes["3"]["valor"] * 6,
        "formaDePago":"Transferencia"
    },
    "20000056789012": {
        "activo": True,
        "fecha": "2025.03.10 12:00:00", # Ajustado
        "idTurista": "4",
        "idPaquete": "4",
        "cantidadDePersonas": 5,
        "Total": paquetes["4"]["valor"] * 5,
        "formaDePago":"Efectivo"
    },
    "20000067890123": {
        "activo": True,
        "fecha": "2025.04.05 16:45:00", # Ajustado
        "idTurista": "5",
        "idPaquete": "5",
        "cantidadDePersonas": 10,
        "Total": paquetes["5"]["valor"] * 10,
        "formaDePago": "Tarjeta"
    },
    "20000078901234": {
        "activo": True,
        "fecha": "2023.09.18 09:15:00", # Ajustado
        "idTurista": "6",
        "idPaquete": "6",
        "cantidadDePersonas": 4,
        "Total": paquetes["6"]["valor"] * 4,
        "formaDePago": "Transferencia"
    },
    "20000089012345": {
        "activo": True,
        "fecha": "2025.05.30 11:00:00", # Ajustado
        "idTurista": "7",
        "idPaquete": "7",
        "cantidadDePersonas": 8,
        "Total": paquetes["7"]["valor"] * 8,
        "formaDePago": "Efectivo"
    },
    "20000090123456": {
        "activo": True,
        "fecha": "2024.10.01 13:20:00", # Ajustado
        "idTurista": "8",
        "idPaquete": "10",
        "cantidadDePersonas": 1,
        "Total": paquetes["10"]["valor"],
        "formaDePago": "Efectivo"
    },
    "20000001234567": {
        "activo": True,
        "fecha": "2024.07.22 15:10:00", # Ajustado
        "idTurista": "9",
        "idPaquete": "9",
        "cantidadDePersonas": 7,
        "Total": paquetes["9"]["valor"] * 7,
        "formaDePago": "Tarjeta"
    }
}

    while True:
        # Menú principal
        print()
        print("---------------------------")
        print("MENÚ PRINCIPAL")
        print("---------------------------")
        print("[1] Gestión de clientes")
        print("[2] Gestión de paquetes")
        print("[3] Gestión de contratos")
        print("[4] Reportes")
        print("[5] Ayuda")
        print("---------------------------")
        print("[0] Salir del programa")
        print("---------------------------")
        print()

        opcion = input("Seleccione una opción: ")
        if opcion not in [str(i) for i in range(0,6)]:
            input("Opción inválida. Presione ENTER para volver.")
            continue
        print()

        if opcion == "0":
            exit()

        # Gestión de clientes
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
                if sub not in [str(i) for i in range(0,5)]: #Rango va de 0 a 5, sino la opción 4 no entra. 
                    input("Opción inválida. Presione ENTER para volver.")
                    continue
                print()
                if sub == "0": break
                
                if sub == "1":
                    turistas = ingresarTurista(turistas)
                    
                elif sub == "2":
                    turistas=modificarTurista(turistas)
                    
                elif sub == "3":
                    turistas=eliminarTuristas(turistas)
                
                elif sub == "4":  
                    turistas=listarTuristasActivos(turistas)
                
                input("\nENTER para continuar.")

# GESTIÓN DE PAQUETES
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
                
                opcion = input("Seleccione una opción: ")
                if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()

            if opcion == "0": # Opción salir del programa
                exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

            elif opcion == "1":   # Opción 1
                paquetes = altaPaquete(paquetes)

            elif opcion == "2":   # Opción 2
                paquetes = modificarPaquete(paquetes)

            elif opcion == "3":   # Opción 3
                paquetes = eliminarPaquete(paquetes)

            elif opcion == "4":   # Opción 4
                listarPaquetesActivos(paquetes)


        # Gestión de contratos
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
                
                if sub == "1": # altaContrato
                    altaContrato(paquetes, contratos, turistas)
                    
                elif sub == "2":# bajaContrato
                    bajaContrato(paquetes, contratos, turistas)
                    
                elif sub == "3":# modificarContrato
                    modificarContrato(paquetes, contratos, turistas) 
                input("\nENTER para continuar.")

        # Reportes
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
                if sub == "1": ...  # listarClientesActivos
                elif sub == "2": ...  # listarPaquetesVendidos
                elif sub == "3": reporteResumenMontosPorMes(contratos, paquetes)
                elif sub == "4": informePaquetesPorVentas(contratos, paquetes)
                input("\nENTER para continuar.")

        # Ayuda
        elif opcion == "5":
            ...  # ayuda

        # Pausa general
        input("\nENTER para volver al menú principal.")

if __name__ == "__main__":
    main()