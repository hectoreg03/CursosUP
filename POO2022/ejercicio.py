class Trabajador():
    salario : int
    nombre  : str
    antiguedad : int
    
    def __init__(self, nm,r):
        self.nombre = nm
        self.antiguedad = r
        
    def trabajar(self):
        pass
    
    def getsalary(self):
        return self.salario
    

class Gerente(Trabajador):
    def __init__(self, nm, r):
        self.nombre = nm
        self.salario = 50000
        self.antiguedad = r
        
    def trabajar(self):
        print("El gerente ",self.nombre," esta gerenciando")

    def nuevo_salario(self, empleado : TrabajadorAntiguo, nuevo_salario):
        if empleado.salario < nuevo_salario :
            empleado.salario = nuevo_salario - (1000*self.antiguedad)
        
class TrabajadorAntiguo(Trabajador):
    def getsalary(self):
        return self.salary+(1000*self.antiguedad)

class Programador(TrabajadorAntiguo):
    def __init__(self, nm, r):
        self.nombre = nm
        self.salario = 25000
        self.antiguedad = r
        
    def trabajar(self):
        print("El programador ",self.nombre," esta programando")
        
        
class Secretaria(TrabajadorAntiguo):
    def __init__(self, nm, r):
        self.nombre = nm
        self.salario = 5000
        self.antiguedad = r
        
    def trabajar(self):
        print("La secretaria ",self.nombre," esta apoyando")


def main():
    empresa=[]
    empleados = int(input("Ingrese la cantidad de empleados que tiene la empresa\n"))
    l = 0
    for i in range(empleados):
        print("Los puestos son:\n 1.- Gerente\n 2.- Programador\n 3.-Secretaria\n")
        l = 4
        while l < 1 and l > 3 :
            l = int( input("Ingrese el tipo de puesto\n") )
            if l == 1 :
                nombre  = input("Ingrese el nombre del empleado\n")
                antiguedad = int(input("Ingrese la antiguedad del empleado\n"))
                r = Gerente(nombre,antiguedad)
                empresa.append(r)
            elif l== 2:
                nombre  = input("Ingrese el nombre del empleado\n")
                antiguedad = int(input("Ingrese la antiguedad del empleado\n"))
                r = Programador(nombre,antiguedad)
                empresa.append(r)
            elif l==3:
                nombre  = input("Ingrese el nombre del empleado\n")
                antiguedad = int(input("Ingrese la antiguedad del empleado\n"))
                r = Secretaria(nombre,antiguedad)
                empresa.append(r)
            else:
                print("Ha dado un puesto inavlido, vuelva a ingresarlo\n")
    consultas = int(input("Ingrese la cantidad de consultas que desea hacer\n"))
    for i in range(consultas):
        print("Hola")
