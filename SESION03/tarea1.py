'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
Crear un menú para crear objetos y realizar las diversas operaciones referidas.

'''

import datetime

class CuentaBancaria:
    def __init__(self, numeroCta, nombreCliente, saldo):
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__fechaApertura = datetime.date.today()
        self.__saldo = saldo if saldo >= 100000 else 100000

    def get_detalles(self):
        return f"Cuenta: {self.__numeroCta}, Cliente: {self.__nombreCliente}, Fecha: {self.__fechaApertura}, Saldo: {self.__saldo}"

    def consignar(self, monto):
        if monto > 0: 
            self.__saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.__saldo: 
            self.__saldo -= monto

def menu():
    cuentas = {}
    while True:
        print("1. Abrir cuenta\n2. Consignar\n3. Retirar\n4. Mostrar detalles\n5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre del cliente: ")
            saldo = float(input("Saldo inicial: "))
            numero = len(cuentas) + 1
            cuentas[numero] = CuentaBancaria(numero, nombre, saldo)
            print(f"Cuenta {numero} creada.\n")
        
        elif opcion == '2':
            numero = int(input("Número de cuenta: "))
            if numero in cuentas:
                monto = float(input("Monto a consignar: "))
                cuentas[numero].consignar(monto)
        
        elif opcion == '3':
            numero = int(input("Número de cuenta: "))
            if numero in cuentas:
                monto = float(input("Monto a retirar: "))
                cuentas[numero].retirar(monto)
        
        elif opcion == '4':
            numero = int(input("Número de cuenta: "))
            if numero in cuentas:
                print(cuentas[numero].get_detalles())
        
        elif opcion == '5':
            break

if __name__ == "__main__":
    menu()

55
