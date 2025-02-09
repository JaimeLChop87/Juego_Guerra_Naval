
import random
import time

class Guerra_naval():
    
    def __init__(self):
        self.filas = ["-","A","B","C","D","E","F","G","H","I","J"]
        self.columnas = ["1", "2", "3", "4", "5", "6", "7", "8", "9","10"]
        self.tableros_juego = {"Jug01":[],"Jug02":[],"PC":[],"PC2":[]}
        
        self.barcos = {
            "Porta_Aviones":(5,"A","No"),
            "Acorazado":(4,"C","No"),
            "Destructor":(3,"D","No"),
            "Fragata":(2,"F","No"),
            "Submarino_Atomico": (3,"S","No")           
        }
        self.horientaciones = ["V","H"]
    
    def menu_inicial (self):
        """muestra opciones de juego, el usuario selecciona opciones de menu
        1 , 2 , 3 , 4 segun seleccion, devuelve int con la opcion seleccionada"""
        self.OpcionesMenu = ["1","2","3","4"]
        
        while True:
            print(""" 
              *********** GUERRA NAVAL ********* 
                 ****************************
                    **********************""")
            print("""
                1- Jugador vs Pc
                2- Jugador vs Jugador
                3- Menu
                4- Salir""")
            self.User=input("seleccione Opcion_: ")
            
            #opcion salir del menu y aplicacion
            if self.User == "4":
                print("Saliendo de aplicacion") 
                break           
            
            elif self.User == "1":
                self.nombre_Jugador01 = input("Ingresar Nick_Name Jugador01: ")
                print(f"el jugador {self.nombre_Jugador01} Vs PC"  )
                table01 = app.crear_tablero()
                app.asignar_barcos_PC("Jug01",table01)
                table02 = app.crear_tablero()
                app.asignar_barcos_PC("PC",table02)
                app.jugar_guerra_naval(self.tableros_juego)
                
                
            elif self.User == "2":
                self.nombre_Jugador01 = input("Ingresar Nick_Name Jugador01")
                self.nombre_Jugador02 = input("Ingresar Nick_Name Jugador02")
                table01 = app.crear_tablero()
                app.asignar_barcos("Jug01",table01)
                table02 = app.crear_tablero()
                app.asignar_barcos("Jug02",table02)
                app.jugar_guerra_naval(self.tableros_juego)

    def crear_tablero (self):
        """crea tablero para el juego por jugador, tablero de 1-10 X A-J"""
        Tablero_Jugador={}
        Tablero_Jugador[self.filas[0]] = [x for x in range (1,11)]
            
        for fila in range(1,11):
            Tablero_Jugador[self.filas[fila]] = ["~"]*10
        
        return Tablero_Jugador

    def mostrar_tablero (self,tablero):
        tableroMuestra = tablero
        for letra, fila in tableroMuestra.items():
            filam = ""
            filam += letra
            for casilla in fila:
                if casilla == "~":
                    filam += f" \033[34m{casilla}\033[0m "
                elif casilla == "+":
                    filam += f" \033[93m{casilla}\033[0m "
                elif casilla == "*":
                    filam += f" \033[91m{casilla}\033[0m "
                elif str(casilla) in self.columnas:
                    filam += f" {casilla} "  
                else:
                    filam += f" \033[36m{casilla}\033[0m "
                
            print (filam)
     
    def verificar_choqueH (self,Tablero_Jugador):
        self.fraccionH = Tablero_Jugador[self.player_fila][int(self.player_columna)-1:int(self.player_columna)+ self.carga[0]-1]
        print (self.fraccionH)
        no_a=0
        for i in self.fraccionH:
            if i != "~":
                no_a += 1
            else:
                pass
        if no_a>0:
            return "NA"
        else:
            return "OK"
        
    def verificar_choqueV(self,Tablero_Jugador):
        
        self.fraccionV = []
        
        for fila in self.filas [self.filas.index(self.player_fila):self.carga[0]+self.filas.index(self.player_fila)]:
            item = Tablero_Jugador[fila][self.columnas.index(self.player_columna)]
            self.fraccionV.append(item)
        
        print(self.fraccionV)    
        no_a=0  
        for i in self.fraccionV:
            if i != "~":
                no_a += 1
            else:
                pass
        if no_a>0:
            return "NA"
        else:
            return "OK"        
    
    def modificar_tablero (self,barco,Tablero_Jugador):
        Tablero_Jugador = Tablero_Jugador
        if self.horientacion =="H":
            Tablero_Jugador[self.player_fila][int(self.player_columna)-1:int(self.player_columna)+self.carga[0]-1] = self.fraccionBarco
            print (f"Barco {barco} ingresado en coordenadas ({self.player_fila},{self.player_columna}) - {self.horientacion}")
        
        elif self.horientacion =="V":
            for fila in self.filas [self.filas.index(self.player_fila):self.carga[0]+self.filas.index(self.player_fila)]:
                Tablero_Jugador[fila][self.columnas.index(self.player_columna)] = self.barcos[barco][1]
                           
    def asignar_barcos (self,jugador,tablero):
        
        Tablero_Jugador = tablero       
        
        print("""
              ***indique las coordenadas para ubicar la unidad, 
              tenga en cuenta la horientacion y los espacios de la unidad***
              """)
        self.mostrar_tablero(Tablero_Jugador)
        for barco, self.carga in self.barcos.items():
            
            while True:
                print(f"Unidad_: {barco}\nEspacios: {self.carga[0]}")
                print(f"ingrese coordenadas (A-J,1-10) y horientacion (V, vertical - H, horizontal)")
                
                self.horientacion = input("Horientacion 'v/V'-Vertical 'h/H'-Horizontal )_: ").upper()
                self.player_columna = input("columna (1-10)_: ")
                self.player_fila = input("Fila (A-J)_: ").upper()
                self.fraccionBarco = [self.carga[1]]*self.carga[0]          
                
                if self.player_fila in self.filas and self.player_columna in self.columnas and self.horientacion in self.horientaciones:
                    if self.horientacion =="H":
     
                        if int(self.player_columna)-1  + self.carga[0] > 10:
                            print("No se tiene espacio en tablero")
                            del self.horientacion, self.player_columna,self.player_fila
                        elif self.verificar_choqueH(Tablero_Jugador) == "NA":
                            print(f"Una de las unidades interfiere con la ubicacion... reasignar ubicacion {barco}")
                            del self.horientacion, self.player_columna,self.player_fila
                        else:
                            self.modificar_tablero (barco,Tablero_Jugador)
                            self.mostrar_tablero(Tablero_Jugador)
                            del self.horientacion, self.player_columna,self.player_fila
                            break
                        
                    elif self.horientacion =="V":
                        
                        if int(self.filas.index(self.player_fila))-1+self.carga[0] > len(self.filas)-1:
                            print("No se tiene espacio en tablero")
                            del self.horientacion, self.player_columna,self.player_fila
                        
                        elif self.verificar_choqueV(Tablero_Jugador) == "NA":
                            print(f"Una de las unidades interfiere con la ubicacion... reasignar ubicacion {barco}")
                            del self.horientacion, self.player_columna,self.player_fila
                        else:
                            self.modificar_tablero (barco,Tablero_Jugador)
                            self.mostrar_tablero(Tablero_Jugador)
                            del self.horientacion, self.player_columna,self.player_fila
                            break
                             
                else:
                    print("****los valores ingresados no se identifican en los rangos especificados****")                 
            
        self.tableros_juego[jugador].insert(0,Tablero_Jugador)
        del Tablero_Jugador  
        return  f"se genero tablero jugador {jugador}_{self.nombre_Jugador01}"  

    def asignar_barcos_PC (self,jugador,tablero):
        
        Tablero_Jugador = tablero       
        
        print("""
              ***Generando tablero PC***
              """)
        self.mostrar_tablero(Tablero_Jugador)
        for barco, self.carga in self.barcos.items():
            
            while True:
                #time.sleep(1)
                print(f"Unidad_: {barco}\nEspacios: {self.carga[0]}")
                print(f"ingrese coordenadas (A-J,1-10) y horientacion (V, vertical - H, horizontal)")
                
                self.horientacion = self.horientaciones[random.randint(0, len(self.horientaciones)-1)]
                self.player_columna = self.columnas[random.randint(0, len(self.columnas)-1)]
                self.player_fila = self.filas[random.randint(1, len(self.filas)-1)]
                self.fraccionBarco = [self.carga[1]]*self.carga[0]          
                
                if self.player_fila in self.filas and self.player_columna in self.columnas and self.horientacion in self.horientaciones:
                    if self.horientacion =="H":
     
                        if int(self.player_columna)-1  + self.carga[0] > 10:
                            print("No se tiene espacio en tablero")
                            del self.horientacion, self.player_columna,self.player_fila
                        elif self.verificar_choqueH(Tablero_Jugador) == "NA":
                            print(f"Una de las unidades interfiere con la ubicacion... reasignar ubicacion {barco}")
                            del self.horientacion, self.player_columna,self.player_fila
                        else:
                            self.modificar_tablero (barco,Tablero_Jugador)
                            #self.mostrar_tablero(Tablero_Jugador)
                            del self.horientacion, self.player_columna,self.player_fila
                            break
                        
                    elif self.horientacion =="V":
                        
                        if int(self.filas.index(self.player_fila))-1+self.carga[0] > len(self.filas)-1:
                            print("No se tiene espacio en tablero")
                            del self.horientacion, self.player_columna,self.player_fila
                        
                        elif self.verificar_choqueV(Tablero_Jugador) == "NA":
                            print(f"Una de las unidades interfiere con la ubicacion... reasignar ubicacion {barco}")
                            del self.horientacion, self.player_columna,self.player_fila
                        else:
                            self.modificar_tablero (barco,Tablero_Jugador)
                            #self.mostrar_tablero(Tablero_Jugador)
                            del self.horientacion, self.player_columna,self.player_fila
                            break
                             
                else:
                    print("****los valores ingresados no se identifican en los rangos especificados****")                 
            
        self.tableros_juego[jugador].insert(0,Tablero_Jugador)
        del  Tablero_Jugador   
        return  f"se genero tablero jugador {jugador}"

    def jugar_guerra_naval (self, tableros_juego):
        
        tableros_juego = tableros_juego
        
        jugadorespartida = []
        for jugador, items in tableros_juego.items():
            if len(items)>0:
                jugadorespartida.append(jugador)
        
        OpcionesTiro01 = []
        OpcionesTiro02 = []
        for fila in self.filas[1:len(self.filas)-1]:
            for columna in self.columnas:
                OpcionesTiro01.append ((fila,columna))
                OpcionesTiro02.append ((fila,columna))
            
        tablerotiroJug01 = self.crear_tablero()
        tableros_juego[f"{jugadorespartida[0]}"].insert (1,tablerotiroJug01)
        
        tablerotiroJug02 = self.crear_tablero()
        tableros_juego[f"{jugadorespartida[1]}"].insert (1,tablerotiroJug02)
        
        self.PuntosJugador01 = 0
        self.PuntosJugador02 = 0
          
        turno = 0
        while (self.PuntosJugador01 < 17) and (self.PuntosJugador02 < 17):
            #time.sleep(0.2)
            if str(jugadorespartida[turno]) == "PC" or  str(jugadorespartida[turno]) == "PC2":
                print(f"*** Calculando coordenadas mediante IA NavalGAme ***")
                self.player_columna = self.columnas[random.randint(0, len(self.columnas)-1)]
                self.player_fila = self.filas[random.randint(1, len(self.filas)-1)]
                tiro = (self.player_fila,self.player_columna)
            else: 
                print(f"*** Ingresar coordenadas de tiro jugador {jugadorespartida[turno]} ***")
                self.player_columna = input("columna (1-10)_: ")
                self.player_fila = input("Fila (A-J)_: ").upper()
                tiro = (self.player_fila,self.player_columna)
            
            print (jugadorespartida[turno])
            if turno == 0:                                          
                
                while self.player_fila in self.filas and self.player_columna in self.columnas:
                    print(tiro)
                    if tableros_juego[f"{jugadorespartida[1]}"][0][tiro[0]][self.columnas.index(tiro[1])]=="~":
                        
                        if tableros_juego[f"{jugadorespartida[0]}"][1][tiro[0]][self.columnas.index(tiro[1])]== "+":
                            print(f"*** en las cordenadas {tiro} ya se efectuo disparo, volver a ingresar ***")
                            del self.player_columna , self.player_fila
                            break
                        
                        else:    
                            print("*** no se impactó ninguna unidad ***")
                            tableros_juego[f"{jugadorespartida[0]}"][1][tiro[0]][self.columnas.index(tiro[1])]= "+"
                            self.mostrar_tablero(tableros_juego[f"{jugadorespartida[0]}"][1])
                            self.mostrar_tablero(tableros_juego[f"{jugadorespartida[1]}"][0])
                            del self.player_columna , self.player_fila
                            turno = 1
                            break
                            
                    elif tableros_juego[f"{jugadorespartida[0]}"][1][tiro[0]][self.columnas.index(tiro[1])]== "*":
                            print(f"*** en las cordenadas {tiro} ya se efectuo disparo, volver a ingresar ***")
                            del self.player_columna , self.player_fila
                            break
                    else:
                        print("*** IMPACTO A UNIDAD ENEMIGA ***")
                        tableros_juego[f"{jugadorespartida[0]}"][1][tiro[0]][self.columnas.index(tiro[1])]= "*"
                        self.mostrar_tablero(tableros_juego[f"{jugadorespartida[0]}"][1])
                        self.mostrar_tablero(tableros_juego[f"{jugadorespartida[1]}"][0])
                        del self.player_columna , self.player_fila
                        self.PuntosJugador01 += 1
                        print(f"Puntos jugador01 {self.PuntosJugador01}")
                        turno = 1
                        break

            else:                                          
                
                while self.player_fila in self.filas and self.player_columna in self.columnas:
                    print(tiro)
                    if tableros_juego[f"{jugadorespartida[0]}"][0][tiro[0]][self.columnas.index(tiro[1])]=="~":
                        
                        if tableros_juego[f"{jugadorespartida[1]}"][1][tiro[0]][self.columnas.index(tiro[1])]== "+":
                            print(f"*** en las cordenadas {tiro} ya se efectuo disparo, volver a ingresar ***")
                            del self.player_columna , self.player_fila
                            break
                        
                        else:    
                            print("*** no se impactó ninguna unidad ***")
                            tableros_juego[f"{jugadorespartida[1]}"][1][tiro[0]][self.columnas.index(tiro[1])]= "+"
                            self.mostrar_tablero(tableros_juego[f"{jugadorespartida[1]}"][1])
                            self.mostrar_tablero(tableros_juego[f"{jugadorespartida[0]}"][0])
                            del self.player_columna , self.player_fila
                            turno = 0
                            break
                            
                    elif tableros_juego[f"{jugadorespartida[1]}"][1][tiro[0]][self.columnas.index(tiro[1])]== "*":
                            print(f"*** en las cordenadas {tiro} ya se efectuo disparo, volver a ingresar ***")
                            del self.player_columna , self.player_fila
                            break
                    else:
                        print("*** IMPACTO A UNIDAD ENEMIGA ***")
                        tableros_juego[f"{jugadorespartida[1]}"][1][tiro[0]][self.columnas.index(tiro[1])]= "*"
                        self.mostrar_tablero(tableros_juego[f"{jugadorespartida[1]}"][1])
                        self.mostrar_tablero(tableros_juego[f"{jugadorespartida[0]}"][0])
                        del self.player_columna , self.player_fila
                        self.PuntosJugador02 += 1
                        print(f"Puntos jugador02 {self.PuntosJugador02}")
                        turno = 0
                        break                                     
        print(f"Puntos jugador01 {self.PuntosJugador01}")
        print(f"Puntos jugador02 {self.PuntosJugador02}")                 
        if self.PuntosJugador01  > self.PuntosJugador02:
            print (f"jugador {jugadorespartida[0]} ganador ")
        else:
             print (f"jugador {jugadorespartida[1]} ganador")            
 
                        
if __name__ == "__main__":
    app = Guerra_naval() 

    app.menu_inicial()


