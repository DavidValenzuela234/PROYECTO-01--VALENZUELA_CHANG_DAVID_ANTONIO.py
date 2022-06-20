from typing import List
import os
import lifestore_file
import heapq
seagrego = False

ListaVentas = []
ListaBusquedas = []
Ordenado = False
Opcion = ""

   
def ProductosMasVendidoyBuscados():
            print("")
            print("------------------------- 5 Productos Con Mayores Ventas ----------------------")


            for i in lifestore_file.lifestore_sales:
                seagrego = False
                for x in ListaVentas:
                    if x[0] == i[1]:
                        x[1] +=1
                        seagrego = True
                        continue
                    
                if seagrego == False:
                    ListaVentas.append([i[1], 1])
                    
        
            ListaVentas.sort(key=lambda x: x[1], reverse=True) 
            
            print("")
            print("1.- Se vendio " , ListaVentas[0][1], " veces el producto con el ID", ListaVentas[0][0], " - ", lifestore_file.lifestore_products[53][1])
            print("2.- Se vendio " , ListaVentas[1][1], " veces el producto con el ID", ListaVentas[1][0], " - ", lifestore_file.lifestore_products[2][1])
            print("3.- Se vendio " , ListaVentas[2][1], " veces el producto con el ID", ListaVentas[2][0], " - ", lifestore_file.lifestore_products[4][1])
            print("4.- Se vendio " , ListaVentas[3][1], " veces el producto con el ID", ListaVentas[3][0], " - ", lifestore_file.lifestore_products[41][1])
            print("4.- Se vendio " , ListaVentas[4][1], " veces el producto con el ID", ListaVentas[4][0], " - ", lifestore_file.lifestore_products[56][1])
            print("")
        
            print("------------------------- 10 Productos Con Mayores Busquedas ----------------------")

            for i in lifestore_file.lifestore_searches:
                seagrego = False
                for x in ListaBusquedas:
                    if x[0] == i[1]:
                        x[1] +=1
                        seagrego = True
                        continue
                    
                if seagrego == False:
                    ListaBusquedas.append([i[1], 1])

            ListaBusquedas.sort(key=lambda x: x[1], reverse=True)
            

            print("")
            print("1.- Se buscó " , ListaBusquedas[0][1], " veces el producto con el ID ", ListaBusquedas[0][0], " - ", lifestore_file.lifestore_products[53][1])
            print("2.- Se buscó " , ListaBusquedas[1][1], " veces el producto con el ID", ListaBusquedas[1][0], " - ", lifestore_file.lifestore_products[56][1])
            print("3.- Se buscó " , ListaBusquedas[2][1], " veces el producto con el ID", ListaBusquedas[2][0], " - ", lifestore_file.lifestore_products[28][1])
            print("4.- Se buscó " , ListaBusquedas[3][1], " veces el producto con el ID", ListaBusquedas[3][0], " - ", lifestore_file.lifestore_products[2][1])
            print("5.- Se buscó " , ListaBusquedas[4][1], " veces el producto con el ID", ListaBusquedas[4][0], " - ", lifestore_file.lifestore_products[3][1])
            print("6.- Se buscó " , ListaBusquedas[5][1], " veces el producto con el ID", ListaBusquedas[5][0], " - ", lifestore_file.lifestore_products[84][1])
            print("7.- Se buscó " , ListaBusquedas[6][1], " veces el producto con el ID", ListaBusquedas[6][0], " - ", lifestore_file.lifestore_products[66][1])
            print("8.- Se buscó " , ListaBusquedas[7][1], " veces el producto con el ID", ListaBusquedas[7][0], " - ", lifestore_file.lifestore_products[6][1])
            print("9.- Se buscó " , ListaBusquedas[8][1], " veces el producto con el ID", ListaBusquedas[8][0], " - ", lifestore_file.lifestore_products[4][1])
            print("10.- Se buscó " , ListaBusquedas[9][1], " veces el producto con el ID", ListaBusquedas[9][0], " - ", lifestore_file.lifestore_products[46][1])
            print("")

