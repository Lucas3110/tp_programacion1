"""
-----------------------------------------------------------------------------------------------
Título: Empresa de viajes
Fecha: 25/05/25
Autor: Maia Medina, Eugenia Alonso, Lucas Rodriguez, Ciro Petrella y Caterina Turdo
Descripción: Sistema para gestion de paquetes de viajes

Pendientes:
Menu funcional e informes
-----------------------------------------------------------------------------------------------
"""
# Fecha de contrato (str) 
# IDTurista (str)
# IDPaquete (str) -> Usar la fecha del día (limpiar con un strip() o algo. 
# cantidadDePersonas (int) -> Hacer el cálculo del precio total del paquete si es más de una persona.
# Total (float) 
# formaDePago (str) -> VISA 


# MÓDULOS
#----------------------------------------------------------------------------------------------
import datetime  

# FUNCIONES
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
def modificarPaquete(paquetes):
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

def altaContrato(_paquetes, _contratos):
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
    _idTurista= str(input("Ingrese su ID de turista: ")) #FALTA VALIDACIÓN. 
    
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
    _medioDePago= str(input("Ingrese medio de pago a utilizar: "))
    
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
        "fecha": _fechaDeContrato.strftime("%Y-%m-%d %H:%M:%S.%f"),
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

def verificaIDturista (): ###Falta funciones turista.
    '''Verifica que el número de turista sea válido. '''
    
    return


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

def bajaContrato(_paquetes, _contratos): 
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
    _idTurista= str(input("Ingrese su ID de turista: ")) #Falta validar idTurista.
    _idContrato= str(input("Ingrese el ID del contrato a dar de baja: "))
    
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


