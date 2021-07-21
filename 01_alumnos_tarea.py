#PROGRAMA PARA GESTION DE ALUMNOS
#DEFINIR VARIABLES DE ENTRADA Y SALIDAS
alumnos = []
alumno={}
salir='no'
# LOGICA

def createAlumno(nombre, email,celular):
    # print("REGISTRO DE NUEVO ALUMNO")
        nuevoAlumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }    
        alumnos.append(nuevoAlumno)
        return 1

def readAlumno():
        print("LISTADO DE ALUMNOS")
        # print(alumnos)
        for  a in alumnos:
            print("===================================")
            for clave,valor in a.items():                
                print(clave + " : " + valor)

def updateAlumno():
    print("MODIFICACIÓN DE ALUMNOS")
    buscarNombre=input('Ingrese el nombre del alumno a modificar: ')

    i=0
    finded=False
    for a in alumnos:
        for clave,valor in a.items():
            if valor==buscarNombre:            
                # print(buscarNombre + " se encuentra en la posición de la lista " + str(i))  
                finded=True
                # break  
        if finded==False:
            i+=1   

    if finded==False:
        print('No existe el alumno ' + str(buscarNombre) + 'en el sistema')
    else:            
        email=input('Ingrese email a modificar: ')            
        celular=input('Ingrese celular a modificar: ')            
        alumnos[i]['email']=email    
        alumnos[i]['celular']=celular     
        print(alumnos[i]) 
        return 1       
                        
def deleteAlumno():
    print("ELIMINACIÓN DE ALUMNOS")
    buscarNombre=input('Ingrese el nombre del alumno a eliminar: ')

    i=0
    finded=False
    for a in alumnos:
        for clave,valor in a.items():
            if valor==buscarNombre:            
                # print(buscarNombre + " se encuentra en la posición de la lista " + str(i))  
                finded=True
                # break  
        if finded==False:
            i+=1   

    if finded==False:
        print('No existe el alumno ' + str(buscarNombre) + ' en el sistema')
    else:                
        del alumnos[i] 
        # print(alumnos[i])  
        return 1 

while(salir=='no'):
    print("OPCIONES : 1 - registrar alumno | 2 - mostrar alumnos | 3 - modificar alumnos | 4 - eliminar alumnos")
    opcion = input()
    if(opcion == "1"):
        print("REGISTRO DE NUEVO ALUMNO:")
        nombre = input("NOMBRE:")
        email = input("EMAIL:")
        celular = input("CELULAR:")
        r=createAlumno(nombre, email,celular)
        if r==1:
            print("REGISTRO EXITOSO")

    elif(opcion == "2"):
        readAlumno()

    elif(opcion == "3"):        
        r=updateAlumno()
        if r==1:            
            print("MODIFICACIÓN EXITOSA")    

    elif(opcion == "4"):        
        r=deleteAlumno()
        if r==1:            
            print("ELIMINACIÓN EXITOSA")    

    else:
        print("Marco una opcion incorrecta")
        continue        
    print("Desea salir del programa?")
    salir  = input()

# MOSTRAR RESULTADOS