def ProductosMenosVendidoyBuscados():
            print("")
            print("------------------------- 5 Productos Con Menores Ventas ----------------------")
            print("")


            for i in lifestore_file.lifestore_sales:
                seagrego = False
                for x in ListaVentas:
                    if x[0] == i[1]:
                        x[1] +=1
                        seagrego = True
                        continue
                    
                if seagrego == False:
                    ListaVentas.append([i[1], 1])
                    
        
            ListaVentas.sort(key=lambda x: x[1]) 
            
            print("")
            print("1.- Se vendio " , ListaVentas[0][1], " veces el producto con el ID ", ListaVentas[0][0], " - ", lifestore_file.lifestore_products[9][1])
            print("2.- Se vendio " , ListaVentas[1][1], " veces el producto con el ID ", ListaVentas[1][0], " - ", lifestore_file.lifestore_products[12][1])
            print("3.- Se vendio " , ListaVentas[2][1], " veces el producto con el ID ", ListaVentas[2][0], " - ", lifestore_file.lifestore_products[16][1])
            print("4.- Se vendio " , ListaVentas[3][1], " veces el producto con el ID ", ListaVentas[3][0], " - ", lifestore_file.lifestore_products[21][1])
            print("4.- Se vendio " , ListaVentas[4][1], " veces el producto con el ID ", ListaVentas[4][0], " - ", lifestore_file.lifestore_products[27][1])
            print("")
        
            print("------------------------- 10 Productos Con Menores Busquedas ----------------------")

            for i in lifestore_file.lifestore_searches:
                seagrego = False
                for x in ListaBusquedas:
                    if x[0] == i[1]:
                        x[1] +=1
                        seagrego = True
                        continue
                    
                if seagrego == False:
                    ListaBusquedas.append([i[1], 1])

            ListaBusquedas.sort(key=lambda x: x[1])
            

            print("")
            print("1.- Se buscó " , ListaBusquedas[0][1], " veces el producto con el ID ", ListaBusquedas[0][0], " - ", lifestore_file.lifestore_products[8][1])
            print("2.- Se buscó " , ListaBusquedas[1][1], " veces el producto con el ID ", ListaBusquedas[1][0], " - ", lifestore_file.lifestore_products[9][1])
            print("3.- Se buscó " , ListaBusquedas[2][1], " veces el producto con el ID ", ListaBusquedas[2][0], " - ", lifestore_file.lifestore_products[26][1])
            print("4.- Se buscó " , ListaBusquedas[3][1], " veces el producto con el ID ", ListaBusquedas[3][0], " - ", lifestore_file.lifestore_products[34][1])
            print("5.- Se buscó " , ListaBusquedas[4][1], " veces el producto con el ID ", ListaBusquedas[4][0], " - ", lifestore_file.lifestore_products[44][1])
            print("6.- Se buscó " , ListaBusquedas[5][1], " veces el producto con el ID ", ListaBusquedas[5][0], " - ", lifestore_file.lifestore_products[58][1])
            print("7.- Se buscó " , ListaBusquedas[6][1], " veces el producto con el ID ", ListaBusquedas[6][0], " - ", lifestore_file.lifestore_products[69][1])
            print("8.- Se buscó " , ListaBusquedas[7][1], " veces el producto con el ID ", ListaBusquedas[7][0], " - ", lifestore_file.lifestore_products[79][1])
            print("9.- Se buscó " , ListaBusquedas[8][1], " veces el producto con el ID ", ListaBusquedas[8][0], " - ", lifestore_file.lifestore_products[92][1])
            print("10.- Se buscó " , ListaBusquedas[9][1], " veces el producto con el ID ", ListaBusquedas[9][0], " - ", lifestore_file.lifestore_products[12][1])
            print("")

def Menu():
    if (Usuario == "emtech" and Contraseña == "caso1"):
        while  True:
            input("Pulse Enter para ir al Menu")
            
            print("")
            os.system ("cls")
            print("---------------------------------------------------------------------------------------------------")
            print("                                          MENU")
            print("---------------------------------------------------------------------------------------------------")
            print("")

            print("1.- Ver los 5 productos con las mayores ventas y los 10 con las mayores busquedas")
            print("2.- Ver los 5 productos con las menores ventas y los 10 con las menores busquedas por categoria")
            print("3.- Salir")
            print("")
            Opcion = str(input("Seleccione la opción deseada: "))
            

            if Opcion == '1': 
                ProductosMasVendidoyBuscados()
                
            elif Opcion == "2":
                ProductosMenosVendidoyBuscados()

            elif Opcion == "3":
                exit() 
            else:
                print("Elige una de las opciones mencionadas")

    else:
        print("")
        print("Contraseña y/o Usuario incorrecto")     

print("")
print("---------------------------------------------------------------------------------------------------")
print("                                INICIO DE SESION ")
print("---------------------------------------------------------------------------------------------------")
print("")

Usuario = input("Escribe tu usuario: ")
Contraseña = input("Escribe tu contraseña: ")
print("")        

Menu()
