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
# Cantidad de personas (int) -> Hacer el cálculo del precio total del paquete si es más de una persona.
# Total (float) 
# Forma de pago (str) -> VISA 


# MÓDULOS
#----------------------------------------------------------------------------------------------
import datetime 
import re 

# FUNCIONES
#----------------------------------------------------------------------------------------------
# FUNCIONES PARA CREAR PAQUETES
#----------------------------------------------------------------------------------------------

def cargarServicios():
    """
    Permite seleccionar al menos 2 servicios del paquete turístico y cargar sus detalles.
    Devuelve un diccionario 'servicios'.
    """
    opciones = {
        "1": "vuelo",
        "2": "alojamiento",
        "3": "actividad",
        "4": "traslado",
        "5": "seguro de viaje"
    }

    servicios = {}

    print("\nSeleccione al menos 2 servicios para el paquete.")
    print("Escriba '0' para finalizar la carga.")

    while True:
        print("\nTipos de servicio:")
        print("[1] vuelo")
        print("[2] alojamiento")
        print("[3] actividad")
        print("[4] seguro de viaje")
        print("[5] traslado")
        print("[0] finalizar")

        #.strip() es un elimina los espacios en blanco que pueden quedar al inicio o al final.
        seleccion = input("Opción: ").strip()

        if seleccion == "0":
            break

        if seleccion not in opciones:
            print("Opción inválida.")
            continue

        tipo = opciones[seleccion]

        detalle = input(f"Ingrese el detalle del servicio '{tipo}': ").strip()

        if detalle == "":
            print("El detalle no puede estar vacío.")
            continue


        if tipo not in servicios:
            servicios[tipo] = []

        servicios[tipo].append(detalle)


    if len(servicios) < 2:
        print("Debe ingresar al menos 2 servicios.")
        return None

    return servicios

def esFloatValido(texto):
    texto = texto.replace(",", ".")
    if texto.count(".") > 1:
        return False
    #usamos replace para en caso que ponga algun numero con punto reemplace por nada para que isdigit evalue que sean solo numeros los ingresados.
    return texto.replace(".", "").isdigit()

