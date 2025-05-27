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
# IDPaquete (str)
# Cantidad de personas (int)
# Total (float)
# Forma de pago (str)

# MÓDULOS
#----------------------------------------------------------------------------------------------
import datetime 


# FUNCIONES
#----------------------------------------------------------------------------------------------
def altaCliente(_clientes):
    ...
    return _clientes


def altaContrato():
    """
    Solicita información al usuario para dar de alta un contrato de viaje.

    Incluyendo el ID del turista, ID del paquete, cantidad de viajeros, medio de pago y la fecha del contrato.
    Calcula también el total a abonar (actualmente en 0). 

    Returns:
    ID del turista (str)
    ID del paquete (str)
    Cantidad de viajeros (int)
    Medio de pago (str)
    Total a pagar (actualmente siempre 0) (int)
    Fecha y hora del contrato
    
    """
    _precio= 0 
    _idTurista= str(input("Ingrese su ID de turista: "))
    _idPaquete= str(input("Ingrese el ID del paquete a abonar: "))
    _cantidadDeViajeros= int(input("Ingrese la cantidad de asistentes: "))
    _medioDePago= str(input("Ingrese medio de pago a utilizar: "))
    _total= _precio*_cantidadDeViajeros
    _fechaDeContrato= datetime.datetime.now()

    return _idTurista, _idPaquete, _cantidadDeViajeros, _medioDePago, _total, _fechaDeContrato


def bajaContrato():
    """
    De baja un contrato de viaje, utilizando el ID de turista y el ID del paquete.  
    Ademmás, registra la fecha y hora de la baja. 

    Returns:
    ID del turista (str)
    ID del paquete (str)
    Estado de cancelación (inicialmente `False`) (bool)
    Fecha y hora de la baja del contrato
    """
    cancelado= False 
    _idTurista= str(input("Ingrese su ID de turista: "))
    _idPaquete= str(input("Ingrese el ID del paquete a dar de baja: "))
    _fechaDeBaja= datetime.datetime.now()
    
    return _idTurista, _idPaquete, cancelado, _fechaDeBaja


def modficarContrato():
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
    _idPaquete= str(input("Ingrese el ID del paquete a modificar: "))
    _fechaDeModificacion= datetime.datetime.now()
    
    return (_idTurista, _idPaquete,_fechaDeModificacion)
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    # Inicialización de variables
    clientes = {...}
    paquetes = {...}
    contratos = {...}

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
                if sub == "0": break
                if sub == "1": ...  # altaPaquete
                elif sub == "2": ...  # bajaPaquete
                elif sub == "3": ...  # modificarPaquete
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
                    altaContrato()
                    
                elif sub == "2":# bajaContrato
                    bajaContrato()
                    
                elif sub == "3":# modificarContrato
                    modficarContrato() 
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