def modficarContrato(_paquetes, _contratos):
    """
    Modifica un contrato de viaje.
    Solicita el ID del turista y el ID del paquete,para realizar los cambios. 
    Registra la fecha y hora en que se realiza la modificación.

    Returns:
    ID del turista (str)
    ID del paquete (str)
    Fecha y hora de la modificación del contrato
    """
    _idTurista= str(input("Ingrese su ID de turista: "))
    _idContrato= str(input("Ingrese el ID del contrato a modificar: "))
    _fechaDeModificacion= datetime.datetime.now() 
    
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
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    # Inicialización de variables
    clientes = {...}
    paquetes = {
    "1": {
        "activo": True,
        "nombre": "Aventura en Salta",
        "destino": "Salta",
        "duracion": "5 días",
        "valor": 210000.0,
        "descripcion": "Excursiones y paisajes del norte argentino",
        "servicios": {
            "alojamiento": ["Hotel Solar del Cerro"],
            "actividad": ["City tour y Visita a Cafayate"],
            "vuelo": ["JetSmart"]
        }
    },
    "2": {
        "activo": True,
        "nombre": "Mendoza Full Wine",
        "destino": "Mendoza",
        "duracion": "4 días",
        "valor": 265000.0,
        "descripcion": "Degustaciones y hotel boutique en la montaña",
        "servicios": {
            "alojamiento": ["Cavas Wine Lodge"],
            "actividad": ["Bodega Norton y Spa vinoterapia"],
            "vuelo": ["Aerolíneas Argentinas"]
        }
    },
    "3": {
        "activo": True,
        "nombre": "Relax en Iguazú",
        "destino": "Misiones",
        "duracion": "6 días",
        "valor": 295000.0,
        "descripcion": "Naturaleza, hotel con pileta y parque temático",
        "servicios": {
            "alojamiento": ["Hotel La Cantera Jungle Lodge"],
            "actividad": ["Cataratas y Parque de las Aves"],
            "traslado": ["Aeropuerto - Hotel"]
        }
    },
    "4": {
        "activo": True,
        "nombre": "Bariloche Aventura",
        "destino": "Bariloche",
        "duracion": "7 días",
        "valor": 310000.0,
        "descripcion": "Trekking, kayak y nieve en la Patagonia",
        "servicios": {
            "alojamiento": ["Refugio Piedras Blancas"],
            "actividad": ["Trekking al cerro y Rafting en el río"],
            "vuelo": ["Flybondi"]
        }
    },
    "5": {
        "activo": True,
        "nombre": "Buenos Aires Clásico",
        "destino": "CABA",
        "duracion": "3 días",
        "valor": 180000.0,
        "descripcion": "Hotel céntrico y city tour cultural",
        "servicios": {
            "alojamiento": ["Hotel NH Tango"],
            "actividad": ["City Tour y Cena Tango Show"]
        }
    },
    "6": {
        "activo": True,
        "nombre": "Costa Atlántica",
        "destino": "Mar del Plata",
        "duracion": "5 días",
        "valor": 155000.0,
        "descripcion": "Playa, paseo costero y hotel con desayuno",
        "servicios": {
            "alojamiento": ["Hotel Dos Reyes"],
            "traslado": ["Bus desde Buenos Aires"],
            "actividad": ["Acuario y puerto"]
        }
    },
    "7": {
        "activo": True,
        "nombre": "Tucumán Colonial",
        "destino": "Tucumán",
        "duracion": "4 días",
        "valor": 198000.0,
        "descripcion": "Ruta de la independencia y cerros del NOA",
        "servicios": {
            "alojamiento": ["Hotel Carlos V"],
            "actividad": ["Casa de Tucumán y Excursión a Tafí del Valle"]
        }
    },
    "8": {
        "activo": True,
        "nombre": "Sur Glaciar Express",
        "destino": "El Calafate",
        "duracion": "4 días",
        "valor": 320000.0,
        "descripcion": "Perito Moreno y navegación",
        "servicios": {
            "alojamiento": ["Hotel Kosten Aike"],
            "actividad": ["Glaciar Perito Moreno y Navegación por Lago Argentino"],
            "vuelo": ["Aerolíneas Argentinas"]
        }
    },
    "9": {
        "activo": True,
        "nombre": "Córdoba Sierras y Relax",
        "destino": "Córdoba",
        "duracion": "5 días",
        "valor": 230000.0,
        "descripcion": "Villa General Belgrano, caminatas y spa",
        "servicios": {
            "alojamiento": ["Cabañas Alpinas"],
            "actividad": ["Spa y senderismo y Villa General Belgrano"],
            "traslado": ["Auto alquilado"]
        }
    },
    "10": {
        "activo": True,
        "nombre": "San Juan y Valle de la Luna",
        "destino": "San Juan",
        "duracion": "6 días",
        "valor": 245000.0,
        "descripcion": "Naturaleza, fósiles y aventura paleontológica",
        "servicios": {
            "alojamiento": ["Hostería del Sol"],
            "actividad": ["Valle de la Luna y Museo de Dinosaurios"],
            "traslado": ["Minivan desde aeropuerto"]
        }
    }
} ### Diccionarios de contratos 
    contratos = { "20000000000000": {
        "activo": True,
        "fecha": "2999-12-31 00:00:00.000000", #Fecha de alta de contrato 
        "idTurista": "0", ####### FALTA
        "idPaquete": "2",
        "cantidadDePersonas": 1,
        "Total": paquetes["2"]["valor"] ,  
        "formaDePago":"Efectivo"
    },
                  
    "20000023456789": {
        "activo": True,
        "fecha": "2025-01-12 14:15:00.000000",
        "idTurista": "1",
        "idPaquete": "1",
        "cantidadDePersonas": 3,
        "Total": paquetes["1"]["valor"] * 3,
        "formaDePago":"Transferencia"
    },
    "20000034567890": {
        "activo": True,
        "fecha": "2024-11-20 09:00:00.000000",
        "idTurista": "2",
        "idPaquete": "2",
        "cantidadDePersonas": 1,
        "Total": paquetes["2"]["valor"],
        "formaDePago":"Tarjeta"    
    },
    "20000045678901": {
        "activo":True,
        "fecha": "2024-12-01 08:00:00.000000",
        "idTurista": "3",
        "idPaquete": "3",
        "cantidadDePersonas": 6,
        "Total": paquetes["3"]["valor"] * 6,
        "formaDePago":"Transferencia"
    },
    "20000056789012": {
        "activo": True,
        "fecha": "2025-03-10 12:00:00.000000",
        "idTurista": "4",
        "idPaquete": "4",
        "cantidadDePersonas": 5,
        "Total": paquetes["4"]["valor"] * 5,
        "formaDePago":"Efectivo"
    },
    "20000067890123": {
        "activo": True,
        "fecha": "2025-04-05 16:45:00.000000",
        "idTurista": "5",
        "idPaquete": "5",
        "cantidadDePersonas": 10,
        "Total": paquetes["5"]["valor"] * 10,
        "formaDePago": "Tarjeta"
    },
    "20000078901234": {
        "activo": True,
        "fecha": "2023-09-18 09:15:00.000000",
        "idTurista": "6",
        "idPaquete": "6",
        "cantidadDePersonas": 4,
        "Total": paquetes["6"]["valor"] * 4,
        "formaDePago": "Transferencia"
    },
    "20000089012345": {
        "activo": True,
        "fecha": "2025-05-30 11:00:00.000000",
        "idTurista": "7",
        "idPaquete": "7",
        "cantidadDePersonas": 8,
        "Total": paquetes["7"]["valor"] * 8,
        "formaDePago": "Efectivo"
    },
    "20000090123456": {
        "activo": True,
        "fecha": "2024-10-01 13:20:00.000000",
        "idTurista": "8",
        "idPaquete": "10",
        "cantidadDePersonas": 1,
        "Total": paquetes["10"]["valor"],
        "formaDePago": "Efectivo"
    },
    "20000001234567": {
        "activo": True,
        "fecha": "2024-07-22 15:10:00.000000",
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
                print("MENÚ DE CLIENTES")
                print("---------------------------")
                print("[1] Alta cliente")
                print("[2] Baja cliente")
                print("[3] Modificar cliente")
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
                if sub == "1": clientes = altaCliente(clientes)
                elif sub == "2": ...  # bajaCliente
                elif sub == "3": ...  # modificarCliente
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
                    altaContrato(paquetes, contratos)
                    
                elif sub == "2":# bajaContrato
                    bajaContrato(paquetes, contratos)
                    
                elif sub == "3":# modificarContrato
                    modficarContrato(paquetes, contratos) 
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
                elif sub == "3": ...  # listarContratosVigentes
                elif sub == "4": ...  # listar5PaquetesMenosVendidos
                input("\nENTER para continuar.")

        # Ayuda
        elif opcion == "5":
            ...  # ayuda

        # Pausa general
        input("\nENTER para volver al menú principal.")

if __name__ == "__main__":
    main()