def altaPaquete(paquetes):
    """
    Carga un nuevo paquete turístico con campos obligatorios y servicios multivaluados.
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
    if servicios is None:
        return paquetes

    nro = len(paquetes) + 1

    id_paquete = f"PQT{nro:03d}"

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
    print("\n--- MODIFICAR PAQUETE ---")

    # Mostrar paquetes activos disponibles
    print("\nPaquetes activos disponibles:")
    for idPQT, datos in paquetes.items():
        if datos["activo"]:
            print(f"- {idPQT}: {datos['nombre']} | {datos['destino']} ({datos['duracion']}) - ${datos['valor']}")

    id_paquete = input("\nIngrese el ID del paquete a modificar (ej. PQT001): ").strip()

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
                print("✔ Nombre actualizado.")

        elif opcion == "2":
            nuevo = input("Nuevo destino: ").strip()
            if nuevo != "":
                paquete["destino"] = nuevo
                print("✔ Destino actualizado.")

        elif opcion == "3":
            nuevo = input("Nueva duración: ").strip()
            if nuevo != "":
                paquete["duracion"] = nuevo
                print("✔ Duración actualizada.")

        elif opcion == "4":
            nuevo = input("Nuevo valor por persona: ").strip().replace(",", ".")
            if esFloatValido(nuevo):
                paquete["valor"] = float(nuevo)
                print("✔ Valor actualizado.")
            else:
                print("Valor inválido. No se modificó.")

        elif opcion == "5":
            nuevo = input("Nueva descripción: ").strip()
            if nuevo != "":
                paquete["descripcion"] = nuevo
                print("✔ Descripción actualizada.")

        elif opcion == "6":
            nuevos_servicios = cargarServicios()
            if nuevos_servicios is not None:
                paquete["servicios"] = nuevos_servicios
                print("✔ Servicios actualizados.")
            else:
                print("Los servicios no fueron modificados.")

        else:
            print("Opción inválida. Intente de nuevo.")

    print(f"\nPaquete '{id_paquete}' modificado con éxito.")
    return paquetes

# FUNCIONES PARA ELIMINAR PAQUETES
#----------------------------------------------------------------------------------------------
def eliminarPaquete(paquetes):
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

    id_paquete = input("\nIngrese el ID del paquete que desea eliminar (ej. PQT001): ").strip()

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
    print("\n--- LISTADO DE PAQUETES ACTIVOS ---\n")

    hay_activos = False

    for id_paquete, datos in paquetes.items():
        if datos["activo"]:
            hay_activos = True
            print(f"   ID: {id_paquete}")
            print(f"   Nombre: {datos['nombre']}")
            print(f"   Destino: {datos['destino']}")
            print(f"   Duración: {datos['duracion']}")
            print(f"   Valor por persona: ${datos['valor']}")
            print(f"   Descripción: {datos['descripcion']}")
            print("   Servicios:")
            for tipo, lista in datos["servicios"].items():
                for i, item in enumerate(lista, 1):
                    print(f"     - {tipo.capitalize()} {i}: {item}")
            print("-" * 50)

    if not hay_activos:
        print("No hay paquetes activos cargados.")

# -------------------------------------
# Funciones Contrato
# -------------------------------------

def altaContrato(_paquetes, _contratos):
    """
    Solicita información al usuario para dar de alta un contrato de viaje.

    Incluyendo el ID del turista, ID del paquete, cantidad de viajeros, medio de pago y la fecha del contrato.
    Calcula también el total a abonar (actualmente en 0). 
    
    Parametos: Recibe los diccionarios de paquetes y contratos. 
    
    Returns:
    ID del turista (str)
    ID del paquete (str)
    Cantidad de viajeros (int)
    Medio de pago (str)
    Total a pagar (actualmente siempre 0) (int)
    Fecha y hora de alta del contrato
    
    """
    #Ingreso ID turista
    _idTurista= str(input("Ingrese su ID de turista: ")) #FALTA VALIDACIÓN. 
    
    #Ingreso ID paquete
    _idPaquete= str(input("Ingrese el ID del paquete a abonar: "))
    
    _verificaNumeroDePaqueteBool, _verificaNumeroDePaqueteValor= verificaIDpaquete(_idPaquete, _paquetes)
    
    #Validación en bucle por si ingresa mal el número de paquete. 
    while _verificaNumeroDePaqueteBool == False:
        _idPaquete= str(input("Paquete no válido. Ingrese el ID del paquete a abonar: "))
        _verificaNumeroDePaqueteBool, _verificaNumeroDePaqueteValor= verificaIDpaquete(_idPaquete, _paquetes)
    
    #Ingreso cantidad de personas 
    _cantidadDeViajeros= int(input("Ingrese la cantidad de asistentes: "))
    #Valida cantidad de personas
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
        "ID turista": _idTurista,
        "ID paquete": _verificaNumeroDePaqueteValor,
        "Cantidad de personas": cantidadAsistentesValidado,
        "Total": _total,
        "Medios de pago": {
            "Elegido por usuario": [_medioDePago] ####Revisar 
        }
    }
    
    print(_contratos) #Eliminar - Solo verifica que se agregó el nuevo contrato al diccionario.

    return _idTurista, _idPaquete, cantidadAsistentesValidado, _medioDePago, _total, _fechaDeContrato, _idContrato


def verificaIDpaquete(_idPaquete, _paquetes): ################# HACER DOCSTRING
    '''Verifica que el número ingresado como ID de paquete sea valido.'''
    #formatoNombrePaquete = r"^PQT\d{3}$" #Formato del ID de un paquete.
    #if re.match(formatoNombrePaquete, _idPaquete) and
    
    if _idPaquete in _paquetes:
        return True, _idPaquete
    
    else:
        return False, _idPaquete 
 
 
def validaCantidadAsistentes(ingreso): ################# HACER DOCSTRING
    ''' Valida que la cantidad de asistentes sea un número positivo mayor a 0 y menor a 100 '''
    while ingreso < 0 or ingreso > 100:
        ingreso= int(input("No válido. Ingrese la cantidad de asistentes: "))
    
    return ingreso

def verificaIDturista (): ###Falta funciones turista.
    '''Verifica que el número de turista sea válido. '''
    
    return


def verificaIDcontrato(_idContrato, _contratos): #Revisar el else. 
    '''Verifica que el número ingresado como ID de contrato sea valido. '''
    if _idContrato in _contratos: #Agregar una validación para que solo tome los contratos activos. 
        return True, _idContrato
    
    elif _idContrato not in _contratos: 
        return False, _idContrato
    
    return

def bajaContrato(_paquetes, _contratos): 
    """
    De baja un contrato de viaje, utilizando el ID de turista y el ID del paquete.  
    Ademmás, registra la fecha y hora de la baja. 

    Returns:
    ID del turista (str)
    ID del paquete (str)
    Estado de cancelación (inicialmente 'False') (bool)
    Fecha y hora de la baja del contrato
    """
    cancelado= False #Eliminar 
    _idTurista= str(input("Ingrese su ID de turista: ")) #Falta validar ID turista.
    _idContrato= str(input("Ingrese el ID del contrato a dar de baja: "))
    
    _verificaNumeroDeContratoBool, _verificaNumeroDeContratoValor= verificaIDcontrato(_idContrato, _contratos)
    
    if _verificaNumeroDeContratoBool == True: 
        cancelado= True #Eliminar 
        _fechaDeBaja= datetime.datetime.now()
        print("Cancelado con éxito. Fecha de cancelación: ", _fechaDeBaja)
        
        #contratoAeliminar= _contratos.pop(_verificaNumeroDeContratoValor) #Esto lo elimina, no lo desactiva. 
        
        _contratos[_idContrato]["activo"]= False
        
        print(_contratos) ##Elimar. Solo verifico que se haya eliminado del diccionario de contratos. 
        
        return _idTurista, cancelado, _fechaDeBaja, _contratos
    
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
    _idContrato= str(input("Ingrese el ID del paquete a modificar: "))
    _fechaDeModificacion= datetime.datetime.now()
    
    #Verifica ID contrato
    idContratoVerificadoBool, idContratoVerificadoValor= verificaIDcontrato(_idContrato, _contratos)
    
    #Modifica el contrato 
    #if idContratoVerificadoBool == True:
        
        
    
    return (_idTurista, idContratoVerificadoValor, _fechaDeModificacion)

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    # Inicialización de variables
    clientes = {...}
    paquetes = {
    "PQT001": {
        "activo": True,
        "nombre": "Aventura en Salta",
        "destino": "Salta",
        "duracion": "5 días",
        "valor": 210000.0,
        "descripcion": "Excursiones y paisajes del norte argentino",
        "servicios": {
            "alojamiento": ["Hotel Solar del Cerro"],
            "actividad": ["City tour", "Visita a Cafayate"],
            "vuelo": ["JetSmart"]
        }
    },
    "PQT002": {
        "activo": True,
        "nombre": "Mendoza Full Wine",
        "destino": "Mendoza",
        "duracion": "4 días",
        "valor": 265000.0,
        "descripcion": "Degustaciones y hotel boutique en la montaña",
        "servicios": {
            "alojamiento": ["Cavas Wine Lodge"],
            "actividad": ["Bodega Norton", "Spa vinoterapia"],
            "vuelo": ["Aerolíneas Argentinas"]
        }
    },
    "PQT003": {
        "activo": True,
        "nombre": "Relax en Iguazú",
        "destino": "Misiones",
        "duracion": "6 días",
        "valor": 295000.0,
        "descripcion": "Naturaleza, hotel con pileta y parque temático",
        "servicios": {
            "alojamiento": ["Hotel La Cantera Jungle Lodge"],
            "actividad": ["Cataratas", "Parque de las Aves"],
            "traslado": ["Aeropuerto - Hotel"]
        }
    },
    "PQT004": {
        "activo": True,
        "nombre": "Bariloche Aventura",
        "destino": "Bariloche",
        "duracion": "7 días",
        "valor": 310000.0,
        "descripcion": "Trekking, kayak y nieve en la Patagonia",
        "servicios": {
            "alojamiento": ["Refugio Piedras Blancas"],
            "actividad": ["Trekking al cerro", "Rafting en el río"],
            "vuelo": ["Flybondi"]
        }
    },
    "PQT005": {
        "activo": True,
        "nombre": "Buenos Aires Clásico",
        "destino": "CABA",
        "duracion": "3 días",
        "valor": 180000.0,
        "descripcion": "Hotel céntrico y city tour cultural",
        "servicios": {
            "alojamiento": ["Hotel NH Tango"],
            "actividad": ["City Tour", "Cena Tango Show"]
        }
    },
    "PQT006": {
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
    "PQT007": {
        "activo": True,
        "nombre": "Tucumán Colonial",
        "destino": "Tucumán",
        "duracion": "4 días",
        "valor": 198000.0,
        "descripcion": "Ruta de la independencia y cerros del NOA",
        "servicios": {
            "alojamiento": ["Hotel Carlos V"],
            "actividad": ["Casa de Tucumán", "Excursión a Tafí del Valle"]
        }
    },
    "PQT008": {
        "activo": True,
        "nombre": "Sur Glaciar Express",
        "destino": "El Calafate",
        "duracion": "4 días",
        "valor": 320000.0,
        "descripcion": "Perito Moreno y navegación",
        "servicios": {
            "alojamiento": ["Hotel Kosten Aike"],
            "actividad": ["Glaciar Perito Moreno", "Navegación por Lago Argentino"],
            "vuelo": ["Aerolíneas Argentinas"]
        }
    },
    "PQT009": {
        "activo": True,
        "nombre": "Córdoba Sierras y Relax",
        "destino": "Córdoba",
        "duracion": "5 días",
        "valor": 230000.0,
        "descripcion": "Villa General Belgrano, caminatas y spa",
        "servicios": {
            "alojamiento": ["Cabañas Alpinas"],
            "actividad": ["Spa y senderismo", "Villa General Belgrano"],
            "traslado": ["Auto alquilado"]
        }
    },
    "PQT010": {
        "activo": True,
        "nombre": "San Juan y Valle de la Luna",
        "destino": "San Juan",
        "duracion": "6 días",
        "valor": 245000.0,
        "descripcion": "Naturaleza, fósiles y aventura paleontológica",
        "servicios": {
            "alojamiento": ["Hostería del Sol"],
            "actividad": ["Valle de la Luna", "Museo de Dinosaurios"],
            "traslado": ["Minivan desde aeropuerto"]
        }
    }
} ### Diccionarios de contratos 
    contratos = { "20000000000000": {
        "activo": True,
        "fecha": "2999-12-31 00:00:00.000000", #Fecha de alta de contrato 
        "ID turista": "0", ####### FALTA
        "ID paquete": "PQT002",
        "Cantidad de personas": 1,
        "Total": paquetes["PQT002"]["valor"] ,  
        "Medios de pago": {
            "Billeteras virtuales": ["Mercadopago", "Brubank", "UALA"],
            "Tarjetas": ["VISA", "MASTERCARD", "AMERICAN EXPRESS"],
            "Otros": ["Transferencia", "Efectivo"]
        }
    },
                  
    "20000023456789": {
        "activo": True,
        "fecha": "2025-01-12 14:15:00.000000",
        "ID turista": "1",
        "ID paquete": "PQT001",
        "Cantidad de personas": 3,
        "Total": paquetes["PQT001"]["valor"] * 3,
        "Medios de pago": {
            "Billeteras virtuales": ["Mercadopago", "Prex"],
            "Tarjetas": ["VISA", "CABAL"],
            "Otros": ["Transferencia"]
        }
    },
    "20000034567890": {
        "activo": True,
        "fecha": "2024-11-20 09:00:00.000000",
        "ID turista": "2",
        "ID paquete": "PQT002",
        "Cantidad de personas": 1,
        "Total": paquetes["PQT002"]["valor"],
        "Medios de pago": {
            "Billeteras virtuales": ["Brubank"],
            "Tarjetas": ["MASTERCARD"],
            "Otros": ["Efectivo"]
        }
    },
    "20000045678901": {
        "activo":True,
        "fecha": "2024-12-01 08:00:00.000000",
        "ID turista": "3",
        "ID paquete": "PQT003",
        "Cantidad de personas": 6,
        "Total": paquetes["PQT003"]["valor"] * 6,
        "Medios de pago": {
            "Billeteras virtuales": [],
            "Tarjetas": ["VISA"],
            "Otros": ["Efectivo"]
        }
    },
    "20000056789012": {
        "activo": True,
        "fecha": "2025-03-10 12:00:00.000000",
        "ID turista": "4",
        "ID paquete": "PQT004",
        "Cantidad de personas": 5,
        "Total": paquetes["PQT004"]["valor"] * 5,
        "Medios de pago": {
            "Billeteras virtuales": ["Mercadopago", "UALA"],
            "Tarjetas": ["AMERICAN EXPRESS"],
            "Otros": []
        }
    },
    "20000067890123": {
        "activo": True,
        "fecha": "2025-04-05 16:45:00.000000",
        "ID turista": "5",
        "ID paquete": "PQT005",
        "Cantidad de personas": 10,
        "Total": paquetes["PQT005"]["valor"] * 10,
        "Medios de pago": {
            "Billeteras virtuales": ["Prex", "UALA"],
            "Tarjetas": [],
            "Otros": ["Transferencia", "Efectivo"]
        }
    },
    "20000078901234": {
        "activo": True,
        "fecha": "2023-09-18 09:15:00.000000",
        "ID turista": "6",
        "ID paquete": "PQT006",
        "Cantidad de personas": 4,
        "Total": paquetes["PQT006"]["valor"] * 4,
        "Medios de pago": {
            "Billeteras virtuales": ["Brubank"],
            "Tarjetas": ["VISA", "MASTERCARD"],
            "Otros": []
        }
    },
    "20000089012345": {
        "activo": True,
        "fecha": "2025-05-30 11:00:00.000000",
        "ID turista": "7",
        "ID paquete": "PQT007",
        "Cantidad de personas": 8,
        "Total": paquetes["PQT007"]["valor"] * 8,
        "Medios de pago": {
            "Billeteras virtuales": ["Mercadopago"],
            "Tarjetas": ["CABAL", "AMERICAN EXPRESS"],
            "Otros": ["Efectivo"]
        }
    },
    "20000090123456": {
        "activo": True,
        "fecha": "2024-10-01 13:20:00.000000",
        "ID turista": "8",
        "ID paquete": "PQT010",
        "Cantidad de personas": 1,
        "Total": paquetes["PQT010"]["valor"],
        "Medios de pago": {
            "Billeteras virtuales": [],
            "Tarjetas": ["MASTERCARD"],
            "Otros": ["Transferencia"]
        }
    },
    "20000001234567": {
        "activo": True,
        "fecha": "2024-07-22 15:10:00.000000",
        "ID turista": "9",
        "ID paquete": "PQT009",
        "Cantidad de personas": 7,
        "Total": paquetes["PQT009"]["valor"] * 7,
        "Medios de pago": {
            "Billeteras virtuales": ["UALA"],
            "Tarjetas": ["VISA"],
            "Otros": ["Transferencia", "Efectivo"]
        }
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

        # Gestión de paquetes
        elif opcion == "2":
            while True:
                print()
                print("---------------------------")
                print("MENÚ DE PAQUETES")
                print("---------------------------")
                print("[1] Alta paquete")
                print("[2] Baja paquete")
                print("[3] Modificar paquete")
                print("---------------------------")
                print("[0] Volver al menú principal")
                print("---------------------------")
                print()

                sub = input("Seleccione una opción: ")
                if sub not in [str(i) for i in range(0,4)]:
                    input("Opción inválida. Presione ENTER para volver.")
                    continue
                print()
                if sub == "0":
                    break
               
                if sub == "1": # altaPaquete
                    paquetes = altaPaquete(paquetes) 
                    
                elif sub == "2":  # bajaPaquete
                    paquetes = eliminarPaquete(paquetes)
                    
                elif sub == "3":  # modificarPaquete
                    paquetes = modificarPaquete(paquetes)
                    
                input("\nENTER para continuar.")

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